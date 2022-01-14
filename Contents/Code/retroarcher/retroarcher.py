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


def config_to_dict(configFile):
    def splitter(line):
        return line.split('=', 1)

    with open(configFile, 'r') as f:
        text = f.read().rstrip('\n')
        header, *data_lines = text.split('\n')

    data = dict(map(splitter, data_lines))

    return header, data


def config_rewrite(configFile, header, data):
    with open(configFile, 'w') as f:
        data_lines = list(map('='.join, data.items()))
        text = '\n'.join([header] + data_lines)
        f.write(text)


def convertXMLtoJSON(filepath):
    try:
        inputFile = open(filepath, 'rb')
        j = xmltodict.parse(inputFile)
    except FileNotFoundError:
        j = {}

    return j


def get_ip():  # https://stackoverflow.com/a/28950776/11214013
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def getJson_fromXML(url):
    headers = {
        'Accept': 'application/xml'
    }

    xml = requests.get(url=url, headers=headers).text

    result = xmltodict.parse(xml)

    return result


def getPaths():
    # build_directories
    paths = {}
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
    for key in paths_to_get:
        if key == 0:
            paths['script'] = script
        else:
            path = os.path.dirname(paths[paths_to_get[key - 1]])
            paths[paths_to_get[key]] = path

    paths['agentModulesDir'] = os.path.join(paths['contentsDir'], 'Libraries', 'Shared')
    paths['retroarcherModulesDir'] = os.path.join(paths['contentsDir'], 'Libraries', 'Modules')
    paths['retroarcherStartVideosDir'] = os.path.join(paths['contentsDir'], 'Resources', 'StartVideos')
    paths['retroarcherFontDir'] = os.path.join(paths['contentsDir'], 'Resources', 'Fonts')
    paths['retroarcherFFMPEGDir'] = os.path.join(paths['contentsDir'], 'Resources', 'ffmpeg')

    logging.debug('Paths: %s' % (paths))
    return paths


def getSettings(directory, agent):
    settingsFile = os.path.join(directory, 'Plug-in Support', 'Preferences', agent + str('.xml'))
    return settingsFile


def getDataFolders(directory, agent):
    dataFolders = {}
    dataFolders['dataFolder'] = os.path.join(directory, 'Plug-in Support', 'Data', agent)
    dataFolders['mediaFolder'] = os.path.join(directory, 'Plug-in Support', 'Data', agent, 'media')
    dataFolders['dbFolder'] = os.path.join(directory, 'Plug-in Support', 'Data', agent, 'database')
    return dataFolders


def launcher(clientIP, clientPlatform, clientDevice, clientProduct, clientPlayer, clientUser, clientUserId,
             clientUserName, movieName, dataFolders):
    if Prefs['str_MoonlightPcUuid'] == '' or Prefs['str_MoonlightPcUuid'] == None:
        serverInfo = getJson_fromXML(Prefs['url_GameStreamServerAddress'])
        logging.debug('serverInfo: %s' % (json.dumps(serverInfo, indent=4)))
        moonlightPcUuid = serverInfo['root']['uniqueid']
    else:
        moonlightPcUuid = Prefs['str_MoonlightPcUuid']
    logging.info('moonlightPcUuid: %s' % (moonlightPcUuid))

    moonlightAppName = Prefs['str_MoonlightAppName']

    if Prefs['str_MoonlightAppId'] == '' or Prefs['str_MoonlightAppId'] == None:
        logging.info('GameStreamHost: %s' % (Prefs['enum_GameStreamHost']))
        if Prefs['enum_GameStreamHost'] == 'GeForce Experience':
            nvstreamsvc_path = os.path.join(os.path.expandvars('$programdata'), 'NVIDIA Corporation', 'nvstreamsvc')

            nvsstreamsvrLogs = ['nvstreamsvcCurrent.log', 'nvstreamsvcOld.log']

            appIdFound = False
            for log in nvsstreamsvrLogs:
                if appIdFound == False:
                    NVlogFile = os.path.join(nvstreamsvc_path, log)
                    if os.path.isfile(NVlogFile):
                        with open(NVlogFile, 'r') as f:
                            logContents = f.read()
                        # find titles
                        titleSplit = logContents.split('Title=')
                        titleCounter = 0

                        while titleCounter < len(titleSplit):
                            if titleSplit[titleCounter].splitlines()[0].lower() == moonlightAppName.lower():
                                moonlightAppId = titleSplit[titleCounter].split('AppId=', 1)[-1].splitlines()[0]
                                appIdFound = True
                                break
                            titleCounter += 1

        else:
            moonlightAppId = '1'

    else:
        moonlightAppId = Prefs['str_MoonlightAppId']
    logging.info('moonlightAppId: %s' % (moonlightAppId))

    # convert movieName to romName
    game_name_full = os.path.basename(movieName)  # the file name
    system = platformPath(movieName)

    # key = os.path.join(system, game_name_full)
    videoKey = game_name_full
    logging.info('videoKey: %s' % (videoKey))

    jsonDir = dataFolders['dbFolder']
    jsonFile = os.path.join(jsonDir, 'database.json')
    with open(jsonFile) as f:
        database = json.load(f)

    secretsFile = os.path.join(jsonDir, 'secrets.json')
    try:
        with open(secretsFile) as f:
            secrets = json.load(f)
    except FileNotFoundError:
        pass

    romFolder = database['romMapping']['platforms'][system]['videos'][videoKey]['romFolder']
    romFile = database['romMapping']['platforms'][system]['videos'][videoKey]['romFile']

    romName = os.path.join(romFolder, romFile)

    logging.info('romName: %s' % (romName))

    systemKey = system.lower().replace(' ', '_')

    emulator = archer_dict.dPlatformMapping[system]['emulators'][Prefs['emulator_' + systemKey]]
    logging.debug('emulator: %s' % (emulator))

    applicationDirectory = Prefs['dir_app_' + emulator]
    binaryCommand = Prefs['str_binary_' + emulator]

    if emulator == 'retroarch':
        core = archer_dict.dPlatformMapping[system]['emulators'][emulator]['cores'][Prefs['core_' + systemKey]]
        logging.info('core: %s' % (core))
        emulatorCore = os.path.join('cores', core)
        logging.info('emulatorCore: %s' % (emulatorCore))
    else:
        emulatorCore = ''

    fullRomPath = os.path.join(SourceRomDir, romName)
    logging.info('fullRomPath: %s' % (fullRomPath))

    logging.info('clientPlatform: %s' % (clientPlatform))

    launch = False
    if clientPlatform.lower() == 'android':
        launch = launchADB(clientIP, moonlightPcUuid, moonlightAppId)
    elif clientProduct.lower() == 'plex for windows' and clientPlatform.lower() == 'windows':
        launch = launchWindows(clientIP, moonlightPcUuid, moonlightAppName, clientUser, secrets)
    elif clientProduct.lower() == 'plex web' and clientDevice.lower() == 'windows':
        launch = launchWindows(clientIP, moonlightPcUuid, moonlightAppName, clientUser, secrets)
    elif clientPlatform.lower() == 'xbox':
        launch = launchXbox(clientIP)
    elif clientPlatform.lower() == 'ios':  # disable for now
        launch = False
    else:
        launch = False

    if launch == True:
        UserId_rpcs3 = clientUserId
        UserId_cemu = UserId_rpcs3
        UserId_length = len(UserId_rpcs3)
        try:
            int(clientUserId)
            while UserId_length != 8:
                if UserId_length < 8:
                    UserId_rpcs3 = '0%s' % (UserId_rpcs3)
                else:
                    UserId_rpcs3 = UserId_rpcs3[1:]
                UserId_cemu = str(int(UserId_rpcs3) + 80000000)
                UserId_length = len(UserId_rpcs3)
        except:
            logging.error('User ID is not an integer: %s' % (clientUserId))

        dSystemPlatformMapping = {
            'win64': {
                'emulators': {
                    'cemu': {
                        'dir': applicationDirectory,
                        'command': 'start "RetroArcher" "%s" --fullscreen --game "%s" --account %s' % (
                            binaryCommand, fullRomPath, UserId_cemu)
                    },
                    'retroarch': {
                        'dir': applicationDirectory,
                        'command': 'start "RetroArcher" "%s" -L "%s" "%s"' % (binaryCommand, emulatorCore, fullRomPath)
                    },
                    'rpcs3': {
                        'dir': applicationDirectory,
                        'command': 'start "RetroArcher" "%s" --no-gui "%s" --user-id %s' % (
                            binaryCommand, fullRomPath, UserId_rpcs3)
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
                },
                'kill_command': 'taskkill /F /IM'
            },
            'win32': {
                'emulators': {
                    'cemu': {
                        'dir': applicationDirectory,
                        'command': 'start "RetroArcher" "%s" --fullscreen --game "%s" --account %s' % (
                            binaryCommand, fullRomPath, UserId_cemu)
                    },
                    'retroarch': {
                        'dir': applicationDirectory,
                        'command': 'start "RetroArcher" "%s" -L "%s" "%s"' % (binaryCommand, emulatorCore, fullRomPath)
                    },
                    'rpcs3': {
                        'dir': applicationDirectory,
                        'command': 'start "RetroArcher" "%s" --no-gui "%s" --user-id %s' % (
                            binaryCommand, fullRomPath, UserId_rpcs3)
                    }
                },
                'stream_host': {
                    'GeForce Experience': {
                        'process': 'nvstreamer.exe',
                    },
                    'Open-Stream': {
                        'process': 'openstream.exe'
                    },
                    'Sunshine': {
                        'process': 'sunshine.exe'
                    }
                },
                'kill_command': 'taskkill /f /im'
            }
            # 'linux' : 'tbd',
            # 'macOS' : 'tbd'
        }

        if sys.platform == 'win32':  # if windows determine if 32 bit or 64 bit
            import struct
            architecture = struct.calcsize("P") * 8  # https://stackoverflow.com/a/1406849
            if architecture == 64:
                platform = 'win64'
            elif architecture == 32:
                platform = 'win32'
        logging.info('architecture: %s' % (architecture))
        logging.info('platform: %s' % (platform))

        emulatorPath = dSystemPlatformMapping[platform]['emulators'][emulator]['dir']
        logging.info('emulatorPath: %s' % (emulatorPath))
        os.chdir(emulatorPath)

        # verify/create user profile folder and file for cemu
        if emulator == 'cemu':
            userProfilePath_cemu = os.path.join(emulatorPath, 'mlc01', 'usr', 'save', 'system', 'act', UserId_cemu)
            userProfileFile_cemu = os.path.join(userProfilePath_cemu, 'account.dat')

            userProfilePathExists_cemu = os.path.isdir(userProfilePath_cemu)
            userProfileFileExists_cemu = os.path.isfile(userProfileFile_cemu)

            if userProfilePathExists_cemu == False or userProfileFileExists_cemu == False:  # we need to create the user profile
                default_cemu_account_file = os.path.join(emulatorPath, 'mlc01', 'usr', 'save', 'system', 'act',
                                                         '80000001', 'account.dat')
                if os.path.isfile(default_cemu_account_file) == True:
                    make_dir(userProfilePath_cemu)
                    copy_file(default_cemu_account_file, userProfileFile_cemu)
                else:
                    logging.critial('Failed to copy default cemu user profile. Exiting.')
                    sys.exit()

            # rewrite the account file everytime (so user never needs to delete the file when we make changes/improvements
            userProfileFileExists_cemu = os.path.isfile(userProfileFile_cemu)
            if userProfileFileExists_cemu == True:
                # need to parse and replace some stuff in the file
                header, data = config_to_dict(userProfileFile_cemu)

                data['PersistentId'] = UserId_cemu
                if data[
                    'Uuid'] == 'e9df01108a453a2c90e94adc35c9528a':  # this is the default Uuid value... if equal to this, then change it, otherwise leave it alone
                    data['Uuid'] = str(uuid.uuid1()).replace('-', '')
                data['TransferableIdBase'] = '2000004%s' % (data['Uuid'][-8:])

                mii_name_max_length = 10
                x = 0
                data['MiiName'] = ''
                data['MiiData'] = '010001100000cc6f030034330100010001000100010001000100'
                while x < mii_name_max_length:
                    try:
                        data['MiiName'] += '00'
                        data['MiiName'] += clientUserName[x].encode('utf-8').hex()

                        data['MiiData'] += '00'
                        data['MiiData'] += clientUserName[x].encode('utf-8').hex()
                    except IndexError:
                        data['MiiName'] += '0000'
                        data['MiiData'] += '0100'
                    x += 1
                data['MiiName'] += '0000'
                data['MiiData'] += '0100%s' % (
                    '010001000100010001000106010001000100010001000100010001000100010001000100010001000100010001000100')

                config_rewrite(userProfileFile_cemu, header, data)

        command = dSystemPlatformMapping[platform]['emulators'][emulator]['command']
        logging.debug('command: %s' % (command))
        os.system(command)

        # kill the stream once the emulator is killed
        '''
        #this is trying to kill streamer process before it's even started... we need to run after retroarch.exe exits
        process = dSystemPlatformMapping[platform]['stream_host'][gamestreamhost]['process']
        print(process)
        command = '%s %s' % (dSystemPlatformMapping[platform]['kill_command'], process)
        print(command)
        print(os.system(command))
        '''

        '''
        import psutil
        for proc in psutil.process_iter():
            if proc.name == process:
                p = psutil.Process(proc.pid)
                proc.kill()
        '''


def launchADB(clientIP, moonlightPcUuid, moonlightAppId):
    # https://stackoverflow.com/a/37327094/11214013

    global scannerIP
    scannerIP = clientIP

    adbRanges = [[5555, 5585], [30000,
                                50000]]  # https://www.reddit.com/r/tasker/comments/jbzeg5/adb_wifi_and_android_11_wireless_debugging/
    for adbRange in adbRanges:
        adbThreadedScan(adbRange)
        logging.info('adbPortsFound: %s' % (adbPortsFound))
        adbAddress = adbConnect(clientIP, adbPortsFound)
        logging.info('adbAddress: %s' % (adbAddress))
        if adbAddress != None:
            device = adb.device(serial=adbAddress)
            break

    # possible apps that can be useful
    packages = {
        'Moonlight': {
            'package': 'com.limelight'
        }
    }

    for key in packages:
        if device.shell('pm list packages | grep ' + packages[key]['package']) != '':
            packages[key]['installed'] = True
            logging.info('%s is installed on client device: %s' % (key, packages[key]['package']))
        else:
            packages[key]['installed'] = False
            logging.info('%s is NOT installed on client device: %s' % (key, packages[key]['package']))
            # try:
            #    if packages[key][1] != '':
            #        installAPK(packages[key]['download'])
            # except:
            #    pass
            # maybe we want to auto install some apks?

    # add -W for more silent starting https://developer.android.com/studio/command-line/adb
    # why did -W stop working after a server reboot?
    if packages[Prefs['enum_GameStreamApp']]['installed'] == True:
        device.shell(
            'am start -W -n com.limelight/com.limelight.ShortcutTrampoline --es "UUID" "' + moonlightPcUuid + '" --es "AppId" "' + str(
                moonlightAppId) + '"')  # open moonlight on client device streaming to server desktop
        return True
    else:
        return False


def adbConnect(clientIP, adbPortsFound):
    for adbPort in adbPortsFound:
        adbAddress = clientIP + ':' + str(adbPort)
        adbConnectOutput = adb.connect(adbAddress)
        logging.debug('adbConnectOutput: %s' % (adbConnectOutput))
        message = adbConnectOutput.split(clientIP + ':' + str(adbPort), 1)[0].strip()
        if message == 'cannot connect to':
            logging.debug('adb connection unsuccessful, trying next port if available')
        elif message == 'failed to connect to':
            logging.debug(
                'adb connection failed, device is probably not paired... Android 11+ ???, trying next available port anyway')
        elif message == 'connected to' or message == 'already connected to':
            logging.info('adb connected on port: %s' % (adbPort))
            return adbAddress
        else:
            logging.debug('unknown connection status, trying next available port')


def adbThreadedScan(adbRange):
    from threading import Thread
    from queue import Queue

    # number of threads, feel free to tune this parameter as you wish
    rangeThreads = adbRange[-1] - adbRange[0]
    logging.info('rangeThreads: %s' % (rangeThreads))
    prefThreads = Prefs['int_PortScanThreads']
    logging.info('prefThreads: %s' % (prefThreads))
    if rangeThreads < prefThreads:
        N_THREADS = rangeThreads
    else:
        N_THREADS = prefThreads
    # thread queue
    global q
    q = Queue()

    global adbPortsFound
    adbPortsFound = []
    for t in range(N_THREADS):
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

    for port in range(adbRange[0], adbRange[-1]):
        if (port % 2) != 0:  # if port is an odd number
            # for each port, put that port into the queue
            # to start scanning
            q.put(port)

            # if port_scan(clientIP, port):
            #    print('port is open: ' + str(port))
            #    adbPortsFound.append(port)
    q.join()  # wait for all ports to finish being scanned


def port_scan(host, port):  # determine whether `host` has the `port` open
    try:
        # creates a new socket
        s = socket.socket()
        # tries to connect to host using that port
        s.connect((host, port))
        # make timeout if you want it a little faster ( less accuracy )
        # s.settimeout(0.2)
    except:
        # cannot connect, port is closed
        # return false
        pass
    else:
        # the connection was established, port is open!
        # return True
        adbPortsFound.append(port)
    finally:
        s.close()


def port_scan_thread():
    while True:
        # get the port number from the queue
        port = q.get()
        # scan that port number
        port_scan(scannerIP, port)
        # tells the queue that the scanning for that port 
        # is done
        q.task_done()


def launchWindows(clientIP, moonlightPcUuid, moonlightAppName, clientUser, secrets):
    u = secrets[clientUser]['win']['u']
    p = secrets[clientUser]['win']['p']

    command_list = [
        ['schtasks', '/create', '/TN', '\RetroArcher launcher', '/s', clientIP, '/sc', 'onlogon', '/tr',
         f'C:\Program Files\Moonlight Game Streaming\Moonlight.exe stream {moonlightPcUuid} {moonlightAppName}', '/f',
         '/u', u, '/p', p],
        ['schtasks', '/run', '/TN', '\RetroArcher launcher', '/s', clientIP, '/u', u, '/p', p],
        ['schtasks', '/delete', '/TN', '\RetroArcher launcher', '/s', clientIP, '/u', u, '/p', p, '/f']
    ]

    for command_args in command_list:
        try:
            proc = subprocess.run(command_args, check=True)
        except subprocess.CalledProcessError as cpe:
            # error handling
            logging.info('subprocess error: %s' % (cpe))
            sys.exit(1)

    return True


def launchXbox(clientIP):
    # # first start xbox-rest-server
    # base_url = f"http://localhost:{Prefs['enum_XboxAuthRedirectPort']}"
    #
    # headers = {
    #     'accept': 'application/json'
    # }
    # url = f"{base_url}/device/?addr={clientIP}"
    #
    # proc = subprocess.Popen([sys.executable,
    #                          os.path.join(os.path.dirname(os.path.realpath(__file__)), 'xbox_rest_server.py'),
    #                          '--port', str(Prefs['enum_XboxAuthRedirectPort']),
    #                          ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #
    # # make sure the xbox-rest-server is responding
    # counter = 0
    #
    # while counter < 30:
    #     try:
    #         test_resp = requests.get(url=base_url, headers=headers)
    #         if test_resp.status_code == 200:
    #             break
    #     except:
    #         pass
    #     time.sleep(1)
    #     counter += 1
    #
    # try:
    #     resp = requests.get(url=url, headers=headers)
    # except requests.exceptions.ConnectionError:
    #     logging.debug(proc.communicate())
    #     logging.debug(proc.stdout)
    #     logging.debug(proc.stderr)
    #     return False
    #
    # # kill the xbox-rest-server
    # proc.kill()
    #
    # if resp.status_code != 200:
    #     return False
    #
    # console_info = resp.json()[0]

    console_info = XboxDiscovery().discover(addr=clientIP, server_port=int(Prefs['int_XboxAuthRedirectPort']))[0]

    try:
        if console_info['address'] == clientIP:
            logging.info(f'Found matching Xbox: {console_info["name"]}')
            console_liveid = console_info['liveid']
        else:
            return False
    except KeyError:
        return False

    launch_status = xbox_main(console_liveid=console_liveid, launch_client=True)

    return launch_status


def list_hash(fileList):
    logging.debug('fileList: %s' % (fileList))

    bufferSize = Prefs['int_BufferSize']

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    md5List = []
    sha1List = []

    for x in fileList:
        with open(x, 'rb') as f:
            while True:
                data = f.read(bufferSize)
                if not data:
                    break
                md5.update(data)
                sha1.update(data)
        md5List.append(md5.hexdigest())
        sha1List.append(sha1.hexdigest())

    return sorted(md5List), sorted(sha1List)


def list_videos(directory):
    videoExtensions = ['.mp4', '.mkv']
    list = []
    if os.path.exists(directory):
        for file in os.listdir(directory):
            for extension in videoExtensions:
                if file.endswith(extension):
                    list.append(os.path.join(directory, file))
    return list


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


def make_link(src, dst, system, romName):
    if sys.platform == 'win32':
        ffmpegPath = 'ffmpeg\\ffmpeg'
    else:
        ffmpegPath = 'ffmpeg'
    logging.debug('ffmpegPath: %s' % (ffmpegPath))

    fontFolder = paths['retroarcherFontDir']
    fontFile = os.path.join(fontFolder, 'OpenSans', 'OpenSans-Light.ttf').replace('\\', '\\\\')

    illegal_characters = [',']

    title = romName
    time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    if os.path.isfile(dst) == True:
        os.remove(dst)  # remove destination if it exists already
    for x in illegal_characters:
        romName = romName.replace(x, '\%s' % (x))

    command = "%s -ss 0 -i \"%s\" -t %s -vf \"drawtext=text='%s': fontfile='fonts/%s': fontcolor=%s: fontsize=%s: box=%s: boxcolor=%s: boxborderw=%s: x=%s: y=%s\" -codec:v %s -codec:a copy -map_metadata -1 -metadata title=\"%s\" -metadata creation_time=%s -map_chapters -1 \"%s\"" % (
        ffmpegPath, src, str(Prefs['int_FfmpegLength']), romName, fontFile, Prefs['str_FfmpegTextColor'],
        str(Prefs['int_FfmpegTextSize']), border, Prefs['str_FfmpegTextBoxColor'], Prefs['str_FfmpegTextBoxBorder'],
        Prefs['str_FfmpegTextX'], Prefs['str_FfmpegTextY'], Prefs['enum_FfmpegEncoder'], title, time, dst)
    logging.debug('command: %s' % (command))
    os.system(command)

    # os.symlink(src[0], dst) #symlinks not picked up by Plex :( ... hence the workaround with ffmpeg
    '''
    try:
        os.link(src, dst) #Plex sucks with hardlinks all pointing to the same file :(
    except FileExistsError:
        print('FileExistsError')
        os.remove(dst)
        make_link(src, dst)
    except OSError as e:
        print('OSError' + str(e))
        if str(e).startswith('[WinError 1142] An attempt was made to create more links on a file than the file system supports:'):
            print(src)
            os.remove(src)
            #fix src[1] if we end up making hardlinks again
            os.system('copy "' + src[1] +'" "' +src + '"') #we will not link to a new file (although with the same name) according to this https://unix.stackexchange.com/a/50188, explains why when we delete the original source the links still work
            make_link(src, dst)
    '''


def platformPath(fullpath):
    dirLength = len(splitall(fullpath))
    dirPath = os.path.dirname(fullpath)
    dirName = os.path.basename(dirPath)

    x = 0
    while x < dirLength:
        for key, value in archer_dict.dPlatformMapping.items():

            if dirName == key:
                x = dirLength
                game_platform = dirName
                break
        dirPath = os.path.dirname(dirPath)
        dirName = os.path.basename(dirPath)
        x += 1
    return game_platform


def scanner(paths, SourceRomDir, dataFolders):
    logging.info('paths: %s' % (paths))
    logging.info('SourceRomDir: %s' % (SourceRomDir))
    logging.info('dataFolders: %s' % (dataFolders))

    videoExtensions = ['.mp4', '.mkv']
    multi_disk_search = ['(cd', '(disk', '(disc', '(part', '(pt', '(prt']  # what else do we need in this list?
    SourceRomDirLength = len(splitall(SourceRomDir))

    startVideoDirectory = os.path.join(paths['retroarcherStartVideosDir'])  # map to start video directory
    mainVideoDirectory = os.path.join(startVideoDirectory, 'Main')  # map the main videos directory

    # compare these later
    mainVideoList = list_videos(mainVideoDirectory)
    logging.info('mainVideoList: %s' % (mainVideoList))
    mainMD5List, mainSHA1List = list_hash(mainVideoList)
    logging.info('mainMD5List: %s' % (mainMD5List))
    logging.info('mainSHA1List: %s' % (mainSHA1List))

    '''set these as global'''
    global border

    if Prefs['bool_FfmpegTextBox'].lower() == 'true':
        border = str(1)
    else:
        border = str(0)

    # compare this to existing settings later
    ffmpegOverlay = {
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
    jsonDir = dataFolders['dbFolder']
    mediaDir = dataFolders['mediaFolder']
    make_dir(jsonDir)
    make_dir(mediaDir)

    # try to read the existing jsonFile
    jsonFile = os.path.join(jsonDir, 'database.json')
    try:
        with open(jsonFile) as f:
            database = json.load(f)
        useExisting = True
    except:
        useExisting = False

    if useExisting == True:
        try:
            if ffmpegOverlay == database['ffmpegOverlay']:
                logging.info('ffmpegOverlay settings did not change')
                ffmpeg_changed = 0  # no changes
            else:
                database['ffmpegOverlay'] = ffmpegOverlay
                logging.info('ffmpegOverlay settings changed, re-encoding everything')
                ffmpeg_changed = 1  # settings changed, re-encode ALL
        except KeyError as e:
            logging.error('KeyError: %s' % (str(e)))
            logging.error('database corruption detected... database will be re-created')
            useExisting = False
        if mainMD5List == database['mainVideoHash']:
            logging.info('main videos are the same as before')
            mainVideos = 0  # don't use a new video
        else:
            database['mainVideoHash'] = mainMD5List
            logging.info('main videos have changed')
            mainVideos = 1  # possibly use a new video

    if useExisting == False:  # do not make this an elif statement becuase we may set useExisting to be false in the above if statement!
        print('use existing is false... something wrong with the json file?')
        logging.info('cannot use existing database.json... maybe it does not exist yet... maybe it is corrupted...')
        database = {'ffmpegOverlay': ffmpegOverlay}
        ffmpeg_changed = 1  # settings changed, re-encode ALL, not really but database is messed up, need to re-make everything.
        database['mainVideoHash'] = mainMD5List
        mainVideos = 1  # possibly use a new video
        database['romMapping'] = {}
        database['romMapping']['platforms'] = {}

    for root, directories, files in os.walk(SourceRomDir):  # https://stackoverflow.com/a/35703223
        for d in directories:
            if root == SourceRomDir:
                for key, value in archer_dict.dPlatformMapping.items():  # https://stackoverflow.com/a/51446563
                    # print(value)
                    # print(value['systemNames'])

                    x = 0
                    while x < len(value['systemNames']):

                        if d.lower() == value['systemNames'][x].lower():
                            x = len(value['systemNames'])
                            system = key
                            logging.info('system: %s' % (system))

                            try:
                                getSystem = Prefs['scanner_' + system.replace(' ',
                                                                              '_').lower()].lower()  # this is a string not bool... lowercase the system name, and the value
                                logging.info('getSystem for %s: %s' % (system, getSystem))
                            except KeyError:
                                getSystem = ''  # In case user has folder that is not supported by RetroArcher yet
                                logging.info('System (%s) is not supported yet.' % (system))

                            if getSystem == 'true':
                                # probably pre-mature until we know if a rom was found, but this should be faster... from here to next for loop
                                platformVideoDirectory = os.path.join(startVideoDirectory, 'Platforms', system)

                                platformVideoList = list_videos(platformVideoDirectory)
                                platformMD5List, platformSHA1List = list_hash(platformVideoList)

                                try:
                                    database['romMapping']['platforms'][system]
                                except KeyError:
                                    database['romMapping']['platforms'][system] = {}
                                try:
                                    database['romMapping']['platforms'][system]['platformVideoHash']
                                except KeyError:
                                    database['romMapping']['platforms'][system]['platformVideoHash'] = {}
                                if platformMD5List != database['romMapping']['platforms'][system]['platformVideoHash']:
                                    database['romMapping']['platforms'][system]['platformVideoHash'] = platformMD5List
                                    platformVideos = 1  # possibly use a new platform video
                                else:
                                    platformVideos = 0  # don't use a new platform video
                                # print(database)

                                # rom extensions allowed
                                # print(value['romExtensions'])
                                # print(value['multiDisk'])

                                checks = [value['romExtensions']]
                                if value['multiDisk'] == True:
                                    checks.append(['m3u'])

                                libraryType = value['libraryType']
                                libPath = os.path.join(dataFolders['mediaFolder'], libraryType)
                                make_dir(libPath)
                                logging.info('libPath: %s' % (libPath))
                                dstPath = os.path.join(dataFolders['mediaFolder'], libraryType, system)
                                make_dir(dstPath)
                                logging.info('dstPath: %s' % (dstPath))

                                multi_disk_game_list = {}
                                keys_to_delete = []

                                for root1, directories1, files1 in os.walk(os.path.join(root, d)):
                                    relativePath = os.path.join(*splitall(root1)[
                                                                 SourceRomDirLength:])  # https://blog.finxter.com/python-join-list-as-path/#:~:text=path.join()%20method%20takes%20one%20or%20more%20path%20arguments,to%20unpack%20the%20list%20into%20the%20argument%20list.

                                    iteration = 0
                                    for check in checks:
                                        # if iteration == 1:
                                        #    print('starting m3u files now')
                                        #    time.sleep(2)
                                        # else:
                                        #    print('starting normal roms now')
                                        #    time.sleep(2)
                                        for f in files1:
                                            splitFile = f.rsplit('.', 1)
                                            romExtension = splitFile[-1].lower()
                                            # print(romExtension)

                                            # custom system game naming conventions
                                            if system.lower() == 'sony playstation 3':  # rpcs3... can't they just be normal and load an iso?
                                                ps3Path = os.path.join('ps3_game', 'usrdir')
                                                if ps3Path in root1.lower():
                                                    if f.lower() == 'eboot.bin':
                                                        gameFolder = \
                                                            os.path.split(os.path.join(*splitall(relativePath)[:-2]))[
                                                                -1]
                                                        romName = gameFolder.rsplit(' ', 1)[
                                                            0]  # title id separates game name... no brackets?
                                                        # print(romName)
                                                        # print(f.lower())
                                                    else:
                                                        continue
                                                else:
                                                    continue
                                            elif system.lower() == 'nintendo wii u':  # cemu... need to get the folder name
                                                y = 0
                                                while y < len(check):
                                                    if romExtension == check[y].lower() and romExtension == 'rpx':
                                                        gameFolder = \
                                                            os.path.split(os.path.join(*splitall(relativePath)[:-1]))[
                                                                -1]
                                                        romName = gameFolder.rsplit(' [', 1)[0]
                                                        # print(romName)
                                                        # print(f.lower())
                                                        print(gameFolder)
                                                        print(romName)
                                                    elif romExtension == check[y].lower() and romExtension == 'wud':
                                                        gameFolder = \
                                                            os.path.split(os.path.join(*splitall(relativePath)))[-1]
                                                        romName = gameFolder.rsplit(' [', 1)[0]
                                                        print(gameFolder)
                                                        print(romName)
                                                    y += 1
                                            else:
                                                romName = splitFile[0]

                                            # figure out which video to use
                                            src = None
                                            isGame = False
                                            skipRom = False

                                            y = 0
                                            # while y < len(value['romExtensions']):
                                            while y < len(check):
                                                if romExtension == check[y].lower():
                                                    # print(system + ' true')
                                                    # need to adjust multi disk m3u generation
                                                    if any(mds in romName.lower() for mds in
                                                           multi_disk_search):  # https://stackoverflow.com/a/3389611
                                                        for mds in multi_disk_search:
                                                            if mds in romName.lower():
                                                                # print(mds)
                                                                break

                                                        if value['multiDisk'] == True:
                                                            index0 = romName.lower().find(mds)
                                                            # print(index0)
                                                            temp = romName[index0:]
                                                            # print(romName)
                                                            # print(temp)
                                                            index1 = temp.lower().find(')')
                                                            # print(index1)
                                                            gameName = (romName[0:index0].rstrip() + ' ' + temp[
                                                                                                           index1 + 1:].strip()).strip()  # probably adjust game name
                                                            logging.info('gameName: %s' % (gameName))

                                                            try:
                                                                multi_disk_game_list[gameName]
                                                                multi_disk_game_list[gameName][
                                                                    len(multi_disk_game_list[gameName])] = f
                                                                logging.info('MultiDisk game already in list: %s' % (f))
                                                            except KeyError:
                                                                matched = 0
                                                                for title in multi_disk_game_list:
                                                                    logging.debug('MultiDisk game title: %s' % (title))
                                                                    splitExisting = title.split('(')
                                                                    splitGame = gameName.split('(')

                                                                    lengthExisting = len(splitExisting)
                                                                    lengthGame = len(splitGame)

                                                                    tempExisting = title.rsplit('(', 1)[0].strip()
                                                                    tempGame = gameName.rsplit('(', 1)[0].strip()

                                                                    if tempExisting == tempGame and lengthGame > 2:
                                                                        # print('these are the same?')
                                                                        keys_to_delete.append(title)
                                                                        # print(multi_disk_game_list[title])
                                                                        # print(tempExisting)
                                                                        # print(tempGame)
                                                                        gameName = tempGame
                                                                        multi_disk_game_list[gameName] = \
                                                                            multi_disk_game_list[title]
                                                                        multi_disk_game_list[gameName][
                                                                            len(multi_disk_game_list[gameName])] = f
                                                                        matched = 1
                                                                        time.sleep(2)
                                                                        break

                                                                if matched == 0:
                                                                    multi_disk_game_list[gameName] = {0: f}
                                                                    logging.info(
                                                                        'MultiDisk game being added to the list: %s' % (
                                                                            f))

                                                            skipRom = True
                                                        else:
                                                            isGame = True
                                                    else:
                                                        isGame = True

                                                    if isGame == True and skipRom == False:
                                                        # try to find a game specific start video
                                                        for extension in videoExtensions:
                                                            tempFile = os.path.join(startVideoDirectory, 'Games',
                                                                                    system, romName + extension)
                                                            if os.path.isfile(tempFile):
                                                                src = tempFile
                                                                videoType = 'game'

                                                                videoHash, junk = list_hash([src])
                                                                # print(videoHash[0])
                                                                # print(database['romMapping']['platforms'][system]['videos'][romName + extension]['videoHash'])
                                                                try:
                                                                    if videoHash[0] == \
                                                                            database['romMapping']['platforms'][system][
                                                                                'videos'][romName + extension][
                                                                                'videoHash']:
                                                                        logging.debug(
                                                                            'videoHash is equal hash in database: %s' % (
                                                                                videoHash[0]))
                                                                        makeLink = False
                                                                    else:
                                                                        logging.debug(
                                                                            'videoHash is not equal hash in database: %s' % (
                                                                                videoHash[0]))
                                                                        makeLink = True
                                                                except KeyError:
                                                                    makeLink = True
                                                                break

                                                        # try to find a find a random platform start video, then try to find a random non platform start video
                                                        if src == None:
                                                            startVidDir = [platformVideoDirectory, mainVideoDirectory]
                                                            video_type = ['platform', 'main']
                                                            typeHashList = [platformMD5List, mainMD5List]
                                                            typeMakeNew = [platformVideos, mainVideos]
                                                            t = 0
                                                            for videoDir in startVidDir:
                                                                videoList = list_videos(videoDir)
                                                                if len(videoList) > 0:
                                                                    src = os.path.join(videoDir,
                                                                                       random.choice(videoList))
                                                                    videoType = video_type[t]

                                                                    found = 0
                                                                    for extension in videoExtensions:
                                                                        if found == 0:
                                                                            try:
                                                                                oldHash = \
                                                                                    database['romMapping']['platforms'][
                                                                                        system]['videos'][
                                                                                        romName + extension][
                                                                                        'videoHash']
                                                                                if typeMakeNew[t] == 1 and oldHash in \
                                                                                        typeHashList[t]:
                                                                                    makeLink = random.choice(
                                                                                        [True, False])
                                                                                else:
                                                                                    makeLink = False
                                                                            except KeyError:
                                                                                pass
                                                                            try:
                                                                                if videoType != database['romMapping'][
                                                                                    'platforms'][system]['videos'][
                                                                                    romName + extension]['videoType']:
                                                                                    logging.info(
                                                                                        'video type has changed')
                                                                                    makeLink = True
                                                                                    found = 1
                                                                                else:
                                                                                    logging.info(
                                                                                        'video type has not changed')
                                                                                    found = 1
                                                                            except KeyError:
                                                                                logging.info('video type not found')

                                                                    if found == 0:
                                                                        makeLink = True

                                                                    if makeLink == True:
                                                                        videoHash, junk = list_hash([src])

                                                                    break
                                                                t += 1

                                                    if ffmpeg_changed == 1:
                                                        makeLink = True

                                                    if makeLink == True and skipRom == False:
                                                        destinationPath = os.path.join(libraryType, system,
                                                                                       romName + '.' +
                                                                                       src.rsplit('.', 1)[-1])

                                                        videoKey = os.path.join(romName + '.' + src.rsplit('.', 1)[-1])

                                                        try:
                                                            database['romMapping']['platforms'][system]['videos']
                                                        except KeyError:
                                                            database['romMapping']['platforms'][system]['videos'] = {}
                                                        try:
                                                            database['romMapping']['platforms'][system]['videos'][
                                                                videoKey]
                                                        except KeyError:
                                                            database['romMapping']['platforms'][system]['videos'][
                                                                videoKey] = {}

                                                        database['romMapping']['platforms'][system]['videos'][videoKey][
                                                            'romFolder'] = relativePath
                                                        database['romMapping']['platforms'][system]['videos'][videoKey][
                                                            'romFile'] = f
                                                        database['romMapping']['platforms'][system]['videos'][videoKey][
                                                            'videoType'] = videoType
                                                        database['romMapping']['platforms'][system]['videos'][videoKey][
                                                            'videoHash'] = videoHash[
                                                            0]  # just a single item, so don't need whole list

                                                        # print(database)
                                                        jsonFile = os.path.join(jsonDir, 'database.json')
                                                        with open(jsonFile, 'w') as f:
                                                            json.dump(database, f)

                                                        dst = os.path.join(dataFolders['mediaFolder'], destinationPath)
                                                        # print(dst)

                                                        make_link(src, dst, system, romName)  # enable for testing

                                                    elif skipRom == True:
                                                        logging.info('Skipping MultiDisk game image: %s' % (f))
                                                    elif makeLink == False:
                                                        logging.info('No update needed for this rom: %s' % (f))
                                                y += 1
                                        if iteration == 0:
                                            # multi disk m3u maker AND ffmpeg generator (so we don't have to scan again).
                                            for keyX, valueX in multi_disk_game_list.items():
                                                make_m3u = 1

                                                romName = keyX

                                                for titles in keys_to_delete:
                                                    if titles == keyX:
                                                        make_m3u = 0
                                                        break

                                                if make_m3u == 1:
                                                    f = romName + '.m3u'
                                                    fileContents = ''
                                                    # print(romName)
                                                    m3uPath = os.path.join(root, d, f)
                                                    for keyY, valueY in valueX.items():
                                                        diskNumber = keyY
                                                        fileContents += valueY + '\n'
                                                        # print(diskNumber)
                                                    # print(fileContents)

                                                # write the m3u
                                                if fileContents != '':
                                                    with open(m3uPath, 'w',
                                                              encoding='utf-8') as m3u:  # https://stackoverflow.com/a/35086151/11214013
                                                        m3u.write(fileContents)

                                        iteration += 1

                            elif getSystem == 'false':
                                logging.info('Skipping disabled system: %s' % (system))
                            elif getSystem == '':
                                logging.info('Skipping system not found in agent settings: %s' % (system))
                            else:
                                logging.error('Skipping system for unknown reason: %s' % (system))
                        x += 1

    # print(database)

    # add some stuff here to remove video files that the rom doesn't exist anymore
    for key in database['romMapping']['platforms']:
        pass


def splitall(path):  # https://www.oreilly.com/library/view/python-cookbook/0596001673/ch04s16.html
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path:  # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts


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
                logging.error('xbox console status error: %s' % (consoles.status.error_message))
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
                    # elif app.name.lower() == 'plex':
                    # plex_installed = True

                # launch moonlight
                if moonlight_installed:
                    # press B button, stop the video
                    button = InputKeyType('B')
                    await xbl_client.smartglass.press_button(console.id, button)

                    await xbl_client.smartglass.launch_app(console.id, one_store_product_id)
                    return True
                else:
                    logging.error(
                        'Moonlight is not installed on xbox, install it: https://www.microsoft.com/store/apps/9MW1BS08ZBTH')
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

    paths = getPaths()  # get the paths
    logging.info('paths: %s' % (paths))

    # hack for cleaner folder structure and relative imports
    sys.path.append(paths['scriptDir'])
    sys.path.append(paths['retroarcherModulesDir'])
    sys.path.append(paths['codeDir'])

    # agent imports
    import archer_dict

    # module imports (user doesn't need to install)
    import requests
    import xmltodict

    # from module imports
    from adbutils import adb  # https://github.com/openatx/adbutils

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

    # arguments for automatic update
    parser.add_argument('--update', action='store_true', required=False, help='Update plug-in from github.')

    # testing args from tautulli
    parser.add_argument('--username', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--user_email', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--user_thumb', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--initial_stream', type=str, nargs='?', required=False, default='', help='Dev')
    parser.add_argument('--stream_local', type=str, nargs='?', required=False, default='', help='Dev')
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
    info = convertXMLtoJSON(infoFile)
    # print(json.dumps(info, indent=4))
    x = 0
    for key in info['plist']['dict'][
        'key']:  # get the agent name (maybe useful for if users want to switch and try different branches while keeping original settings)
        if key == 'CFBundleIdentifier':
            agent = info['plist']['dict']['string'][x]
            # print(agent)
            break
        x += 1

    '''settings from agent'''
    # get the agent settings (use it for this script as well)
    settingsFile = getSettings(paths['plexDir'], agent)
    # print(settingsFile)
    settings = convertXMLtoJSON(settingsFile)
    # print('original settings')
    # print(json.dumps(settings, indent=4))

    try:
        settings['PluginPreferences']
    except KeyError:
        settings = {'PluginPreferences': {}}

    Prefs = {}
    for key, value in archer_dict.dDefaultSettings.items():
        try:
            Prefs[key] = settings['PluginPreferences'][key]
        except KeyError as e:
            Prefs[key] = value
        if Prefs[key] == None:
            Prefs[key] = value
        settingSplit = key.split('_', 1)
        if settingSplit[0] == 'enum':
            try:
                Prefs[key] = archer_dict.dict_enum_settings_map[settingSplit[-1]][Prefs[key]]
            except KeyError as e:
                pass
        elif settingSplit[0] == 'int':
            Prefs[key] = int(Prefs[key])
        elif settingSplit[0] == 'list':
            Prefs[key] = Prefs[key].split(',')
        elif settingSplit[0] == 'dir':
            if os.path.isdir(Prefs[key]):
                pass
            else:
                Prefs[key] = None
                # print('%s directory does not exist: %s' % (key, value))
                logging.warning('%s directory does not exist: %s' % (key, value))

    # emulator and core settings... not in dDefaultSettings
    for key, value in settings['PluginPreferences'].items():
        keySplit = key.split('_')
        if keySplit[0] == 'emulator' or keySplit[0] == 'core':
            try:
                if value == None:
                    Prefs[key] = 0
                else:
                    Prefs[key] = int(value)
            except KeyError as e:
                Prefs[key] = 0
            except TypeError as e:  # probably won't ever have this scenario...
                Prefs[key] = 0

    # print('Prefs:')
    # print(json.dumps(Prefs, indent=4))

    if launch or scan:
        if Prefs['dir_SourceRomDirectory'] == None:
            logging.critical('Source Rom Directory does not exist or is not set in agent settings.')
            sys.exit(1)
        SourceRomDir = os.path.abspath(Prefs['dir_SourceRomDirectory'])

    '''get data folders'''
    dataFolders = getDataFolders(paths['plexDir'], agent)
    logging.info('dataFolders: %s' % (dataFolders))

    '''script arguments'''
    if not launch:
        if scan:
            scanner(paths, SourceRomDir, dataFolders)

        if xbox_auth:
            xbox_main()

    elif launch:
        # string agruments
        clientPlatform = opts.platform  # from tautulli (Android or Firefox for example)
        clientIP = opts.ip_address  # from tautulli
        clientDevice = opts.device  # from tautulli (Windows for example)
        clientProduct = opts.product  # from tautulli (PlexWeb for example)
        clientPlayer = opts.player  # from tautulli (Firefox for example)
        clientUser = opts.user  # from tautulli (Firefox for example)
        clientUserId = opts.user_id
        clientUserName = opts.username
        movieName = opts.file  # from tautulli

        # integer arguments
        timeRemaining = opts.remaining_time.split(':')  # from tautulli... why returning 00:00:00 ?
        try:
            countdown = (int(timeRemaining[0]) * 3600) + (int(timeRemaining[1]) * 60) + (
                int(timeRemaining[2]))  # seconds remaining
        except:
            countdown = 0

        serverIP = get_ip()
        logging.info('serverIP: %s' % (serverIP))

        # this is only checking the very first part of the IP... should we check the next 2 as well?
        if serverIP.rsplit('.', 1)[0] == clientIP.rsplit('.', 1)[0]:
            launcher(clientIP, clientPlatform, clientDevice, clientProduct, clientPlayer, clientUser, clientUserId,
                     clientUserName, movieName, dataFolders)
        else:
            logging.error(
                'Client appears to be a remote client. RetroArcher cannot execute scripts on a remote client yet. If the client really is local to the server, try accessing your Plex server at "http://x.x.x.x:32400/web" instead of "https://app.plex.tv"')
            sys.exit(1)
