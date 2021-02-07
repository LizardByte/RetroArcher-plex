### RetroArcher.bundle for Plex Media Server:
Retro Archer is a gaming plug-in for Plex!

### Prerequisites for server:
 - Tautulli (https://tautulli.com/)
 - Windows
    - GeForce Experience (https://www.nvidia.com/en-us/geforce/geforce-experience/)
 - Linux
    - TBD
 - Mac
    - TBD

### Prerequisites for client:
 - Moonlight: (https://github.com/moonlight-stream/moonlight-android)
 - Enable developer mode
    - TV-(https://developer.android.com/training/tv/start/start#run-on-a-real-device)-Skip Step 1
    - Phone/Tablet-(https://developer.android.com/studio/debug/dev-options#enable)

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
4. Move to the folder:  /var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins
5. Find the group number for user "plex" by command "id plex".
6. "cd" to folder in step 4 and change ownership of RetroArcher.bundle: "sudo chown plex:{gid} RetroArcher.bundle"
7. Run "sudo service plexmediaserver restart".

### Moonlight (https://github.com/moonlight-stream/moonlight-docs/wiki/Setup-Guide#using-moonlight-to-stream-your-entire-desktop)
1. Install Latest GeForce Experience and login
2. Under Settings/Shield enable GAMESTREAM (note: a monitor must be connected to the Nvidia GPU)
3. Click "Add"
4. Browse to C:\windows\system32\mstsc.exe
5. Click "Edit" and rename to "RetroArcher" or whatever you want
6. Change the BoxArt if you wish.
7. If you have multiple monitors, it would be best to set them to duplicate.
