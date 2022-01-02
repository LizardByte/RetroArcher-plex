# Changelog

## v1.1.2 (2022-01-02)

* Clients:
  * Fix: Use python subprocess to connect to Windows clients 
  * Emulators:
    * Fix: Improve Cemu user profile creation
    * Fix: Default core for Doom Engine updated in `DefaultPrefs.json`
  * Metadata:
    * Add: Rating images in metadata xml file (not shown in clients) 
    * Remove: YouTube URL Service (broken)
  * Preferences:
    * Fix: Preference validation

## v1.1.1 (2021-06-14)

* Clients:
  * Add: Setting to control number of threads during ADB port scan 
  * Fix: Improve ADB port scanning 
* Emulators:
  * Fix: Improve Cemu account.dat file creation

## v1.1.0 (2021-06-13)

* Emulators:
  * Add: Nintendo Wii U platform
  * Add: Cemu emulator support
* Misc:
  * Fix: General code cleanup

## v1.0.2 (2021-06-08)

* Clients:
  * Fix: Do not attempt to launch Moonlight on Android if it's not installed 
* Emulators:
  * Fix: Changed default core for Nintendo Family Computer 
  * Fix: Changed default core for Nintendo Game Boy Advance
  * Fix: Changed default core for Sega Mega Drive
* Logging:
  * Fix: Improve `retroarcher.py` logging 
* Misc:
  * Add: Feature Upvote system (Closes #40)
  * Fix: Updated issue template

## v1.0.1 (2021-06-05)

* Settings:
  * Fix: Enum settings would not use values specified in agent settings

## v1.0.0 (2021-06-04)

* Misc:
  * Initial release
