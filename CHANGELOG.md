# Changelog

## [1.2.0 - 2022-01-14]
### Added
- (Clients) Added Xbox One/One X + Series S/X as clients (Experimental) - Closes [#2](https://github.com/RetroArcher/RetroArcher.bundle/issues/2)
- (Repository) Added PR checks
- (Repository) Added automated build and release actions
- (Releases) Added Linux release (Development Only)
- (Releases) Added Mac release (Development Only)
### Changed
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
