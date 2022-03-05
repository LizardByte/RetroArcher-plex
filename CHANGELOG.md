# Changelog

## [1.2.5] - 2022-03-04
### Added
- (Clients) - Stop playback in Plex before launching Moonlight on Android
### Changed
- (Emulators) - Updated accepted extensions for PS2 cores in RetroArch
### Fixed
- (Clients) - Resolved issue where ADB port scanner wouldn't connect in some cases for Android 11+
- (Clients) - Improved speed of ADB port scanner for Android 11+
- (Clients) - Attempt to connect on port 5555 before scanning ports for Android clients
- (Scanner) - Fixed issue where some characters would cause scanner to fail

## [1.2.4] - 2022-02-26
### Fixed
- (Clients) - Resolved issue with outdated ADB binaries (#137)
- (Dependencies) - Fixed issue with package excluding some dependencies

## [1.2.3] - 2022-02-25
### Fixed
- (Dependencies) - Fixed issue with package excluding some dependencies

## [1.2.2] - 2022-01-28
### Changed
- (CI) - Plist file now generated during build time
- (Dependencies) - Bump plexapi to 4.9.1 (custom version for Python 2.7 with Theme support)
- (Scanner) - Fixed issue with ffmpeg binary not being found in some cases
### Removed
- (Resources) - Removed Ubuntu font (not used)

## [1.2.1] - 2022-01-18
### Added
- (Launcher) - Stream process now killed when emulator is closed
### Changed
- (General) - Refactor and clean up `retroarcher.py`
- (Launcher) - Emulator now runs in python subprocess
- (Scanner) - Fixed issue that may cause scanner error when ffmpeg settings changed
- (Scanner) - ffmpeg now runs in subprocess
### Breaking
- (Tautulli) - Notification arguments must be updated

## [1.2.0] - 2022-01-15
### Added
- (Clients) Added Xbox One/One X + Series S/X as clients (Experimental) - Closes [#2](https://github.com/RetroArcher/RetroArcher.bundle/issues/2)
- (Repository) Added PR checks
- (Repository) Added automated build and release actions
- (Releases) Added Linux release (Development Only)
- (Releases) Added Mac release (Development Only)
### Changed
- (Info) Improved info/attribution in agent settings
- (Scanner) Fixed issue with scanning introduced in v1.1.2 - Fixes [#116](https://github.com/RetroArcher/RetroArcher.bundle/issues/116)
### Removed
- (Repository) Removed dependencies, now installed during the build process

## [1.1.2] - 2022-01-02
### Added
- (Metadata) Rating images in metadata xml file (not shown in clients)
### Changed
- (Clients) Use python subprocess to connect to Windows clients
- (Emulators) Improve Cemu user profile creation
- (Emulators) Default core for Doom Engine updated in `DefaultPrefs.json`
- (Settings) Preference validation
### Removed 
- (Metadata) YouTube URL Service (broken)

## [1.1.1] - 2021-06-14
### Added
- (Clients) Setting to control number of threads during ADB port scan
### Changed
- (Clients) Improve ADB port scanning
- (Emulators) Improve Cemu account.dat file creation

## [1.1.0] - 2021-06-13
### Added
- (Emulators) Nintendo Wii U platform
- (Emulators) Cemu emulator support
### Changed
- (Misc.) General code cleanup

## [1.0.2] - 2021-06-08
### Added
- (Misc.) Feature Upvote system (Closes #40)
### Changed
- (Clients) Do not attempt to launch Moonlight on Android if it's not installed
- (Emulators) Changed default core for Nintendo Family Computer
- (Emulators) Changed default core for Nintendo Game Boy Advance
- (Emulators) Changed default core for Sega Mega Drive
- (Logging) Improve `retroarcher.py` logging
- (Misc.) Updated issue template

## [1.0.1] - 2021-06-05
### Changed
- (Settings) Enum settings would not use values specified in agent settings

## [1.0.0] - 2021-06-04
### Added
- (Misc.) Initial release
