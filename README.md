### RetroArcher.bundle for Plex Media Server:
RetroArcher is a gaming plug-in for Plex! Read ALL instructions before running any scripts.

### Prerequisites for server:
 - [Tautulli](https://tautulli.com/)
 - Windows
   - One of these 3:
     - [GeForce Experience](https://www.nvidia.com/en-us/geforce/geforce-experience/)
	   - Benefits:
	     - More development resources
	   - Cons:
	     - Not open source
	     - Only certain Nvidia GPUs supported
		 - Need to physically be at the server for first app connection
	 - [Open-stream](https://open-stream.net/) (not tested yet)
	   - Benefits:
	     - More GPU's supported than GeForce
	     - CPU encoding instead of GPU encoding possible
		 - Somewhat easy to configure
	   - Cons
		 - Need to physically be at the server for first app connection
	 - [Sunshine](https://github.com/loki-47-6F-64/sunshine/releases) (not tested yet)
	   - Benefits:
	     - Pair through URL
		 - Multi-platform support
       - Cons:
	     - Only supports CPU encoding
	     - Difficult to configure
 - Linux (coming soon)
   - [Sunshine](https://github.com/loki-47-6F-64/sunshine/releases)
	 - Benefits:
	   - Pair through URL
	   - Multi-platform support
     - Cons:
	   - Only supports CPU encoding
	   - Difficult to configure
 - Mac
   - Not available yet. Open-Stream claims they will support Windows, Linux and Mac, but currently only a release for Windows is available. Their project is open source. If you have the skills maybe you can help them get this working on Mac.
 - Optional (depending on what games you want to play and how)
   - [RetroArch](https://www.retroarch.com/)
   - [RPCS3](https://rpcs3.net/) - coming soon

### Prerequisites for client:
 - Android:
   - [Moonlight](https://github.com/moonlight-stream/moonlight-android)
   - Enable developer mode
     - TV-(https://developer.android.com/training/tv/start/start#run-on-a-real-device) Skip Step 1
     - Phone/Tablet-(https://developer.android.com/studio/debug/dev-options#enable)
   - Android 11+:
     - [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) (optional)
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
	  - [RetroArcher.client.windows](https://github.com/ReenigneArcher/RetroArcher.client.windows)
	  - [Moonlight-qt](https://github.com/moonlight-stream/moonlight-qt/releases)
	    - Install to default location
		- Run this from command promp as admin:
		  `netsh advfirewall firewall set rule group="Remote Scheduled Tasks Management" new enable=Yes`
    - On the server:
	  - Open this directory `<plex data folder location>\Plex Media Server\Plug-in Support\Data\com.github.agents.reenignearcher.retroarcher\database`
	  - Create a file named `secrets.json` if it doesn't exist. The content of the file is below. This process will be improved later (Issue #54)
```
{
  "Plex Username Here" : {
    "win" : {
	  "u" : "Windows username here",
	  "p" : "Windows password here"
	  },
	"linux" : {
	  "u" : "",
	  "p" : ""
	  },
	"mac" : {
	  "u" : "",
	  "p" : ""
	  }
	}
}
```

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
1. Download the [zipped bundle](https://github.com/ReenigneArcher/RetroArcher.bundle/archive/main.zip) from github,
2. Extract it,
3. Rename it to **RetroArcher.bundle**,
4. Find the [Plex Media Server data directory](https://support.plex.tv/hc/en-us/articles/202915258-Where-is-the-Plex-Media-Server-data-directory-located)
5. Move the RetroArcher.bundle folder to the Plug-ins directory,
6. Restart plex and test,
7. If necessary change the owner and permissions of the RetroArcher.bundle and
8. Restart plex again.

Ubuntu
1. Download the [zipped bundle](https://github.com/ReenigneArcher/RetroArcher.bundle/archive/main.zip) from github,
2. Extract it,
3. Rename it to **RetroArcher.bundle**,
4. Move to the folder:  `/var/<folder>/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins` where <folder> is "lib" or "snap"
5. Find the group number for user "plex" by command "id plex".
6. "cd" to folder in step 4 and change ownership of RetroArcher.bundle: "sudo chown plex:{gid} RetroArcher.bundle"
7. Run "sudo service plexmediaserver restart".

### Game Stream Server Desktop (https://github.com/moonlight-stream/moonlight-docs/wiki/Setup-Guide#using-moonlight-to-stream-your-entire-desktop)
1. Install Latest GeForce Experience, Open-Stream, or Sunshine
2. If using GeForce Experience:
    - Log-in
    - Under Settings/Shield enable GAMESTREAM (note: a monitor must be connected to the Nvidia GPU)
    - Click "Add"
    - Browse to C:\windows\system32\mstsc.exe
    - Click "Edit" and rename to "RetroArcher"
    - Change the BoxArt if you wish (https://github.com/ReenigneArcher/RetroArcher.database/blob/main/Posters/3-4/RetroArcher/RetroArcher.png).
    - Open Moonlight on a client app
    - Long press okay on your server name and select `View Details`, make a note of the `Name` and `UUID`, select `OK`
    - Select the server and enter the pairing code on your server
    - Long press ok on the app you created in Step 3-6 and select `View Details`, make a note of the `Name` and `ID`, select `OK`
3. If you have multiple monitors, it would be best to set them to duplicate.

### RetroArcher plug-in
1. Access your Plex server at http://localhost:32400/web/index.html# or however you normally access it and log-in
2. Goto settings/agents
3. On the movies tab select `RetroArcher` and select the gear icon
4. The following settings need to be entered
    - ROMS|Fullpath of source rom directory
    - SCANNER|ADVANCED|FFMPEG|Encoder (h264_nvenc is set as default assuming most users will have an nvidia gpu)
    - LAUNCHER|Moonlight Machine UUID - (this setting will be removed in the future, but is needed for now - Issue #47)
    - LAUNCHER|Moonlight App ID (`1` unless using GeForce Experience) - (this setting will be removed in the future, but is needed for now - Issue #47)
    - LAUNCHER|Moonlight App Name (`Desktop` unless using GeForce Experience) - (this setting will be removed in the future, but is needed for now - Issue #47)
    - GAMESTREAM|GENERAL|White listed users (not working yet)
    - PLEX|Server token
	- APPLICAITON|DIRECTORY|RetroArch (the directory where your retroarch config, cores, etc. exist)
    - Ignore last 3 settings entirely (these are from the broken youtube service for extras  - Issue #14)
5. Click Save
6. Disable `Local Media Assets (Movies)`

### Scanning roms
1. Note that valid roms found will have a short video generated.
    - This video will be placed inside the `<plex data folder location>\Plex Media Server\Plug-in Support\Data\com.github.agents.reenignearcher.retroarcher` directory.
    - If your start videos are 1080p and 20 seconds in length, they will take approximately 5-6GB per 1000 files.
      - The length of the video can be adjusted in the plug-in settings within Plex. 20 seconds is enough in my testing for Android clients. For Windows clients a longer amount may be desired.
2. Note that Plex will start collecting meta-data once the videos are added. The metadata collected can take up a lot of space. Most users will have large rom collections, much larger than a standard movie library. Therefore consider that the metadata folder will grow tremendously. I am recommending a separate large SSD for your Plex Data folder only.
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
- Notes
  - In the future I will try to automate this with python-plexapi.

### Tautulli settings
1. Open [Notification Agents](http://localhost:8181/settings#tabs_tabs-notification_agents) in Tautulli 
2. Add a new notification agent
    - Configuration
      - Script Folder: `<plex data folder location>\Plex Media Server\Plug-ins\RetroArcher.bundle\Contents\Code\retroarcher`
      - Script File: `.\retroarcher.py`
      - Script Timeout: `0`
      - Description: `RetroArcher`
    - Triggers
      - Playback Start
    - Conditions
      - `File` - `contains` - `com.github.agents.reenignearcher.retroarcher`
    - Arguments
      - Playback Start
	    - `--launch --user {user} --device {device} --platform {platform} --product {product} --player {player} --ip_address {ip_address} --file {file}`
- Notes
  - In the future I will try to automate this with tautulli python api (Issue #48).

### Moonlight clients
- Each new moonlight client needs to be paired to the server.
- Start a stream from the moonlight client and it will ask you to enter the pairing code on the server.
- For GeForce Experience and Open-Stream you need to enter the pin on the server itself.
- For Sunshine you enter the pin at a URL like so. `http://<serveripaddress>:47989/pin/<pin>`
  - You could theoretically set this address up with something like Nginx proxy manager and a custom domain name so you can enter your pin from any network.
  - Probably as an improvement to RetroArcher a simple website will be added and running on the server that allows you to enter the pin in a tradition web gui.

### Additional considerations
- By providing game streaming to other users on your Plex server you are granting them full access to your machine. There is a plan to add a watchdog to the script to ensure that the emulator remains full-screen and if not, then the stream will be killed. This may not be 100% reliable though, so even when this is implemented there could still be a risk. Allow game streaming with your shared users at your own risk.
- By granting the server ADB permission to Android devices or other methods to control your devices, you are accepting huge security risk. With or without gamestreaming enabled, this is a risk. Proceed with caution.
- If you have a large game collection, your Plex data directory may grow significantly in size. It is recommended to have as large as possible of a SSD for use only by your Plex data directory.
- There is no warranty or anyway to revert your Plex data directory. Make a backup if you are concerned about ever restoring it to it's previous state.
- This is Windows only currently. There is a plan to support Linux servers with Desktop GUI's, but more work needs to be done on that front. If you would like to try and run this on Linux, and document what needs to change to get everything working, that could be helpful.
- While the repository is public now, this plug-in is not released yet. Some settings from the plug-in settings page in Plex are not implemented yet. They will all be implemented before the initial release. Additionally, there will be many bugs, issues, etc. Some I am already aware of. Check the open issues before submitting new ones.

### Contributors
- Anyone willing to contribute is always welcome to submit pull requests. You can also reach out on the [Discord](https://discord.gg/d6MpcrbYQs) server.