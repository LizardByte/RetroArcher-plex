import argparse
import asyncio
import hashlib
import json
import logging
import os
import random
import shutil
import socket
import subprocess
import sys
import time
import uuid
import webbrowser

from datetime import datetime
from threading import Thread
from queue import Queue

adb_connected = None

q = Queue()


async def auth_callback(request):
    error = request.query.get("error")
    if error:
        description = request.query.get("error_description")
        print(f"Error in auth_callback: {description}")
        return
    # Run in task to not make unsuccessful parsing the HTTP response fail
    asyncio.create_task(queue.put(request.query["code"]))
    return web.Response(
        headers={"content-type": "text/html"},
        text="<script>window.close()</script>",
    )


def config_to_dict(config_file):
    def splitter(line):
        return line.split('=', 1)

    with open(config_file, 'r') as f:
        text = f.read().rstrip('\n')
        header, *data_lines = text.split('\n')

    data = dict(map(splitter, data_lines))

    return header, data


def config_rewrite(config_file, header, data):
    with open(config_file, 'w') as f:
        data_lines = list(map('='.join, data.items()))
        text = '\n'.join([header] + data_lines)
        f.write(text)


def convert_xml_to_json(filepath):
    try:
        input_file = open(filepath, 'rb')
        j = xmltodict.parse(input_file)
    except FileNotFoundError:
        j = {}

    return j


def get_json_from_xml(url):
    headers = {
        'Accept': 'application/xml'
    }

    xml = requests.get(url=url, headers=headers).text

    result = xmltodict.parse(xml)

    return result


def get_paths():
    # build_directories
    path_dict = {}
    script = os.path.realpath(__file__)  # get current script directory

    paths_to_get = {
        0: 'script',
        1: 'scriptDir',
        2: 'codeDir',
        3: 'contentsDir',
        4: 'pluginDir',
        5: 'pluginsDir',
        6: 'plexDir',
        7: 'appDir'
    }
    for path_to_get in paths_to_get:
        if path_to_get == 0:
            path_dict['script'] = script
        else:
            path = os.path.dirname(path_dict[paths_to_get[path_to_get - 1]])
            path_dict[paths_to_get[path_to_get]] = path

    path_dict['agentModulesDir'] = os.path.join(path_dict['contentsDir'], 'Libraries', 'Shared')
    path_dict['retroarcherModulesDir'] = os.path.join(path_dict['contentsDir'], 'Libraries', 'Modules')
    path_dict['retroarcherStartVideosDir'] = os.path.join(path_dict['contentsDir'], 'Resources', 'StartVideos')
    path_dict['retroarcherFontDir'] = os.path.join(path_dict['contentsDir'], 'Resources', 'Fonts')
    path_dict['retroarcherFFMPEGDir'] = os.path.join(path_dict['contentsDir'], 'Resources', 'ffmpeg')

    logging.debug(f'Paths: {path_dict}')
    return path_dict


def get_settings(directory, plugin):
    settings_file_name = os.path.join(directory, 'Plug-in Support', 'Preferences', f'{plugin}.xml')
    return settings_file_name


def get_data_folders(directory, plugin):
    folders = {
        'dataFolder': os.path.join(directory, 'Plug-in Support', 'Data', plugin),
        'mediaFolder': os.path.join(directory, 'Plug-in Support', 'Data', plugin, 'media'),
        'dbFolder': os.path.join(directory, 'Plug-in Support', 'Data', plugin, 'database')
    }
    return folders


def launcher():
    # kill any lingering emulator processes
    emulator_processes = ['cemu', 'cemu.exe', 'retroarch', 'retroarch.exe', 'rpcs3', 'rpcs3.exe']

    for proc in psutil.process_iter():
        if proc.name().lower() in emulator_processes:
            proc.kill()

    # get server/moonlight info
    if not Prefs['str_MoonlightPcUuid']:
        server_info = get_json_from_xml(Prefs['url_GameStreamServerAddress'])
        logging.debug('server_info: %s' % (json.dumps(server_info, indent=4)))
        moonlight_pc_uuid = server_info['root']['uniqueid']
    else:
        moonlight_pc_uuid = Prefs['str_MoonlightPcUuid']
    logging.info(f'moonlight_pc_uuid: {moonlight_pc_uuid}')

    moonlight_app_name = Prefs['str_MoonlightAppName']

    moonlight_app_id = Prefs['str_MoonlightAppId']

    if not Prefs['str_MoonlightAppId']:
        logging.info('GameStreamHost: %s' % (Prefs['enum_GameStreamHost']))
        if Prefs['enum_GameStreamHost'] == 'GeForce Experience':
            nvstreamsvc_path = os.path.join(os.path.expandvars('$programdata'), 'NVIDIA Corporation', 'nvstreamsvc')

            nvsstreamsvr_logs = ['nvstreamsvcCurrent.log', 'nvstreamsvcOld.log']

            app_id_found = False
            for log in nvsstreamsvr_logs:
                if not app_id_found:
                    nv_log_file = os.path.join(nvstreamsvc_path, log)
                    if os.path.isfile(nv_log_file):
                        with open(nv_log_file, 'r') as f:
                            log_contents = f.read()
                        # find titles
                        title_split = log_contents.split('Title=')
                        title_counter = 0

                        while title_counter < len(title_split):
                            if title_split[title_counter].splitlines()[0].lower() == moonlight_app_name.lower():
                                moonlight_app_id = title_split[title_counter].split('AppId=', 1)[-1].splitlines()[0]
                                app_id_found = True
                                break
                            title_counter += 1

        else:
            moonlight_app_id = '1'

    logging.info(f'moonlight_app_id: {moonlight_app_id}')

    # convert movie_name to rom_name
    game_name_full = os.path.basename(movie_name)  # the file name
    system = platform_path(movie_name)

    # key = os.path.join(system, game_name_full)
    video_key = game_name_full
    logging.info(f'video_key: {video_key}')

    json_dir = data_folders['dbFolder']
    json_file = os.path.join(json_dir, 'database.json')
    with open(json_file) as f:
        database = json.load(f)

    secrets_file = os.path.join(json_dir, 'secrets.json')
    try:
        with open(secrets_file) as f:
            secrets = json.load(f)
    except FileNotFoundError:
        pass

    rom_folder = database['romMapping']['platforms'][system]['videos'][video_key]['romFolder']
    rom_file = database['romMapping']['platforms'][system]['videos'][video_key]['romFile']

    rom_name = os.path.join(rom_folder, rom_file)

    logging.info(f'rom_name: {rom_name}')

    system_key = system.lower().replace(' ', '_')

    emulator = archer_dict.dPlatformMapping[system]['emulators'][Prefs[f'emulator_{system_key}']]
    logging.debug(f'emulator: {emulator}')

    application_directory = Prefs[f'dir_app_{emulator}']
    binary_command = Prefs[f'str_binary_{emulator}']

    if emulator == 'retroarch':
        core = archer_dict.dPlatformMapping[system]['emulators'][emulator]['cores'][Prefs[f'core_{system_key}']]
        logging.info(f'core: {core}')
        emulator_core = os.path.join('cores', core)
        logging.info(f'emulator_core: {emulator_core}')
    else:
        emulator_core = ''

    full_rom_path = os.path.join(source_rom_dir, rom_name)
    logging.info(f'full_rom_path: {full_rom_path}')

    user_id_rpcs3 = client_user_id
    user_id_cemu = client_user_id
    user_id_temp = client_user_id
    user_id_length = len(client_user_id)
    try:
        int(user_id_temp)
        while user_id_length != 8:
            if user_id_length < 8:
                user_id_temp = f'0{user_id_temp}'
            else:
                user_id_temp = user_id_temp[1:]
            user_id_rpcs3 = user_id_temp
            user_id_cemu = str(int(user_id_temp) + 80000000)
            user_id_length = len(user_id_temp)
    except TypeError:
        logging.error(f'User ID is not an integer: {client_user_id}')

    system_platform_mapping = {
        'win32': {
            'emulators': {
                'cemu': {
                    'dir': application_directory,
                    'command': [binary_command, '--fullscreen', '--game', full_rom_path, '--account', user_id_cemu]
                },
                'retroarch': {
                    'dir': application_directory,
                    'command': [binary_command, '-L', emulator_core, full_rom_path]
                },
                'rpcs3': {
                    'dir': application_directory,
                    'command': [binary_command, '--no-gui', full_rom_path, '--user-id', user_id_rpcs3]
                }
            },
            'stream_host': {
                'GeForce Experience': {
                    'process': 'nvstreamer.exe',
                },
                'OpenStream': {
                    'process': 'openstream.exe'
                },
                'Sunshine': {
                    'process': 'sunshine.exe'
                }
            }
        }
        # 'linux' : 'tbd',
        # 'macOS' : 'tbd'
    }

    platform = sys.platform
    logging.info(f'platform: {platform}')

    try:
        system_platform_mapping[platform]
    except KeyError:
        logging.critical(f'system os not support: {platform}')
        sys.exit(1)

    emulator_path = os.path.join(system_platform_mapping[platform]['emulators'][emulator]['dir'])
    logging.info(f'emulator_path: {emulator_path}')

    # verify/create user profile folder and file for cemu
    if emulator == 'cemu':
        user_profile_path_cemu = os.path.join(emulator_path, 'mlc01', 'usr', 'save', 'system', 'act', user_id_cemu)
        user_profile_file_cemu = os.path.join(user_profile_path_cemu, 'account.dat')

        user_profile_path_exists_cemu = os.path.isdir(user_profile_path_cemu)
        user_profile_file_exists_cemu = os.path.isfile(user_profile_file_cemu)

        # create the user profile if it doesn't exist
        if not user_profile_path_exists_cemu or not user_profile_file_exists_cemu:
            default_cemu_account_file = os.path.join(emulator_path, 'mlc01', 'usr', 'save', 'system', 'act',
                                                     '80000001', 'account.dat')
            if os.path.isfile(default_cemu_account_file):
                make_dir(user_profile_path_cemu)
                copy_file(default_cemu_account_file, user_profile_file_cemu)
            else:
                logging.critical('Failed to copy default cemu user profile. Exiting.')
                sys.exit()

        # rewrite the account file everytime
        user_profile_file_exists_cemu = os.path.isfile(user_profile_file_cemu)
        if user_profile_file_exists_cemu:
            # parse and replace some stuff in the file
            header, data = config_to_dict(user_profile_file_cemu)

            data['PersistentId'] = user_id_cemu

            # check if Uuid is the same as the default Uuid value
            # if equal to this, then change it, otherwise leave it alone
            if data['Uuid'] == 'e9df01108a453a2c90e94adc35c9528a':
                data['Uuid'] = str(uuid.uuid1()).replace('-', '')
            data['TransferableIdBase'] = '2000004%s' % (data['Uuid'][-8:])

            mii_name_max_length = 10
            mii_loop_counter = 0
            data['MiiName'] = ''
            data['MiiData'] = '010001100000cc6f030034330100010001000100010001000100'
            while mii_loop_counter < mii_name_max_length:
                try:
                    data['MiiName'] += '00'
                    data['MiiName'] += client_user_name[mii_loop_counter].encode('utf-8').hex()

                    data['MiiData'] += '00'
                    data['MiiData'] += client_user_name[mii_loop_counter].encode('utf-8').hex()
                except IndexError:
                    data['MiiName'] += '0000'
                    data['MiiData'] += '0100'
                mii_loop_counter += 1
            data['MiiName'] += '0000'
            data['MiiData'] += '0100%s' % (
                '010001000100010001000106010001000100010001000100010001000100010001000100010001000100010001000100')

            config_rewrite(config_file=user_profile_file_cemu, header=header, data=data)

    # probably should replace client_platform with client_device
    if client_platform.lower() == 'android' or client_device.lower() == 'android':
        launch_status = launch_adb(moonlight_pc_uuid, moonlight_app_id)
    elif client_platform.lower() == 'windows' or client_device.lower() == 'windows':
        launch_status = launch_windows(moonlight_pc_uuid, moonlight_app_name, secrets)
    elif client_platform.lower() == 'xbox':
        launch_status = launch_xbox()
    elif client_platform.lower() == 'atv':  # apple tv
        launch_status = launch_ios()
    else:
        launch_status = False

    if launch_status:
        command = system_platform_mapping[platform]['emulators'][emulator]['command']
        logging.debug(f'command: {command}')

        # start the emulator
        try:
            emu_proc = subprocess.Popen(args=command, cwd=emulator_path, shell=True)
        except subprocess.CalledProcessError as cpe:
            # error handling
            logging.info(f'subprocess error: {cpe}')
            sys.exit(1)

        # kill the stream once the emulator is killed
        stream_process = system_platform_mapping[platform]['stream_host'][Prefs['enum_GameStreamHost']]['process']

        while emu_proc.poll() is None:
            pass
        if emu_proc.poll() is not None:
            logging.debug('emulator subprocess is complete')
            for proc in psutil.process_iter():
                if proc.name().lower() == stream_process.lower():
                    logging.debug('stream_process match found, attempting to end stream process')
                    proc.kill()
                    break

        return


def launch_adb(moonlight_pc_uuid, moonlight_app_id):
    # https://stackoverflow.com/a/37327094/11214013

    # stop and restart the adb server
    adb.server_kill()
    time.sleep(3)
    adb.__init__(socket_timeout=10)

    adb_ranges = [
        [5557, 5585],  # Android version < 11 Others
        [30000, 39999],  # https://www.reddit.com/r/tasker/comments/jbzeg5/adb_wifi_and_android_11_wireless_debugging/
        [40000, 49999],
        [50000, 59999],
        [60000, 65535]
    ]

    device = None

    # try port 5555 first
    adb_address = adb_connect(5555)
    if adb_address:
        device = adb.device(serial=adb_address)
    else:
        for adb_range in adb_ranges:
            if not adb_connected:
                adb_threaded_scan(adb_range)

        count = 0
        while count < 90:
            if adb_connected:
                device = adb.device(serial=adb_connected)
                break
            time.sleep(1)
            count += 1

    if not device:
        logging.error('no adb device found, exiting')
        sys.exit(1)

    # packages dictionary
    packages = {
        'Moonlight': {
            'package': 'com.limelight'
        }
    }

    for package in packages:
        if packages[package]['package'] in device.list_packages():
            packages[package]['installed'] = True
            logging.info(f'{package} is installed on client device: {packages[package]["package"]}')
        else:
            packages[package]['installed'] = False
            logging.info(f'{package} is NOT installed on client device: {packages[package]["package"]}')

    # add -W for more silent starting https://developer.android.com/studio/command-line/adb
    # why did -W stop working after a server reboot?
    if packages[Prefs['enum_GameStreamApp']]['installed']:
        # stop playback in plex
        device.keyevent(key_code=86)
        # https://developer.android.com/reference/android/view/KeyEvent#KEYCODE_MEDIA_STOP

        # open moonlight on client device streaming from server desktop
        shell_commands = [
            'am', 'start', '-W', '-n', 'com.limelight/com.limelight.ShortcutTrampoline',
            '--es', '"UUID"', f'"{moonlight_pc_uuid}"',
            '--es', '"AppId"', f'"{moonlight_app_id}"'
        ]

        status = device.shell(shell_commands)
        logging.debug(f'command status: {status}')

        if 'status: ok' in status.lower():
            return True
        else:
            return False
    else:
        return False


def adb_connect(adb_port):
    adb_address = f'{client_ip}:{adb_port}'
    logging.debug(f'attempting connection on: {adb_address}')
    try:
        adb.connect(addr=adb_address, timeout=10)
    except AdbTimeout as e:
        logging.warning(f'{e}: {adb_address}')

    device = adb.device(serial=adb_address)
    try:
        state = device.get_state()
    except AdbError as e:
        logging.warning(f'{e}: {adb_address}')
    else:
        logging.debug(f'device state: {state}')

        if state == 'device':
            logging.info(f'adb connected on port: {adb_port}')
            return adb_address
        else:
            adb.disconnect(addr=adb_address)  # disconnect if connection not successful
            return False

    return False


def adb_threaded_scan(port_range):
    # number of threads, feel free to tune this parameter as you wish
    range_threads = port_range[-1] - port_range[0]
    logging.info(f'range_threads: {range_threads}')
    pref_threads = Prefs['int_PortScanThreads']
    logging.info(f'pref_threads: {pref_threads}')
    if range_threads < pref_threads:
        n_threads = range_threads
    else:
        n_threads = pref_threads

    for t in range(n_threads):
        try:
            # for each thread, start it
            t = Thread(target=port_scan_thread)
            # when we set daemon to true, that thread will end when the main thread ends
            t.daemon = True
            # start the daemon thread
            t.start()
        except RuntimeError as e:
            logging.error(e)
            break

    for port in range(port_range[0], port_range[-1]):
        if (port % 2) != 0:  # if port is an odd number
            # for each port, put that port into the queue
            # to start scanning
            q.put(port)


def port_scan(port):  # determine whether `host` has the `port` open
    # creates a new socket
    s = socket.socket()

    try:
        # tries to connect to host using that port
        s.connect((client_ip, port))
        # make timeout if you want it a little faster ( less accuracy )
        s.settimeout(0.3)
    except ConnectionRefusedError:
        # cannot connect, port is closed
        pass
    except TimeoutError:
        # cannot connect, port is closed
        pass
    else:
        # the connection was established, port is open!
        logging.debug(f'found open port: {port}')

        connected = adb_connect(port)
        if connected:
            global adb_connected
            adb_connected = connected
            logging.debug(f'connected adb port: {adb_connected}')

    finally:
        s.close()


def port_scan_thread():
    while True:
        port = q.get()  # get the port number from the queue
        port_scan(port=port)  # scan that port number
        q.task_done()  # tells the queue that the scanning for that port is done


def launch_ios():
    # listing and launching of installed apps seems to be possible with this library https://github.com/postlund/pyatv
    # no device available to setup and test with so returning False for now
    # PRs are welcome or send me a test device :D
    return False


def launch_windows(moonlight_pc_uuid, moonlight_app_name, secrets):
    u = secrets[client_user]['win']['u']
    p = secrets[client_user]['win']['p']

    command_list = [
        ['schtasks', '/create', '/TN', r'\RetroArcher launcher', '/s', client_ip, '/sc', 'onlogon', '/tr',
         rf'C:\Program Files\Moonlight Game Streaming\Moonlight.exe stream {moonlight_pc_uuid} {moonlight_app_name}',
         '/f',
         '/u', u, '/p', p],
        ['schtasks', '/run', '/TN', r'\RetroArcher launcher', '/s', client_ip, '/u', u, '/p', p],
        ['schtasks', '/delete', '/TN', r'\RetroArcher launcher', '/s', client_ip, '/u', u, '/p', p, '/f']
    ]

    for command_args in command_list:
        try:
            proc = subprocess.run(command_args, check=True)
        except subprocess.CalledProcessError as cpe:
            # error handling
            logging.info(f'subprocess error: {cpe}')
            sys.exit(1)

    return True


def launch_xbox():
    console_info = XboxDiscovery().discover(addr=client_ip, server_port=int(Prefs['int_XboxAuthRedirectPort']))[0]

    try:
        if console_info['address'] == client_ip:
            logging.info(f'Found matching Xbox: {console_info["name"]}')
            console_liveid = console_info['liveid']
        else:
            return False
    except KeyError:
        return False

    launch_status = xbox_main(console_liveid=console_liveid, launch_client=True)

    return launch_status


def list_hash(file_list):
    logging.debug(f'file_list: {file_list}')

    buffer_size = Prefs['int_BufferSize']

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    md5_list = []
    sha1_list = []

    for x in file_list:
        with open(x, 'rb') as f:
            while True:
                data = f.read(buffer_size)
                if not data:
                    break
                md5.update(data)
                sha1.update(data)
        md5_list.append(md5.hexdigest())
        sha1_list.append(sha1.hexdigest())

    return sorted(md5_list), sorted(sha1_list)


def list_videos(directory):
    video_extensions = ['.mp4', '.mkv']
    video_list = []
    if os.path.exists(directory):
        for file in os.listdir(directory):
            for extension in video_extensions:
                if file.endswith(extension):
                    video_list.append(os.path.join(directory, file))
    return video_list


def make_dir(directory):
    try:
        os.mkdir(directory, mode=0o777)
    except:
        pass


def copy_file(src, dst):
    try:
        shutil.copy2(src, dst)
    except:
        pass


def make_video(src, dst, rom_name):
    font_folder = paths['retroarcherFontDir']
    font_file = os.path.join(font_folder, 'OpenSans', 'OpenSans-Light.ttf')

    # ffmpeg formatting for font files is a little bit weird
    # https://stackoverflow.com/a/57512653/11214013
    font_file = font_file.replace('\\', '/').replace(':', '\\\\:')

    illegal_characters = [',']

    title = rom_name
    current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    if os.path.isfile(dst):
        os.remove(dst)  # remove destination if it exists already
    for character in illegal_characters:
        rom_name = rom_name.replace(character, f'\\{character}')

    if sys.platform == 'win32':
        ff_executable = os.path.join(paths['retroarcherFFMPEGDir'], 'ffmpeg')
    else:
        ff_executable = 'ffmpeg'

    ff = FFmpeg(
        executable=ff_executable,
        inputs={src: ['-ss', '0']},
        outputs={dst: [
            '-t', ffmpeg_overlay['videoLength'], '-vf',

            f"drawtext=text='{rom_name}': fontfile='{font_file}': fontcolor={ffmpeg_overlay['fontColor']}: \
            fontsize={ffmpeg_overlay['fontSize']}: box={ffmpeg_overlay['border']}: \
            boxcolor={ffmpeg_overlay['borderColor']}: boxborderw={ffmpeg_overlay['borderSize']}: \
            x={ffmpeg_overlay['fontX']}: y={ffmpeg_overlay['fontY']}",

            '-codec:v', Prefs['enum_FfmpegEncoder'], '-codec:a', 'copy', '-map_metadata', '-1', '-metadata',
            f'title={title}', '-metadata', f'creation_time={current_time}', '-map_chapters', '-1'
            ]
        }
    )
    logging.debug(ff.cmd)
    ffmpeg_proc = ff.run()

    # os.symlink(src[0], dst) #symlinks not picked up by Plex :( ... hence the workaround with ffmpeg
    '''
    try:
        os.link(src, dst) #Plex sucks with hardlinks all pointing to the same file :(
    except FileExistsError:
        print('FileExistsError')
        os.remove(dst)
        make_video(src, dst)
    except OSError as e:
        print('OSError' + str(e))
        if str(e).startswith('[WinError 1142] An attempt was made to create more links on a file than the file system supports:'):
            print(src)
            os.remove(src)
            #fix src[1] if we end up making hardlinks again
            os.system('copy "' + src[1] +'" "' +src + '"') #we will not link to a new file (although with the same name) according to this https://unix.stackexchange.com/a/50188, explains why when we delete the original source the links still work
            make_video(src, dst)
    '''


def platform_path(full_path):
    dir_length = len(split_all(full_path))
    dir_path = os.path.dirname(full_path)
    dir_name = os.path.basename(dir_path)

    game_platform = None

    counter = 0
    while counter < dir_length:
        for platform_key, platform_value in archer_dict.dPlatformMapping.items():

            if dir_name == platform_key:
                counter = dir_length
                game_platform = dir_name
                break
        dir_path = os.path.dirname(dir_path)
        dir_name = os.path.basename(dir_path)
        counter += 1

    if game_platform:
        return game_platform


def scanner(path_dict):
    logging.info(f'path_dict: {path_dict}')
    logging.info(f'source_rom_dir: {source_rom_dir}')
    logging.info(f'data_folders: {data_folders}')

    video_extensions = ['.mp4', '.mkv']
    multi_disk_search = ['(cd', '(disk', '(disc', '(part', '(pt', '(prt']  # used to determine if rom is part of group
    source_rom_dir_length = len(split_all(source_rom_dir))

    start_video_directory = os.path.join(path_dict['retroarcherStartVideosDir'])  # map to start video directory
    main_video_directory = os.path.join(start_video_directory, 'Main')  # map the main videos directory

    # compare these later
    main_video_list = list_videos(main_video_directory)
    logging.info(f'main_video_list: {main_video_list}')
    main_md5_list, main_sha1_list = list_hash(main_video_list)
    logging.info(f'main_md5_list: {main_md5_list}')
    logging.info(f'main_sha1_list: {main_sha1_list}')

    if Prefs['bool_FfmpegTextBox'].lower() == 'true':
        border = str(1)
    else:
        border = str(0)

    global ffmpeg_overlay
    # compare this to existing settings later
    ffmpeg_overlay = {
        'videoLength': str(Prefs['int_FfmpegLength']),
        'fontSize': str(Prefs['int_FfmpegTextSize']),
        'fontColor': Prefs['str_FfmpegTextColor'],
        'fontX': Prefs['str_FfmpegTextX'],
        'fontY': Prefs['str_FfmpegTextY'],
        'border': border,
        'borderColor': Prefs['str_FfmpegTextBoxColor'],
        'borderSize': Prefs['str_FfmpegTextBoxBorder']
    }

    '''get the existing json file'''
    # create data folders
    json_dir = data_folders['dbFolder']
    media_dir = data_folders['mediaFolder']
    make_dir(json_dir)
    make_dir(media_dir)

    # try to read the existing json_file
    json_file = os.path.join(json_dir, 'database.json')
    try:
        with open(json_file) as f:
            database = json.load(f)
        use_existing = True
    except:
        use_existing = False

    ffmpeg_changed = 0
    if use_existing:
        try:
            if ffmpeg_overlay == database['ffmpegOverlay']:
                logging.info('ffmpeg_overlay settings did not change')
                ffmpeg_changed = 0  # no changes
            else:
                database['ffmpegOverlay'] = ffmpeg_overlay
                logging.info('ffmpeg_overlay settings changed, re-encoding everything')
                ffmpeg_changed = 1  # settings changed, re-encode ALL
        except KeyError as key_error:
            use_existing = False
            logging.error(f'KeyError: {key_error}')
            logging.error('database corruption detected... database will be re-created')
        if main_md5_list == database['mainVideoHash']:
            logging.info('main videos are the same as before')
            main_videos = 0  # don't use a new video
        else:
            database['mainVideoHash'] = main_md5_list
            logging.info('main videos have changed')
            main_videos = 1  # possibly use a new video

    if not use_existing:
        logging.debug(f'use existing: {use_existing}')
        database = {
            'ffmpeg_overlay': ffmpeg_overlay
        }
        ffmpeg_changed = 1  # this forces re-encoding of everything
        database['mainVideoHash'] = main_md5_list
        main_videos = 1  # possibly use a new video
        database['romMapping'] = {}
        database['romMapping']['platforms'] = {}

    for root, directories, files in os.walk(source_rom_dir):  # https://stackoverflow.com/a/35703223
        for d in directories:
            if root == source_rom_dir:
                for platform_key, platform_value in archer_dict.dPlatformMapping.items():
                    # https://stackoverflow.com/a/51446563

                    system_name_counter = 0
                    while system_name_counter < len(platform_value['systemNames']):

                        if d.lower() == platform_value['systemNames'][system_name_counter].lower():
                            system = platform_key
                            logging.info(f'system: {system}')

                            try:
                                # this is a string not bool... lowercase the system name, and the value
                                get_system = Prefs[f'scanner_{system.replace(" ", "_").lower()}'].lower()
                                logging.info(f'get_system for {system}: {get_system}')
                            except KeyError:
                                get_system = ''  # In case user has folder that is not supported by RetroArcher yet
                                logging.info(f'System ({system}) is not supported yet.')

                            if get_system == 'true':
                                # probably pre-mature until we know if a rom was found, but this should be faster
                                platform_video_directory = os.path.join(start_video_directory, 'Platforms', system)

                                platform_video_list = list_videos(platform_video_directory)
                                platform_md5_list, platform_sha1_list = list_hash(platform_video_list)

                                try:
                                    database['romMapping']['platforms'][system]
                                except KeyError:
                                    database['romMapping']['platforms'][system] = {}
                                try:
                                    database['romMapping']['platforms'][system]['platformVideoHash']
                                except KeyError:
                                    database['romMapping']['platforms'][system]['platformVideoHash'] = {}
                                if platform_md5_list != database['romMapping']['platforms'][system][
                                    'platformVideoHash']:
                                    database['romMapping']['platforms'][system]['platformVideoHash'] = platform_md5_list
                                    platform_videos = 1  # possibly use a new platform video
                                else:
                                    platform_videos = 0  # don't use a new platform video

                                checks = [platform_value['romExtensions']]
                                if platform_value['multiDisk']:
                                    if 'm3u' not in checks:
                                        checks.append(['m3u'])

                                library_type = platform_value['libraryType']
                                lib_path = os.path.join(data_folders['mediaFolder'], library_type)
                                make_dir(lib_path)
                                logging.info(f'lib_path: {lib_path}')
                                dst_path = os.path.join(data_folders['mediaFolder'], library_type, system)
                                make_dir(dst_path)
                                logging.info(f'dst_path: {dst_path}')

                                multi_disk_game_list = {}
                                keys_to_delete = []

                                for root1, directories1, files1 in os.walk(os.path.join(root, d)):
                                    relative_path = os.path.join(*split_all(root1)[source_rom_dir_length:])
                                    # https://blog.finxter.com/python-join-list-as-path/

                                    iteration = 0
                                    for check in checks:
                                        for f in files1:
                                            split_file = f.rsplit('.', 1)
                                            rom_extension = split_file[-1].lower()

                                            # standard method
                                            rom_name = split_file[0]

                                            # custom system game naming conventions
                                            if system.lower() == 'sony playstation 3':
                                                # rpcs3... loads a specific file from a specific sub directory

                                                ps3_path = os.path.join('ps3_game', 'usrdir')
                                                if ps3_path in root1.lower():
                                                    if f.lower() == 'eboot.bin':
                                                        game_folder = \
                                                            os.path.split(os.path.join(*split_all(relative_path)[:-2]))[
                                                                -1]

                                                        rom_name = game_folder.rsplit(' ', 1)[0]
                                                        # title id separates game name... no brackets?

                                                    else:
                                                        continue
                                                else:
                                                    continue
                                            elif system.lower() == 'nintendo wii u':
                                                # cemu... need folder name
                                                y = 0
                                                while y < len(check):
                                                    if rom_extension == check[y].lower() and rom_extension == 'rpx':
                                                        game_folder = \
                                                            os.path.split(os.path.join(*split_all(relative_path)[:-1]))[
                                                                -1]
                                                        rom_name = game_folder.rsplit(' [', 1)[0]

                                                    elif rom_extension == check[y].lower() and rom_extension == 'wud':
                                                        game_folder = \
                                                            os.path.split(os.path.join(*split_all(relative_path)))[-1]
                                                        rom_name = game_folder.rsplit(' [', 1)[0]

                                                    y += 1

                                            # figure out which video to use
                                            src = None
                                            is_game = False
                                            skip_rom = False

                                            y = 0
                                            # while y < len(value['romExtensions']):
                                            while y < len(check):
                                                if rom_extension == check[y].lower():
                                                    make_link = False

                                                    if any(mds in rom_name.lower() for mds in multi_disk_search):
                                                        # https://stackoverflow.com/a/3389611

                                                        for mds in multi_disk_search:
                                                            if mds in rom_name.lower():
                                                                # this sets variable mds
                                                                break

                                                        if platform_value['multiDisk']:
                                                            index0 = rom_name.lower().find(mds)
                                                            temp = rom_name[index0:]

                                                            index1 = temp.lower().find(')')

                                                            game_name = f'{rom_name[0:index0].rstrip()} {temp[index1 + 1:].strip()}'.strip()
                                                            logging.info(f'game_name: {game_name}')

                                                            try:
                                                                multi_disk_game_list[game_name]
                                                            except KeyError:
                                                                matched = 0
                                                                for title in multi_disk_game_list:
                                                                    logging.debug(f'MultiDisk game title: {title}')
                                                                    split_existing = title.split('(')
                                                                    split_game = game_name.split('(')

                                                                    length_game = len(split_game)

                                                                    temp_existing = title.rsplit('(', 1)[0].strip()
                                                                    temp_game = game_name.rsplit('(', 1)[0].strip()

                                                                    if temp_existing == temp_game and length_game > 2:
                                                                        # these are the same
                                                                        keys_to_delete.append(title)

                                                                        game_name = temp_game
                                                                        multi_disk_game_list[game_name] = \
                                                                            multi_disk_game_list[title]
                                                                        multi_disk_game_list[game_name][
                                                                            len(multi_disk_game_list[game_name])] = f
                                                                        matched = 1
                                                                        time.sleep(2)
                                                                        break

                                                                if matched == 0:
                                                                    multi_disk_game_list[game_name] = {
                                                                        0: f
                                                                    }
                                                                    logging.info(
                                                                        f'MultiDisk game being added to the list: {f}')
                                                            else:
                                                                multi_disk_game_list[game_name][
                                                                    len(multi_disk_game_list[game_name])] = f
                                                                logging.info(f'MultiDisk game already in list: {f}')

                                                            skip_rom = True
                                                        else:
                                                            is_game = True
                                                    else:
                                                        is_game = True

                                                    if is_game and not skip_rom:
                                                        # try to find a game specific start video
                                                        for extension in video_extensions:
                                                            temp_file = os.path.join(start_video_directory, 'Games',
                                                                                     system, f'{rom_name}{extension}')
                                                            if os.path.isfile(temp_file):
                                                                src = temp_file
                                                                video_type = 'game'

                                                                video_hash, junk = list_hash([src])
                                                                try:
                                                                    if video_hash[0] == database['romMapping'][
                                                                            'platforms'][system]['videos'][
                                                                            f'{rom_name}{extension}']['videoHash']:
                                                                        logging.debug(
                                                                            f'videoHash is equal hash in database: {video_hash[0]}')
                                                                        make_link = False
                                                                    else:
                                                                        logging.debug(
                                                                            f'videoHash is not equal hash in database: {video_hash[0]}')
                                                                        make_link = True
                                                                except KeyError:
                                                                    make_link = True
                                                                break

                                                        # try to find a find a random platform start video
                                                        # then try to find a random non platform start video
                                                        if src is None:
                                                            start_vid_dir = [
                                                                platform_video_directory,
                                                                main_video_directory
                                                            ]

                                                            video_type = ['platform', 'main']
                                                            type_hash_list = [platform_md5_list, main_md5_list]
                                                            type_make_new = [platform_videos, main_videos]
                                                            t = 0
                                                            for video_dir in start_vid_dir:
                                                                video_list = list_videos(video_dir)
                                                                if len(video_list) > 0:
                                                                    src = os.path.join(video_dir,
                                                                                       random.choice(video_list))
                                                                    video_type = video_type[t]

                                                                    found = 0
                                                                    for extension in video_extensions:
                                                                        try:
                                                                            old_hash = \
                                                                                database['romMapping']['platforms'][
                                                                                    system]['videos'][
                                                                                    f'{rom_name}{extension}'][
                                                                                    'videoHash']
                                                                            if type_make_new[t] == 1 and old_hash in \
                                                                                    type_hash_list[t]:
                                                                                make_link = random.choice([True, False])
                                                                            else:
                                                                                make_link = False
                                                                        except KeyError:
                                                                            pass
                                                                        try:
                                                                            if video_type != database['romMapping'][
                                                                                    'platforms'][system]['videos'][
                                                                                    f'{rom_name}{extension}'][
                                                                                    'videoType']:

                                                                                logging.info(
                                                                                    'video type has changed')
                                                                                make_link = True
                                                                                found = 1
                                                                                break
                                                                            else:
                                                                                logging.info(
                                                                                    'video type has not changed')
                                                                                found = 1
                                                                                break
                                                                        except KeyError:
                                                                            logging.info('video type not found')

                                                                    if found == 0:
                                                                        make_link = True

                                                                    video_hash, junk = list_hash([src])

                                                                    break
                                                                t += 1

                                                    if ffmpeg_changed == 1:
                                                        make_link = True

                                                    if make_link and not skip_rom:
                                                        destination_path = os.path.join(library_type, system,
                                                                                        f'{rom_name}.{src.rsplit(".", 1)[-1]}')

                                                        video_key = os.path.join(f'{rom_name}.{src.rsplit(".", 1)[-1]}')

                                                        try:
                                                            database['romMapping']['platforms'][system]['videos']
                                                        except KeyError:
                                                            database['romMapping']['platforms'][system]['videos'] = {}
                                                        try:
                                                            database['romMapping']['platforms'][system]['videos'][
                                                                video_key]
                                                        except KeyError:
                                                            database['romMapping']['platforms'][system]['videos'][
                                                                video_key] = {}

                                                        database['romMapping']['platforms'][system]['videos'][
                                                            video_key]['romFolder'] = relative_path
                                                        database['romMapping']['platforms'][system]['videos'][
                                                            video_key]['romFile'] = f
                                                        database['romMapping']['platforms'][system]['videos'][
                                                            video_key]['videoType'] = video_type
                                                        database['romMapping']['platforms'][system]['videos'][
                                                            video_key]['videoHash'] = video_hash[0]
                                                        # just a single item, so don't need whole list

                                                        # write database file
                                                        json_file = os.path.join(json_dir, 'database.json')
                                                        with open(json_file, 'w') as database_file:
                                                            json.dump(database, database_file)

                                                        dst = os.path.join(data_folders['mediaFolder'],
                                                                           destination_path)

                                                        make_video(src, dst, rom_name)

                                                    elif skip_rom:
                                                        logging.info(f'Skipping MultiDisk game image: {f}')
                                                    elif not make_link:
                                                        logging.info(f'No update needed for this rom: {f}')
                                                y += 1
                                        if iteration == 0:
                                            # makes m3u files
                                            # generates ffmpeg videos
                                            for game, rom_file in multi_disk_game_list.items():
                                                make_m3u = 1

                                                rom_name = game

                                                for titles in keys_to_delete:
                                                    if titles == game:
                                                        make_m3u = 0
                                                        break

                                                if make_m3u == 1:
                                                    f = f'{rom_name}.m3u'
                                                    file_contents = ''

                                                    m3u_path = os.path.join(root, d, f)
                                                    for disk, contents in rom_file.items():
                                                        disk_number = disk
                                                        file_contents += f'{contents}\n'

                                                    # write the m3u
                                                    if file_contents != '':
                                                        with open(m3u_path, 'w', encoding='utf-8') as m3u_file:
                                                            # https://stackoverflow.com/a/35086151/11214013
                                                            m3u_file.write(file_contents)

                                        iteration += 1

                            elif get_system == 'false':
                                logging.info(f'Skipping disabled system: {system}')
                            elif get_system == '':
                                logging.info(f'Skipping system not found in agent settings: {system}')
                            else:
                                logging.error(f'Skipping system for unknown reason: {system}')

                            break

                        system_name_counter += 1

    for platform_key in database['romMapping']['platforms']:
        # to do
        # add some stuff here to remove video files that the rom doesn't exist anymore
        pass


def split_all(path):  # https://www.oreilly.com/library/view/python-cookbook/0596001673/ch04s16.html
    all_parts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            all_parts.insert(0, parts[0])
            break
        elif parts[1] == path:  # sentinel for relative paths
            all_parts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            all_parts.insert(0, parts[1])
    return all_parts


def xbox_main(console_liveid=None, launch_client=None):
    app = web.Application()
    app.add_routes([web.get("/auth/callback", auth_callback)])
    runner = web.AppRunner(app)

    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, "localhost", int(Prefs['int_XboxAuthRedirectPort']))
    loop.run_until_complete(site.start())
    xbl_client = loop.run_until_complete(
        xbox_async_main(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, TOKENS_FILE, console_liveid, launch_client)
    )

    return xbl_client


async def xbox_async_main(client_id: str, client_secret: str, redirect_uri: str, token_filepath: str,
                          console_liveid=None, launch_client=False):
    async with ClientSession() as session:
        auth_mgr = AuthenticationManager(session, client_id, client_secret, redirect_uri)

        # Refresh tokens if we have them
        if os.path.exists(token_filepath):
            with open(token_filepath, mode="r") as f:
                tokens = f.read()
            auth_mgr.oauth = OAuth2TokenResponse.parse_raw(tokens)
            await auth_mgr.refresh_tokens()

        # Request new ones if they are not valid
        if not (auth_mgr.xsts_token and auth_mgr.xsts_token.is_valid()):
            auth_url = auth_mgr.generate_authorization_url()
            webbrowser.open(auth_url)
            code = await queue.get()
            await auth_mgr.request_tokens(code)

        with open(token_filepath, mode="w") as f:
            f.write(auth_mgr.oauth.json())

        xbl_client = XboxLiveClient(auth_mgr)

        if launch_client:
            consoles = await xbl_client.smartglass.get_console_list(True)
            if consoles.status.error_code.lower() != 'ok':
                logging.error(f'xbox console status error: {consoles.status.error_message}')
                sys.exit(1)

            for console in consoles.result:
                if console.id != console_liveid:
                    continue

                logging.info('Found matching xbox on account')

                console_status = await xbl_client.smartglass.get_console_status(console.id)

                # get list of installed apps
                installed_apps = await xbl_client.smartglass.get_installed_apps(console.id)

                moonlight_installed = False
                # plex_installed = False
                for app in installed_apps.result:
                    if app.name.lower() == 'moonlight uwp':
                        moonlight_installed = True
                        one_store_product_id = app.one_store_product_id
                        break

                # launch moonlight
                if moonlight_installed:
                    # press B button, stop the video
                    button = InputKeyType('B')
                    await xbl_client.smartglass.press_button(console.id, button)

                    await xbl_client.smartglass.launch_app(console.id, one_store_product_id)
                    return True
                else:
                    logging.error('Moonlight is not installed on xbox.')
                    logging.error('Moonlight purchase/install link: https://www.microsoft.com/store/apps/9MW1BS08ZBTH')
                    return False

            logging.error('no suitable xbox console found')
            return False

        else:
            return xbl_client


if __name__ == '__main__':
    logDir = os.path.join(os.path.expanduser('~'), 'RetroArcher')
    make_dir(logDir)
    logFile = os.path.join(logDir, 'retroarcher.log')

    logging.basicConfig(filename=logFile, level=logging.DEBUG, format='%(asctime)s :  %(levelname)s - %(message)s')

    logging.info('----retroarcher.py script started----')

    paths = get_paths()  # get the paths
    logging.info(f'paths: {paths}')

    # hack for cleaner folder structure and relative imports
    sys.path.append(paths['scriptDir'])
    sys.path.append(paths['retroarcherModulesDir'])
    sys.path.append(paths['codeDir'])

    # agent imports
    import archer_dict

    # module imports (user doesn't need to install)
    import psutil
    import requests
    import xmltodict

    # from module imports
    from adbutils import adb  # https://github.com/openatx/adbutils
    from adbutils.errors import AdbError, AdbTimeout
    from ffmpy import FFmpeg  # ffmpeg wrapper

    from aiohttp import ClientSession, web  # xbox client
    from xbox.webapi.api.client import XboxLiveClient
    from xbox.webapi.api.provider.smartglass.models import (InputKeyType)
    from xbox.webapi.authentication.manager import AuthenticationManager
    from xbox.webapi.authentication.models import OAuth2TokenResponse
    from xbox.webapi.scripts import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, TOKENS_FILE

    # local imports
    from XboxDiscovery import XboxDiscovery

    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(1)

    # argparse
    parser = argparse.ArgumentParser(
        description="Script to stream desktop to Android using Moonlight and then launches emulator and rom on PC.",
        formatter_class=argparse.RawTextHelpFormatter)

    # arguments for launcher
    parser.add_argument('--launch', action='store_true', required=False, help='Launch the rom from Tautulli.')
    parser.add_argument('--ip_address', type=str, nargs='?', required=False, default='',
                        help='IP address of client device.')
    parser.add_argument('--stream_local', type=str, nargs='?', required=False, default='', help='1 if stream is local')
    parser.add_argument('--platform', type=str, nargs='?', required=False, default='',
                        help='Platform type passed in from Tautulli. Example: Android')
    parser.add_argument('--device', type=str, nargs='?', required=False, default='',
                        help='Device type passed in from Tautulli.')
    parser.add_argument('--product', type=str, nargs='?', required=False, default='',
                        help='Product type passed in from Tautulli.')
    parser.add_argument('--player', type=str, nargs='?', required=False, default='',
                        help='Player type passed in from Tautulli.')
    parser.add_argument('--file', type=str, nargs='?', required=False, default='',
                        help='Full file path passed in from Tautulli.')  # need to parse the filename and match it in the json file to the matching rom file
    parser.add_argument('--user', type=str, nargs='?', required=False, default='',
                        help='Plex User passed in from Tautulli.')
    parser.add_argument('--user_id', type=str, nargs='?', required=False, default='',
                        help='Plex UserID passed in from Tautulli.')

    # arguments for scanner
    parser.add_argument('--scan', action='store_true', required=False,
                        help='Scan the library, update media, and rom mapping.')

    # arguments for xbox auth
    parser.add_argument('--xbox_auth', action='store_true', required=False,
                        help='Obtain token for xbox or renew token.')

    # arguments for updating requirements
    parser.add_argument('--update', action='store_true', required=False, help='To do.')  # to do

    # testing args from tautulli
    parser.add_argument('--username', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--user_email', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--user_thumb', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--initial_stream', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--stream_location', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--machine_id', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--media_type', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--title', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--library_name', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--year', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--release_date', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--updated_date', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--last_viewed_date', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--studio', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--content_rating', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--directors', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--writers', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--actors', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--genres', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--labels', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--collections', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--summary', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--tagline', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--rating', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--critic_rating', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--audience_rating', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--user_rating', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--duration', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--poster_url', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--plex_id', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--plex_url', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--filename', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--file_size', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--section_id', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--rating_key', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--art', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--thumb', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--poster_thumb', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--poster_title', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--indexes', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--remaining_time', type=str, nargs='?', required=False, default='', help='Dev')

    # --user {user} --username {username} --user_email {user_email} --user_thumb {user_thumb} --device {device} --platform {platform} --product {product} --player {player} --initial_stream {initial_stream} --ip_address {ip_address} --remaining_time {remaining_time} --stream_local {stream_local} --stream_location {stream_location} --user_id {user_id} --machine_id {machine_id} --media_type {media_type} --title {title} --library_name {library_name} --year {year} --release_date {release_date} --updated_date {updated_date} --last_viewed_date {last_viewed_date} --studio {studio} --content_rating {content_rating} --directors {directors} --writers {writers} --actors {actors} --genres {genres} --labels {labels} --collections {collections} --summary {summary} --tagline {tagline} --rating {rating} --critic_rating {critic_rating} --audience_rating {audience_rating} --user_rating {user_rating} --duration {duration} --poster_url {poster_url} --plex_id {plex_id} --plex_url {plex_url} --file {file} --filename {filename} --file_size {file_size} --section_id {section_id} --rating_key {rating_key} --art {art} --thumb {thumb} --poster_thumb {poster_thumb} --poster_title {poster_title} --indexes {indexes} --remote_access_mapping_state {remote_access_mapping_state} --remote_access_mapping_error {remote_access_mapping_error} --remote_access_public_address {remote_access_public_address} --remote_access_public_port {remote_access_public_port} --remote_access_private_address {remote_access_private_address} --remote_access_private_port {remote_access_private_port} --update_platform {update_platform}

    opts = parser.parse_args()

    # bool arguments... switches
    scan = opts.scan
    launch = opts.launch
    update = opts.update
    xbox_auth = opts.xbox_auth

    # get the plugin identifier from Plex
    infoFile = os.path.join(os.path.abspath(paths['contentsDir']), 'Info.plist')
    # print(infoFile)
    info = convert_xml_to_json(infoFile)
    # print(json.dumps(info, indent=4))

    agent = 'com.github.agents.retroarcher.retroarcher'

    plist_counter = 0
    try:
        for plist_key in info['plist']['dict']['key']:  # get the agent name
            if plist_key == 'CFBundleIdentifier':
                agent = info['plist']['dict']['string'][plist_counter]
                break
            plist_counter += 1
    except KeyError:
        pass

    # settings from agent
    settings_file = get_settings(paths['plexDir'], agent)
    settings = convert_xml_to_json(settings_file)

    try:
        settings['PluginPreferences']
    except KeyError:
        settings = {'PluginPreferences': {}}

    Prefs = {}
    for prefs_key, prefs_value in archer_dict.dDefaultSettings.items():
        try:
            Prefs[prefs_key] = settings['PluginPreferences'][prefs_key]
        except KeyError:
            Prefs[prefs_key] = prefs_value
        if not Prefs[prefs_key]:
            Prefs[prefs_key] = prefs_value
        settingSplit = prefs_key.split('_', 1)
        if settingSplit[0] == 'enum':
            try:
                Prefs[prefs_key] = archer_dict.dict_enum_settings_map[settingSplit[-1]][Prefs[prefs_key]]
            except KeyError:
                pass
        elif settingSplit[0] == 'int':
            Prefs[prefs_key] = int(Prefs[prefs_key])
        elif settingSplit[0] == 'list':
            Prefs[prefs_key] = Prefs[prefs_key].split(',')
        elif settingSplit[0] == 'dir':
            if os.path.isdir(Prefs[prefs_key]):
                pass
            else:
                Prefs[prefs_key] = None
                logging.warning(f'{prefs_key} directory does not exist: {prefs_value}')

    # emulator and core settings... not in dDefaultSettings
    for prefs_key, prefs_value in settings['PluginPreferences'].items():
        keySplit = prefs_key.split('_')
        if keySplit[0] == 'emulator' or keySplit[0] == 'core':
            try:
                if not prefs_value:
                    Prefs[prefs_key] = 0
                else:
                    Prefs[prefs_key] = int(prefs_value)
            except KeyError:
                Prefs[prefs_key] = 0
            except TypeError:  # probably won't ever have this scenario
                Prefs[prefs_key] = 0

    if launch or scan:
        if not Prefs['dir_SourceRomDirectory']:
            logging.critical('Source Rom Directory is not set in agent settings.')
            sys.exit(1)
        source_rom_dir = os.path.abspath(Prefs['dir_SourceRomDirectory'])

    '''get data folders'''
    data_folders = get_data_folders(directory=paths['plexDir'], plugin=agent)
    logging.info(f'data_folders: {data_folders}')

    '''script arguments'''
    if not launch:
        if scan:
            scanner(paths)

        if xbox_auth:
            xbox_main()

    elif launch:
        # string arguments
        client_platform = opts.platform  # from tautulli (Android or Firefox for example)
        logging.info(f'client_platform: {client_platform}')
        client_ip = opts.ip_address  # from tautulli
        logging.info(f'client_ip: {client_ip}')
        client_device = opts.device  # from tautulli (Windows for example)
        logging.info(f'client_device: {client_device}')
        client_product = opts.product  # from tautulli (PlexWeb for example)
        logging.info(f'client_product: {client_product}')
        client_player = opts.player  # from tautulli (Firefox for example)
        logging.info(f'client_player: {client_player}')
        client_user = opts.user  # from tautulli (Firefox for example)
        logging.info(f'client_user: {client_user}')
        client_user_id = opts.user_id
        logging.info(f'client_user_id: {client_user_id}')
        client_user_name = opts.username
        logging.info(f'client_user_name: {client_user_name}')
        movie_name = opts.file  # from tautulli
        logging.info(f'movie_name: {movie_name}')
        stream_local = opts.stream_local  # from tautulli
        logging.info(f'stream_local: {stream_local}')

        if stream_local:
            launcher()
        else:
            logging.error('Client appears to be a remote client.')
            logging.error('RetroArcher cannot execute scripts on a remote client yet.')
            logging.error('Try using "http://x.x.x.x:32400/web" instead of "https://app.plex.tv"')
            sys.exit(1)
