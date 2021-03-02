### RetroArcher.bundle for Plex Media Server:
Retro Archer is a gaming plug-in for Plex! Read all instructions before running any scripts.

### Prerequisites for server:
 - Tautulli (https://tautulli.com/)
 - Windows
   - One of these 3:
     - GeForce Experience (https://www.nvidia.com/en-us/geforce/geforce-experience/)
	   - Benefits:
	     - More development resources
	   - Cons:
	     - Not open source
	     - Only certain Nvidia GPUs supported
		 - Need to be at server for first app connection
	 - Open-stream [not tested] (https://open-stream.net/)
	   - Benefits:
	     - More GPU's supported than GeForce
	     - CPU encoding instead of GPU encoding possible
		 - Somewhat easy to configure
	   - Cons
		 - Need to be at server for first app connection
	 - Sunshine [not tested] (https://github.com/loki-47-6F-64/sunshine/releases)
	   - Benefits:
	     - Pair through URL
	     - More GPU's supported than GeForce
		 - CPU encoding instead of GPU encoding possible
		 - Multi-platform support
       - Cons:
	     - Difficult to configure
 - Linux
    - Sunshine (https://github.com/loki-47-6F-64/sunshine/releases)
	  - Benefits:
	    - Pair through URL
		- More GPU's supported than GeForce
		- CPU encoding instead of GPU encoding possible
		- Multi-platform support
      - Cons:
	    - Difficult to configure
 - Mac
    - Not available yet. Open-Stream claims they will support Windows, Linux and Mac, but currently only a release for Windows is available. Their project is open source. If you have the skills maybe you can help them get this working on Mac.

### Prerequisites for client:
 - Android:
   - Moonlight (https://github.com/moonlight-stream/moonlight-android)
   - Enable developer mode
     - TV-(https://developer.android.com/training/tv/start/start#run-on-a-real-device) Skip Step 1
     - Phone/Tablet-(https://developer.android.com/studio/debug/dev-options#enable)
   - Android 11+:
     - MacroDroid (https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) - optional
	   - Go to Templates and search for `RetroArcher ADB enabler`, please star the macro.
	   - You'll need to also do the adb hack (instructions are for Windows).
	     - `cd /d <plex data folder location>\Plex Media Server\Plug-ins\RetroArcher.bundle\Contents\Libraries\Modules\adbutils\binaries`
		 - On phone goto developer settings, enable wireless debugging
		 - Select `Wireless debugging` (click the text)
		 - Select `Pair device with pairing code`
		 - `abd pair <ip address & port>` (use the ip and port shown on your phone)
		 - enter your 6 digit code
		 - `adb shell pm grant com.arlosoft.macrodroid android.permission.WRITE_SECURE_SETTINGS`
	 - Tasker can probably do the same as MacroDroid... don't have the instructions yet
	 
  - Windows (currently requires Windows as server):
    - One of these 2:
	  - RetroArcher.client.windows (https://github.com/ReenigneArcher/RetroArcher.client.windows)
	  - Moonlight-qt (https://github.com/moonlight-stream/moonlight-qt/releases)
	    - Install to default location
		- Run this from command promp as admin:
		  `netsh advfirewall firewall set rule group="Remote Scheduled Tasks Management" new enable=Yes`

### Installation:
It is recommended to install the [WebTools plugin](http://forums.plex.tv/discussion/288191/webtools-unsupported-appstore/p1).

Using the Unsupported Appstore from WebTools it is possible
to easily install, update and remove RetroArcher, without having
to go through the hassle of manually downloading, unzipping,
renaming and moving it to the correct directory each time.

After successfully installing WebTools please login and select the
"Unsupported Appstore" Module. There you can add the url manually.

### Manual Installation:
Not recommended, but possible if you know what you are doing.

Windows
1. Download the [zipped bundle](https://github.com/ReenigneArcher/RetroArcher.bundle/archive/master.zip) from github,
2. Extract it,
3. Rename it to **RetroArcher.bundle**,
4. Find the [Plex Media Server data directory](https://support.plex.tv/hc/en-us/articles/202915258-Where-is-the-Plex-Media-Server-data-directory-located)
5. Move the RetroArcher.bundle folder to the Plug-ins directory,
6. Restart plex and test,
7. If necessary change the owner and permissions of the RetroArcher.bundle and
8. Restart plex again.

Ubuntu
1. Download the [zipped bundle](https://github.com/ReenigneArcher/RetroArcher.bundle/archive/master.zip) from github,
2. Extract it,
3. Rename it to **RetroArcher.bundle**,
4. Move to the folder:  `/var/<folder>/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins` where <folder> is "lib" or "snap"
5. Find the group number for user "plex" by command "id plex".
6. "cd" to folder in step 4 and change ownership of RetroArcher.bundle: "sudo chown plex:{gid} RetroArcher.bundle"
7. Run "sudo service plexmediaserver restart".

### Game Stream Server Desktop (https://github.com/moonlight-stream/moonlight-docs/wiki/Setup-Guide#using-moonlight-to-stream-your-entire-desktop)
1. Install Latest GeForce Experience, Open-Stream, or Sunshine
2. If using GeForce Experience:
  a. Log-in
  b. Under Settings/Shield enable GAMESTREAM (note: a monitor must be connected to the Nvidia GPU)
  c. Click "Add"
  d. Browse to C:\windows\system32\mstsc.exe
  e. Click "Edit" and rename to "RetroArcher"
  f. Change the BoxArt if you wish (https://github.com/ReenigneArcher/RetroArcher.database/blob/main/Posters/3-4/RetroArcher/RetroArcher.png).
  g. Open Moonlight on a client app
  h. Long press okay on your server name and select `View Details`, make a note of the `Name` and `UUID`, select `OK`
  i. Select the server and enter the pairing code on your server
  j. Long press ok on the app you created in Step 3-6 and select `View Details`, make a note of the `Name` and `ID`, select `OK`
3. If you have multiple monitors, it would be best to set them to duplicate.

### RetroArcher plug-in
1. Access your Plex server at http://localhost:32400/web/index.html# or however you normally access it and log-in
2. Goto settings/agents
3. On the movies tab select `RetroArcher` and select the gear icon
4. The following settings need to be entered
    - ROMS|Fullpath of source rom directory
    - SCANNER|ADVANCED|FFMPEG|Encoder (h264_nvenc is set as default assuming most users will have an nvidia gpu)
    - LAUNCHER|Moonlight Machine UUID
    - LAUNCHER|Moonlight App ID (`1` unless using GeForce Experience)
    - LAUNCHER|Moonlight App ID (`Desktop` unless using GeForce Experience)
    - GAMESTREAM|GENERAL|White listed users
    - PLEX|Server token
    - Ignore last 3 settings entirely
5. Click Save
6. Disable `Local Media Assets (Movies)`

### Scanning roms
1. Note that valid roms found will have a short video generated.
    - This video will be placed inside the `<plex data folder location>\Plex Media Server\Plug-in Support\Data\com.github.agents.reenignearcher.retroarcher` directory.
    - If your start videos are 1080p and 20 seconds in length, they will take approximately 5-6GB per 1000 files.
      - The length of the video can be adjusted in the plug-in settings within Plex. 20 seconds is enough in my testing for Android clients. For Windows clients a longer amount may be desired.
2. Note that Plex will start collecting meta-data once the videos are added. THe metadata collected can take up a lot of space. Most users will have large rom collections, much larger than a standard movie library. Therefore consider that the metadata folder will grow tremendously. I am recommending a separate large SSD for your Plex Data folder only.
3. Place start videos in `<plex data folder location>\Plex Media Server\Plug-ins\RetroArcher.bundle\Contents\Resources\StartVideos`
    - Games
      - Can contain game specific start videos
	  - There should be a folder named the same as the platform name (Nintendo 64 for example)
	  - Video file name must be the same as the rom name except the extension.
	  - Only a single file is allowed for the game specific start video.
    - Platforms
      - If no game specific start video is found the script will look for platform specific start videos
	  - There should be a folder named the same as the platform name (Nintendo 64 for example)
	  - Video file name is not important
	  - There can be multiple platform specific videos for each platform. The script will choose a random one if multiple are found.
    - Random
      - If no game specific or platform start video is found the script will look for generic start videos
	  - No folders are required in this directory
	  - Video file name is not important
	  - There can be multiple platform specific videos for each platform. The script will choose a random one if multiple are found.
4. Install newest version of python
    - Windows (correct the directory as required)
      - `cd /d <plex data folder location>\Plex Media Server\Plug-ins\RetroArcher.bundle\Contents\Code\retroarcher`
      - `py -3 retroarcher.py -scan`
	  - run this as a scheduled task if you wish or run manually when you add/remove roms
    - Linux (correct the directory as required)
      - `sudo apt update`
	  - `sudo apt install ffmpeg `
      - `cd <plex data folder location>\Plex Media Server\Plug-ins\RetroArcher.bundle\Contents\Code\retroarcher`
      - `python3 retroarcher.py -scan`
	  - set this up as a cron job if you wish or run manually when you add/remove roms

### Create Plex library
- General
  - Library Type: Movies
  - Name: RetroArcher (or whatever you want)
  - Language: English (no other languages tested and probably won't work yet)
- Add folder
  - Single library (preferred):
    - `<plex data folder location>\Plex Media Server\Plug-in Support\Data\com.github.agents.reenignearcher.retroarcher\media`
  - Library per platform:
    - `<plex data folder location>\Plex Media Server\Plug-in Support\Data\com.github.agents.reenignearcher.retroarcher\media\<platform name>`
- Advanced
  - Scanner: Plex Movie Scanner
  - Agent: RetroArcher
  - Visibility: Exclude from home screen (recommended option as games will be shown as movies)
  - Enable Cinema Trailer (disabled)
  - Enable video preview thumbnails (disabled)
  - Collections: Disabled

### Tautulli settings
1. Open Notification Agents in Tautulli (http://localhost:8181/settings#tabs_tabs-notification_agents)
2. Add a new notification agents
    - Configuration
      - Script Folder: `<plex data folder location>\Plex Media Server\Plug-ins\RetroArcher.bundle\Contents\Code\retroarcher`
      - Script File: `.\retroarcher.py`
      - Script Timeout: `0`
      - Description: `RetroArcher`
    - Triggers
      - Playback Start
    - Conditions
      - Preferred:
	    - Library Name is `RetroArcher` (change according to your library name)
	  - Other methods:
	    - Library Name begins with `RetroArcher` (for those of you who want to have different libraries for each platform... RetroArcher - Nintendo 64)
	    - Library Name ends with `RetroArcher` (for those of you who want to have different libraries for each platform... Nintendo 64 - RetroArcher)
    - Arguments
      - Playback Start
	    - `--launch --user {user} --device {device} --platform {platform} --product {product} --player {player} --ip_address {ip_address} --file {file}`

### Moonlight clients
- Each new moonlight client needs to be paired to the server.
- Start a stream from the moonlight client and it will ask you to enter the pairing code on the server.
- For GeForce Experience and Open-Stream you need to enter the pin on the server itself.
- For Sunshine you enter the pin at a URL like so. `http://<serveripaddress>:47989/pin/<pin>`
  - You could theoretically set this address up with something like Nginx proxy manager and a custom domain name so you can enter your pin from any network.
  - Probably as an improvement to RetroArcher a simple website will be added and running on the server that allows you to enter the pin in a tradition web gui.