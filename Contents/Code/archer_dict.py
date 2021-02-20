# -*- coding: utf-8 -*-
#dictionaries
dSiteShortNames1 = {    0: 'igdb',
                        1: 'tgdb',
                        2: 'ss',
                        3: 'lb',
                   }
                   
dSiteShortNames2 = {    'igdb': 0,
                        'tgdb': 1,
                        'ss': 2,
                        'lb': 3,
                   }

dSiteNames2Index = {    'IGDB': 0,
                        'TheGamesDB': 1,
                        'ScreenScraper': 2,
                        'LaunchBox Games Database': 3,
                   }

dRatings = {
    'ESRB' : {
        'igdb' : 1
        },
    'PEGI' : {
        'igdb' : 2
        }
    }

#do something different here... maybe combine with dictionary from igdb
dTHEGAMESDB_rating = {  'EC - Early Childhood' : ['EC', 3],
                        'E - Everyone' : ['E', 6],
                        'E10+ - Everyone 10+' : ['E10+', 10],
                        'T - Teen' : ['T', 13],
                        'M - Mature 17+' : ['M', 17],
                        'AO - Adult Only 18+' : ['AO', 18],
                        'RP - Rating Pending' : ['RP', 18],
                        'Not Rated' : ['NR', 18],
                        '' : ['', 18]
                     }

dDefaultSettings = {
	'sSourceRomDirectory' : '',
	
	'lExcludedTerms' : '[BIOS], Action Replay, Game Genie, Game Saver, GameBooster, GameShark',
    'lIncludeRegions' : '',
    'lExcludeRegions' : '',
    'lIncludeLanguages' : '',
    'lExcludeLanguages' : '',
    'lExcludeTags' : 'Beta, Demo, Kiosk, Proto',
    'eFfmpegEncoder' : 'h264_nvenc',
    'iFfmpegThreads' : '1',
    'iFfmpegLength' : '30',
    'iFfmpegTextSize' : '24',
    'sFfmpegTextColor' : 'white',
    'sFfmpegTextX' : '20',
    'sFfmpegTextY' : '20',
    'sFfmpegTextBox' : 'True',
    'sFfmpegTextBoxColor' : 'black@0.5',
    'sFfmpegTextBoxBorder' : '5',
    'iBufferSize' : '65536',
	
    'sSearchSite' : 'IGDB',
	
    'sMoonlightPcUuid' : '',
    'sMoonlightAppId' : '',
    'sMoonlightAppName' : 'RetroArcher',
	
    'bGameStreamEnabled' : 'False',
    'sGameStreamWhiteList' : '',
    'sGameStreamBlackList' : '',
    'eGameStreamApp' : 'moonlight',
    'eGameStreamHost' : 'Nvidia GeForce Experience',
    'sNvStreamerPath' : 'C:\\Program Files\\NVIDIA Corporation\\NvStreamSrv\\nvstreamer.exe',
    'sSunshinePath' : '',
    'sOpenStreamPath' : '',
	
    'sTwitchClientID' : '',
	'sTwitchClientSecret' : '',
	'sTheGamesDBapikey' : '146a546e4a1e764d50dad39bf3f0129fa1609301b81998a15fb6fd243c5827ae',
    'sRAWGapikey' : 'e4649e88b13b4b2e83c76f5065bd5828',
	'sYouTubeApiKey' : 'AIzaSyCYss6qpH_Ru6XHSiuUTEJU6r5G63IDJ-4',
	
    'ePreferredRatingSystem' : 'ESRB',  
	
    'bPlatformAsCollection' : 'True',
	
    'sThemesSource' : 'RetroArcher.database',
	'iMaxThemes' : '0',
    'sSourceThemeDirectory' : '',
	
    'bGetReviews' : 'True',
	
    'bGetExtraObject' : 'True',
	
    'PLEX_URL' : 'http://localhost:32400',
	'PLEX_TOKEN' : '',
	
    'scanner_nintendo_64' : 'True',
    'scanner_nintendo_gamecube' : 'True',
    'scanner_nintendo_wii' : 'True',
	'scanner_sony_playstation' : 'True',
	
    'emulator_3do_interactive_multiplayer' : 0,
	'emulator_amstrad_cpc' : 0,
	'emulator_arcade' : 0,
	'emulator_atari_2600' : 0,
	'emulator_atari_5200' : 0,
	'emulator_atari_7800' : 0,
	'emulator_atari_jaguar' : 0,
	'emulator_atari_lynx' : 0,  
	'emulator_atari_st' : 0,  
	'emulator_colecovision' : 0,
	'emulator_gce_vectrex' : 0,
	'emulator_magnavox_odyssey_2' : 0,
	'emulator_mattel_intellivision' : 0,
	'emulator_microsoft_dos' : 0,
	'emulator_microsoft_msx' : 0,
	'emulator_microsoft_msx2' : 0,
	'emulator_nintendo_3ds' : 0,
	'emulator_nintendo_64' : 0,
	'emulator_nintendo_ds' : 0,
	'emulator_nintendo_entertainment_system' : 0,
	'emulator_nintendo_family_computer' : 0,
	'emulator_nintendo_game_boy' : 0,
	'emulator_nintendo_game_boy_advance' : 0,
	'emulator_nintendo_game_boy_color' : 0,
	'emulator_nintendo_gamecube' : 0,
	'emulator_nintendo_pokemon_mini' : 0,
	'emulator_nintendo_super_famicom' : 0,
	'emulator_nintendo_virtual_boy' : 0,
	'emulator_sega_sg-1000' : 0,
    'emulator_sony_playstation' : 0,
    'emulator_sony_playstation_2' : 0,
    'emulator_sony_playstation_portable' : 0,
	'emulator_super_nintendo_entertainment_system' : 0,
	'emulator_nintendo_wii' : 0,
	'emulator_wonderswan' : 0,
	'emulator_wonderswan_color' : 0,
	
    'core_3do_interactive_multiplayer' : 0,
	'core_amstrad_cpc' : 0,
	'core_arcade' : 0,
	'core_atari_2600' : 0,
	'core_atari_5200' : 0,
	'core_atari_7800' : 0,
	'core_atari_jaguar' : 0,
	'core_atari_lynx' : 0,
	'core_atari_st' : 0,
	'core_colecovision' : 0,
	'core_gce_vectrex' : 0,
	'core_magnavox_odyssey_2' : 0,
	'core_mattel_intellivision' : 0,
	'core_microsoft_dos' : 0,
	'core_microsoft_msx' : 0,
	'core_microsoft_msx2' : 0,
	'core_nintendo_3ds' : 0,
	'core_nintendo_64' : 0,
	'core_nintendo_ds' : 0,
	'core_nintendo_entertainment_system' : 0,
	'core_nintendo_family_computer' : 0,
	'core_nintendo_game_boy' : 0,
	'core_nintendo_game_boy_advance' : 0,
	'core_nintendo_game_boy_color' : 0,
	'core_nintendo_gamecube' : 0,
	'core_nintendo_pokemon_mini' : 0,
	'core_nintendo_super_famicom' : 0,
	'core_nintendo_virtual_boy' : 0,
	'core_nintendo_wii' : 0,
	'core_sega_sg-1000' : 0,
	'core_sony_playstation' : 0,
	'core_sony_playstation_2' : 0,
	'core_sony_playstation_portable' : 0,
    'core_super_nintendo_entertainment_system' : 0,
	'core_wonderswan' : 0,
	'core_wonderswan_color' : 0,
	
    'bRetroArchCacheClean' : 'True',
	
    'sOgXboxIpAddress' : '',
	'sOgXboxGamePaths' : 'Games',
	'bOgXboxGames' : 'True',
	'sOgXboxAppPaths' :	'Apps, Applications',
	'bOgXboxApps' : 'True',
	'sOgXboxDemoPaths' : 'Demos',
	'bOgXboxDemos' : 'True',
	'sOgXboxPosterSource' : 'RetroArcher-Agent',
	'bOgXboxPosterSync' : 'True',
	'sHelpPlatform' : 'none',
	'bHelpSendLinks' : 'True',
	'bHelpIncludeLibretro' : 'True',
	'bHelpIncludeGameManual' : 'True',
	'bHelpIncludeGameMaps' : 'True',
	'bResetSettings' : 'False',
	'bResetFactory' : 'False',
	'bAutoInstallApk' : 'False',
	'bAutoUpdateApk' : 'False',
	'sUpdateRepository' : 'https://github.com/ReenigneArcher/RetroArcher.bundle',
	'sUpdateBranch' : 'master',
	'sUpdateAuto' : 'False'
}

dPlatformMapping = {
    '1292 Advanced Programmable Video System' : {
        'systemNames' : ['1292 Advanced Programmable Video System'],
        'systemIds' : {
            'igdb' : 139,
            'thegamesdb' : None
            },
        'romExtensions' : [],
        'romType' : 0,
		'multiDisk' : False
        },
    '3DO Interactive Multiplayer' : {
        'systemNames' : ['3DO Interactive Multiplayer', '3DO'],
        'systemIds' : {
            'igdb' : 50,
            'thegamesdb' : 25
			},
        'romExtensions' : [],
        'romType' : 0,
		'multiDisk' : False
		},
    'Acorn Archimedes' : {
        'systemNames' : ['Acorn Archimedes'],
        'systemIds' : {
            'igdb' : 116,
            'thegamesdb' : 4944
			},
        'romExtensions' : [],
        'romType' : 0,
		'multiDisk' : False
		},
    'Acorn Electron' : { 
		'systemNames' : ['Acorn Electron'],
		'systemIds' : {
			'igdb' : 134,
			'thegamesdb' : 4954
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Action Max' : { 
		'systemNames' : ['Action Max'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4976
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Amazon Fire TV' : { 
		'systemNames' : ['Amazon Fire TV'],
		'systemIds' : {
			'igdb' : 132,
			'thegamesdb' : 4916 #Android
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Amstrad CPC' : { 
		'systemNames' : ['Amstrad CPC', 'ACPC', 'Colour Personal Computer'],
		'systemIds' : {
			'igdb' : 25,
			'thegamesdb' : 4914
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Amstrad PCW' : { 
		'systemNames' : ['Amstrad PCW'],
		'systemIds' : {
			'igdb' : 154,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Analogue electronics' : { 
		'systemNames' : ['Analogue electronics', 'analogueelectronics'],
		'systemIds' : {
			'igdb' : 100,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Android' : { 
		'systemNames' : ['Android'],
		'systemIds' : {
			'igdb' : 34,
			'thegamesdb' : 4916
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'APF MP-1000' : { 
		'systemNames' : ['APF MP-1000'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4969
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Apple II' : { 
		'systemNames' : ['Apple II', 'appleii'],
		'systemIds' : {
			'igdb' : 75,
			'thegamesdb' : 4942
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Apple IIGS' : { 
		'systemNames' : ['Apple IIGS'],
		'systemIds' : {
			'igdb' : 115,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Apple iOS' : { 
		'systemNames' : ['Apple iOS', 'iOS'],
		'systemIds' : {
			'igdb' : 39,
			'thegamesdb' : 4915
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Apple MAC OS' : { 
		'systemNames' : ['Apple MAC OS', 'Mac'],
		'systemIds' : {
			'igdb' : 14,
			'thegamesdb' : 37
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Arcade' : { 
		'systemNames' : ['Arcade'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Atari 2600' : { 
		'systemNames' : ['Atari 2600', 'Atari2600'],
		'systemIds' : {
			'igdb' : 59,
			'thegamesdb' : 22
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Atari 5200' : { 
		'systemNames' : ['Atari 5200', 'Atari5200'],
		'systemIds' : {
			'igdb' : 66,
			'thegamesdb' : 26
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Atari 7800' : { 
		'systemNames' : ['Atari 7800', 'Atari7800', 'Atari 7800 ProSystem'],
		'systemIds' : {
			'igdb' : 60,
			'thegamesdb' : 27
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Atari 800' : { 
		'systemNames' : ['Atari 800', 'Atari 8-bit', 'Atari800', 'Atari8bit'],
		'systemIds' : {
			'igdb' : 64,
			'thegamesdb' : 4943
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Atari Jaguar' : { 
		'systemNames' : ['Atari Jaguar', 'Jaguar'],
		'systemIds' : {
			'igdb' : 62,
			'thegamesdb' : 28
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Atari Jaguar CD' : { 
		'systemNames' : ['Atari Jaguar CD', 'Jaguar CD'],
		'systemIds' : {
			'igdb' : 62,
			'thegamesdb' : 29
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Atari Lynx' : { 
		'systemNames' : ['Atari Lynx', 'Lynx'],
		'systemIds' : {
			'igdb' : 61,
			'thegamesdb' : 4924
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Atari ST' : { 
		'systemNames' : ['Atari ST', 'Atari ST/STE', 'Atari-ST', 'Atari-STE', 'Atari STE'],
		'systemIds' : {
			'igdb' : 63,
			'thegamesdb' : 4937
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Atari XE' : { 
		'systemNames' : ['Atari XE', 'Atari-XE'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 30
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'AY-3-8500' : { 
		'systemNames' : ['AY-3-8500'],
		'systemIds' : {
			'igdb' : 140,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'AY-3-8603' : { 
		'systemNames' : ['AY-3-8603'],
		'systemIds' : {
			'igdb' : 145,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'AY-3-8605' : { 
		'systemNames' : ['AY-3-8605'],
		'systemIds' : {
			'igdb' : 146,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'AY-3-8606' : { 
		'systemNames' : ['AY-3-8606'],
		'systemIds' : {
			'igdb' : 147,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'AY-3-8607' : { 
		'systemNames' : ['AY-3-8607'],
		'systemIds' : {
			'igdb' : 148,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'AY-3-8610' : { 
		'systemNames' : ['AY-3-8610'],
		'systemIds' : {
			'igdb' : 141,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'AY-3-8710' : { 
		'systemNames' : ['AY-3-8710'],
		'systemIds' : {
			'igdb' : 144,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'AY-3-8760' : { 
		'systemNames' : ['AY-3-8760'],
		'systemIds' : {
			'igdb' : 143,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Bally Astrocade' : { 
		'systemNames' : ['Bally Astrocade', 'astrocade'],
		'systemIds' : {
			'igdb' : 91,
			'thegamesdb' : 4968
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'BBC Microcomputer System' : { 
		'systemNames' : ['BBC Microcomputer System', 'bbcmicro'],
		'systemIds' : {
			'igdb' : 69,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'BlackBerry OS' : { 
		'systemNames' : ['BlackBerry OS', 'BlackBerry'],
		'systemIds' : {
			'igdb' : 73,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Blu-Ray Player' : { 
		'systemNames' : ['Blu-Ray Player', 'Blu-Ray'],
		'systemIds' : {
			'igdb' : 239,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Call-A-Computer' : { 
		'systemNames' : ['Call-A-Computer', 'Call-A-Computer time-shared mainframe computer system'],
		'systemIds' : {
			'igdb' : 107,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Casio PV-1000' : { 
		'systemNames' : ['Casio PV-1000'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4964
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'CDC Cyber 70' : { 
		'systemNames' : ['CDC Cyber 70', 'cdccyber70'],
		'systemIds' : {
			'igdb' : 109,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Coleco Telstar Arcade' : { 
		'systemNames' : ['Coleco Telstar Arcade'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4970
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'ColecoVision' : { 
		'systemNames' : ['ColecoVision', 'colecovision'],
		'systemIds' : {
			'igdb' : 68,
			'thegamesdb' : 31
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Commodore 16' : { 
		'systemNames' : ['Commodore 16', 'C16'],
		'systemIds' : {
			'igdb' : 93,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Commodore 64' : { 
		'systemNames' : ['Commodore 64', 'C64'],
		'systemIds' : {
			'igdb' : 15,
			'thegamesdb' : 40
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Commodore 128' : { 
		'systemNames' : ['Commodore 128', 'C128'],
		'systemIds' : {
			'igdb' : 15,
			'thegamesdb' : 4946
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Commodore Amiga' : { 
		'systemNames' : ['Commodore Amiga', 'Amiga'],
		'systemIds' : {
			'igdb' : 16,
			'thegamesdb' : 4911
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Commodore Amiga CD32' : { 
		'systemNames' : ['Commodore Amiga CD32', 'Amiga CD32'],
		'systemIds' : {
			'igdb' : 114,
			'thegamesdb' : 4947
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Commodore CDTV' : { 
		'systemNames' : ['Commodore CDTV'],
		'systemIds' : {
			'igdb' : 158,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Commodore PET' : { 
		'systemNames' : ['Commodore PET', 'cpet'],
		'systemIds' : {
			'igdb' : 90,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Commodore Plus 4' : { 
		'systemNames' : ['Commodore Plus 4', 'Commodore Plus/4', 'C+4'],
		'systemIds' : {
			'igdb' : 94,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Commodore VIC-20-20' : { 
		'systemNames' : ['Commodore VIC-20', 'vic-20'],
		'systemIds' : {
			'igdb' : 71,
			'thegamesdb' : 4945
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Daphne' : { 
		'systemNames' : ['Daphne'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Daydream' : { 
		'systemNames' : ['Daydream'],
		'systemIds' : {
			'igdb' : 164,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'DEC GT40' : { 
		'systemNames' : ['DEC GT40', 'gt40'],
		'systemIds' : {
			'igdb' : 98,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Doom' : { 
		'systemNames' : ['Doom', 'Prboom'],
		'systemIds' : {
			'igdb' : 13,
			'thegamesdb' : 1
			},
		'romExtensions' : ['wad'],
		'romType' : 1,
		'multiDisk' : False
		},
    'Donner Model 30' : { 
		'systemNames' : ['Donner Model 30', 'donner30', 'Donner 30'],
		'systemIds' : {
			'igdb' : 85,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Dragon 32' : { 
		'systemNames' : ['Dragon 32'],
		'systemIds' : {
			'igdb' : 153,
			'thegamesdb' : 4952
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Dragon 64' : { 
		'systemNames' : ['Dragon 64'],
		'systemIds' : {
			'igdb' : 153,
			'thegamesdb' : 4952
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'DVD Player' : { 
		'systemNames' : ['DVD Player', 'Digital Versatile Disc Player', 'DVD'],
		'systemIds' : {
			'igdb' : 238,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'EDSAC' : { 
		'systemNames' : ['EDSAC', 'Electronic Delay Storage Automatic Calculator'],
		'systemIds' : {
			'igdb' : 102,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Emerson Arcadia 2001' : { 
		'systemNames' : ['Emerson Arcadia 2001'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4963
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Entex Adventure Vision' : { 
		'systemNames' : ['Entex Adventure Vision'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4974
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Entex Select-A-Game-a-game' : { 
		'systemNames' : ['Entex Select-A-Game'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4973
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Epoch Cassette Vision' : { 
		'systemNames' : ['Epoch Cassette Vision'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4965
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Epoch Super Cassette Vision' : { 
		'systemNames' : ['Epoch Super Cassette Vision'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4966
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Evercade' : { 
		'systemNames' : ['Evercade'],
		'systemIds' : {
			'igdb' : 309,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Exidy Sorcerer' : { 
		'systemNames' : ['Exidy Sorcerer'],
		'systemIds' : {
			'igdb' : 236,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Fairchild Channel F' : { 
		'systemNames' : ['Fairchild Channel F'],
		'systemIds' : {
			'igdb' : 127,
			'thegamesdb' : 4928
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Ferranti Nimrod Computer' : { 
		'systemNames' : ['Ferranti Nimrod Computer', 'Nimrod'],
		'systemIds' : {
			'igdb' : 101,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Final Burn Alpha' : { 
		'systemNames' : ['Final Burn Alpha', 'FBA'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Final Burn Alpha - Libreto' : { 
		'systemNames' : ['Final Burn Alpha - Libreto', 'FBAL'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Fujitsu FM Towns Marty' : { 
		'systemNames' : ['Fujitsu FM Towns Marty', 'FM Towns'],
		'systemIds' : {
			'igdb' : 118,
			'thegamesdb' : 4932
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Fujitsu FM-7-7' : { 
		'systemNames' : ['Fujitsu FM-7', 'FM-7', 'Fujitsu Micro 7'],
		'systemIds' : {
			'igdb' : 152,
			'thegamesdb' : 4978
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Gakken Compact Vision' : { 
		'systemNames' : ['Gakken Compact Vision'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4962
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Game.com' : { 
		'systemNames' : ['Game.com'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4940
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'GCE Vectrex' : { 
		'systemNames' : ['GCE Vectrex', 'Vectrex'],
		'systemIds' : {
			'igdb' : 70,
			'thegamesdb' : 4939
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Google Stadia' : { 
		'systemNames' : ['Google Stadia', 'Stadia'],
		'systemIds' : {
			'igdb' : [170, 203],
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Handheld Electronic Games' : { 
		'systemNames' : ['Handheld Electronic Games', 'Handheld Electronic Games (LCD)'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4951
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'HP 2100' : { 
		'systemNames' : ['HP 2100', 'hp2100'],
		'systemIds' : {
			'igdb' : 104,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'HP 3000' : { 
		'systemNames' : ['HP 3000', 'hp3000'],
		'systemIds' : {
			'igdb' : 105,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Imlac PDS-1' : { 
		'systemNames' : ['Imlac PDS-1', 'imlac-pds1'],
		'systemIds' : {
			'igdb' : 111,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Interton VC 4000' : { 
		'systemNames' : ['Interton VC 4000', 'VC 4000'],
		'systemIds' : {
			'igdb' : 138,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Linux' : { 
		'systemNames' : ['Linux', 'GNU/Linux', 'GNU'],
		'systemIds' : {
			'igdb' : 3,
			'thegamesdb' : 1
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Magnavox Odyssey' : { 
		'systemNames' : ['Magnavox Odyssey', 'Magnavox Odyssey 1', 'Odyssey 1', 'Odyssey', 'Odysee', 'Odisea', 'Odissea'],
		'systemIds' : {
			'igdb' : 88,
			'thegamesdb' : 4961
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Magnavox Odyssey 2' : { 
		'systemNames' : ['Magnavox Odyssey 2', 'Philips Videopac+', 'Philips Videopac G7000', 'Magnavox Odyssey\u00b2', 'Videopac', 'Philips Odyssey'],
		'systemIds' : {
			'igdb' : 133,
			'thegamesdb' : 4927
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Mame' : { 
		'systemNames' : ['Mame'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Mattel Intellivision' : { 
		'systemNames' : ['Mattel Intellivision', 'Intellivision'],
		'systemIds' : {
			'igdb' : 67,
			'thegamesdb' : 32
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Mega Duck' : { 
		'systemNames' : ['Mega Duck'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4948
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microcomputer' : { 
		'systemNames' : ['Microcomputer'],
		'systemIds' : {
			'igdb' : 112,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microsoft DOS' : { 
		'systemNames' : ['Microsoft DOS', 'MS-DOS', 'PC DOS', 'DOS'],
		'systemIds' : {
			'igdb' : 13,
			'thegamesdb' : 1
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microsoft MSX' : { 
		'systemNames' : ['Microsoft MSX', 'MSX'],
		'systemIds' : {
			'igdb' : 27,
			'thegamesdb' : 4929
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microsoft MSX2' : { 
		'systemNames' : ['Microsoft MSX2', 'MSX2'],
		'systemIds' : {
			'igdb' : 53,
			'thegamesdb' : 4929
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microsoft MSX2+' : { 
		'systemNames' : ['Microsoft MSX2+', 'MSX2+'],
		'systemIds' : {
			'igdb' : 53,
			'thegamesdb' : 4929
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microsoft MSX TurboR' : { 
		'systemNames' : ['Microsoft MSX TurboR', 'MSX TurboR'],
		'systemIds' : {
			'igdb' : 53,
			'thegamesdb' : 4929
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microsoft Windows' : { 
		'systemNames' : ['Microsoft Windows', 'Windows', 'PC (Microsoft Windows)', 'PC', 'mswin'],
		'systemIds' : {
			'igdb' : 6,
			'thegamesdb' : 1
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microsoft Windows 3.X' : { 
		'systemNames' : ['Microsoft Windows 3.X', 'Windows 3.X', 'PC (Microsoft Windows 3.X)', 'Microsoft Windows 3.1', 'Windows 3.1', 'PC (Microsoft Windows 3.1)'],
		'systemIds' : {
			'igdb' : 6,
			'thegamesdb' : 1
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microsoft Xbox' : { 
		'systemNames' : ['Microsoft Xbox', 'Xbox'],
		'systemIds' : {
			'igdb' : 11,
			'thegamesdb' : 14
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microsoft Xbox 360' : { 
		'systemNames' : ['Microsoft Xbox 360', 'Xbox 360', 'X360', 'xbx360'],
		'systemIds' : {
			'igdb' : 12,
			'thegamesdb' : 15
			},
		'romExtensions' : ['iso'],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microsoft Xbox Live Arcade' : { 
		'systemNames' : ['Microsoft Xbox Live Arcade', 'Xbox Live Arcade', 'xla'],
		'systemIds' : {
			'igdb' : 36,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microsoft Xbox One' : { 
		'systemNames' : ['Microsoft Xbox One', 'Xbox One', 'XONE', 'Xbone'],
		'systemIds' : {
			'igdb' : 49,
			'thegamesdb' : 4920
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microsoft Xbox Series' : { 
		'systemNames' : ['Microsoft Xbox Series', 'Xbox Series', 'Series X', 'Microsoft Xbox Series X'],
		'systemIds' : {
			'igdb' : 169,
			'thegamesdb' : 4981
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Microvision' : { 
		'systemNames' : ['Microvision', 'Milton Bradley Microvision'],
		'systemIds' : {
			'igdb' : 89,
			'thegamesdb' : 4972
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Mobile' : { 
		'systemNames' : ['Mobile'],
		'systemIds' : {
			'igdb' : 55,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'NEC PC-6000 Series' : { 
		'systemNames' : ['NEC PC-6000 Series'],
		'systemIds' : {
			'igdb' : 157,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'NEC PC-8801' : { 
		'systemNames' : ['NEC PC-8801', 'PC-8801', 'PC-88'],
		'systemIds' : {
			'igdb' : 125,
			'thegamesdb' : 4933
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'NEC PC-9801' : { 
		'systemNames' : ['NEC PC-9801', 'PC-9801', 'PC-98'],
		'systemIds' : {
			'igdb' : 149,
			'thegamesdb' : 4934
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'NEC PC-FX' : { 
		'systemNames' : ['NEC PC-FX', 'PC-FX'],
		'systemIds' : {
			'igdb' : 274,
			'thegamesdb' : 4930
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'NEC TurboGrafx-16' : { 
		'systemNames' : ['NEC TurboGrafx-16', 'TurboGrafx-16', 'turbografx16'],
		'systemIds' : {
			'igdb' : 86,
			'thegamesdb' : 34
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'NEC TurboGrafx-CD' : { 
		'systemNames' : ['NEC TurboGrafx-CD', 'TurboGrafx-CD', 'NEC TurboGrafx-CD32', 'TurboGrafx-CD32'],
		'systemIds' : {
			'igdb' : 150,
			'thegamesdb' : 4955
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo New 3DS' : { 
		'systemNames' : ['Nintendo New 3DS', 'New Nintendo 3DS', 'n3DS'],
		'systemIds' : {
			'igdb' : 137,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo 3DS' : { 
		'systemNames' : ['Nintendo 3DS', '3DS'],
		'systemIds' : {
			'igdb' : 37,
			'thegamesdb' : 4912
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo 64' : { 
		'systemNames' : ['Nintendo 64', 'N64', 'Nintendo 64DD', 'N64DD'],
		'systemIds' : {
			'igdb' : 4,
			'thegamesdb' : 3
			},
		'romExtensions' : ['zip', 'n64', 'v64', 'z64', 'bin', 'u1', 'ndd'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mupen64plus_next_libretro.dll', #default
                    1 : 'mupen64plus_next_libretro.dll', #Mupen64Plus
                    'mupen64plus_next_libretro.dll' : {
                        'coreExtensions' : ['zip', 'n64', 'v64', 'z64', 'bin', 'u1', 'ndd'],
                        'friendlyName' : 'Nintendo 64 (Mupen64Plus)'
                        }
                    }
                }
            }
        },
    'Nintendo DS' : { 
		'systemNames' : ['Nintendo DS', 'NDS', 'DS'],
		'systemIds' : {
			'igdb' : 20,
			'thegamesdb' : 8
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo DSi' : { 
		'systemNames' : ['Nintendo DSi'],
		'systemIds' : {
			'igdb' : 159,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Entertainment System' : { 
		'systemNames' : ['Nintendo Entertainment System', 'Nintendo Entertainment System (NES)', 'NES'],
		'systemIds' : {
			'igdb' : 18,
			'thegamesdb' : 7
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo eShop' : { 
		'systemNames' : ['Nintendo eShop'],
		'systemIds' : {
			'igdb' : 160,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Famicom Disk System' : { 
		'systemNames' : ['Nintendo Famicom Disk System', 'Family Computer Disk System', 'fds', 'Famicom Disk System', 'NFDS', 'Nintendo Family Computer Disk System'],
		'systemIds' : {
			'igdb' : 51,
			'thegamesdb' : 4936
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Family Computer' : { 
		'systemNames' : ['Nintendo Family Computer', 'Family Computer (FAMICOM)', 'FAMICOM', 'Family Computer'],
		'systemIds' : {
			'igdb' : 99,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Game & Watch' : { 
		'systemNames' : ['Nintendo Game & Watch', 'Nintendo Game and Watch', 'Game & Watch', 'Game and Watch', 'Tricotronic'],
		'systemIds' : {
			'igdb' : 307,
			'thegamesdb' : 4950
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Game Boy' : { 
		'systemNames' : ['Nintendo Game Boy', 'Game Boy', 'GB', 'Nintendo GB'],
		'systemIds' : {
			'igdb' : 33,
			'thegamesdb' : 4
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Game Boy Advance' : { 
		'systemNames' : ['Nintendo Game Boy Advance', 'Game Boy Advance', 'GBA', 'Nintendo GBA'],
		'systemIds' : {
			'igdb' : 24,
			'thegamesdb' : 5
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Game Boy Color' : { 
		'systemNames' : ['Nintendo Game Boy Color', 'Game Boy Color', 'GBC', 'Nintendo GBC'],
		'systemIds' : {
			'igdb' : 22,
			'thegamesdb' : 41
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo GameCube' : { 
		'systemNames' : ['Nintendo GameCube', 'NGC', 'GameCube', 'GC', 'Dolphin'],
		'systemIds' : {
			'igdb' : 21,
			'thegamesdb' : 2
			},
		'romExtensions' : ['ciso', 'dol', 'elf', 'gcm', 'gcz', 'iso', 'tgc', 'wad', 'wbfs'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'dolphin_libretro.dll', #default
                    1 : 'dolphin_libretro.dll', #Dolphin
                    'dolphin_libretro.dll' : {
                        'coreExtensions' : ['ciso', 'dol', 'elf', 'gcm', 'gcz', 'iso', 'tgc', 'wad', 'wbfs'],
                        'friendlyName' : 'Nintendo GameCube (Dolphin)'
                        }
                    }
                }
            }
		},
    'Nintendo PlayStation' : { 
		'systemNames' : ['Nintendo PlayStation', 'Nintendo Super Disc'],
		'systemIds' : {
			'igdb' : 131,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Pokemon Mini' : { 
		'systemNames' : ['Nintendo Pokemon Mini', 'Nintendo Pok\u00e9mon mini', 'Pok\u00e9mon mini', 'Pokemon mini'],
		'systemIds' : {
			'igdb' : 166,
			'thegamesdb' : 4957
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Super Famicom' : { 
		'systemNames' : ['Nintendo Super Famicom', 'SFAM', 'Super Famicom', 'SFC', 'Super Family Computer', 'NSFAM', 'NSFC', 'Nintendo Super Family Computer'],
		'systemIds' : {
			'igdb' : 58,
			'thegamesdb' : 6
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Super Famicom Satellaview' : { 
		'systemNames' : ['Nintendo Super Famicom Satellaview', 'Satellaview'],
		'systemIds' : {
			'igdb' : 306,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Switch' : { 
		'systemNames' : ['Nintendo Switch', 'Switch', 'NX'],
		'systemIds' : {
			'igdb' : 130,
			'thegamesdb' : 4971
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Virtual Boy' : { 
		'systemNames' : ['Nintendo Virtual Boy', 'Virtual Boy', 'virtualboy'],
		'systemIds' : {
			'igdb' : 87,
			'thegamesdb' : 4918
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Virtual Console' : { 
		'systemNames' : ['Nintendo Virtual Console', 'Virtual Console (Nintendo)', 'VC', 'Nintendo VC'],
		'systemIds' : {
			'igdb' : 47,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo Wii' : { 
		'systemNames' : ['Nintendo Wii', 'Wii', 'Revolution'],
		'systemIds' : {
			'igdb' : 5,
			'thegamesdb' : 9
			},
		'romExtensions' : ['ciso', 'dol', 'elf', 'gcm', 'gcz', 'iso', 'tgc', 'wad', 'wbfs'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'dolphin_libretro.dll', #default
                    1 : 'dolphin_libretro.dll', #Dolphin
                    'dolphin_libretro.dll' : {
                        'coreExtensions' : ['ciso', 'dol', 'elf', 'gcm', 'gcz', 'iso', 'tgc', 'wad', 'wbfs'],
                        'friendlyName' : 'Nintendo Wii (Dolphin)'
                        }
                    }
                }
            }
		},
    'Nintendo Wii U' : { 
		'systemNames' : ['Nintendo Wii U', 'WiiU', 'Wii U'],
		'systemIds' : {
			'igdb' : 41,
			'thegamesdb' : 38
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nintendo WiiWare' : { 
		'systemNames' : ['Nintendo WiiWare', 'WiiWare'],
		'systemIds' : {
			'igdb' : 56,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nokia N-Gage' : { 
		'systemNames' : ['Nokia N-Gage', 'N-Gage', 'Ngage', 'Nokia Ngage'],
		'systemIds' : {
			'igdb' : 42,
			'thegamesdb' : 4938
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Nuon' : { 
		'systemNames' : ['Nuon'],
		'systemIds' : {
			'igdb' : 122,
			'thegamesdb' : 4935
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Oculus VR' : { 
		'systemNames' : ['Oculus VR'],
		'systemIds' : {
			'igdb' : 162,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'OnLive Game System' : { 
		'systemNames' : ['OnLive Game System'],
		'systemIds' : {
			'igdb' : 113,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'OOParts' : { 
		'systemNames' : ['OOParts'],
		'systemIds' : {
			'igdb' : 372,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Ouya' : { 
		'systemNames' : ['Ouya'],
		'systemIds' : {
			'igdb' : 72,
			'thegamesdb' : 4921
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'PC-50X Family' : { 
		'systemNames' : ['PC-50X Family'],
		'systemIds' : {
			'igdb' : 142,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'PC Engine' : { 
		'systemNames' : ['PC Engine', 'NEC PC Engine'],
		'systemIds' : {
			'igdb' : 86,
			'thegamesdb' : 34
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'PC Engine CD' : { 
		'systemNames' : ['PC Engine CD', 'NEC PC Engine CD'],
		'systemIds' : {
			'igdb' : 150,
			'thegamesdb' : 4955
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'PC Engine SuperGrafx' : { 
		'systemNames' : ['PC Engine SuperGrafx'],
		'systemIds' : {
			'igdb' : 128,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'PDP-1' : { 
		'systemNames' : ['PDP-1', 'pdp1'],
		'systemIds' : {
			'igdb' : 95,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'PDP-7' : { 
		'systemNames' : ['PDP-7'],
		'systemIds' : {
			'igdb' : 103,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'PDP-8' : { 
		'systemNames' : ['PDP-8'],
		'systemIds' : {
			'igdb' : 97,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'PDP-10' : { 
		'systemNames' : ['PDP-10', 'pdp10'],
		'systemIds' : {
			'igdb' : 96,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'PDP-11' : { 
		'systemNames' : ['PDP-11', 'pdp11'],
		'systemIds' : {
			'igdb' : 108,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Philips CD-i' : { 
		'systemNames' : ['Philips CD-i', 'CD-i'],
		'systemIds' : {
			'igdb' : 117,
			'thegamesdb' : 4917
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Pioneer Laseractive' : { 
		'systemNames' : ['Pioneer Laseractive', 'Laseractive'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4975
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'PLATO' : { 
		'systemNames' : ['PLATO', 'Programmed Logic for Automatic Teaching Operations'],
		'systemIds' : {
			'igdb' : 110,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Playdia' : { 
		'systemNames' : ['Playdia'],
		'systemIds' : {
			'igdb' : 308,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'R-Zone' : { 
		'systemNames' : ['R-Zone'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4983
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'RCA Studio II' : { 
		'systemNames' : ['RCA Studio II'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4967
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'SAM Coupé' : { 
		'systemNames' : ['SAM Coupé', 'SAM Coupe'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4979
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sammy Atomiswave' : { 
		'systemNames' : ['Sammy Atomiswave', 'Atomiswave'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'ScummVM' : { 
		'systemNames' : ['ScummVM'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'SDS Sigma 7' : { 
		'systemNames' : ['SDS Sigma 7', 'sdssigma7'],
		'systemIds' : {
			'igdb' : 106,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sega 32X' : { 
		'systemNames' : ['Sega 32X', 'Sega32', 'Sega32X'],
		'systemIds' : {
			'igdb' : 30,
			'thegamesdb' : 33
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sega CD' : { 
		'systemNames' : ['Sega CD', 'segacd', 'Mega CD'],
		'systemIds' : {
			'igdb' : 78,
			'thegamesdb' : 21
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sega Dreamcast' : { 
		'systemNames' : ['Sega Dreamcast', 'Dreamcast', 'DC'],
		'systemIds' : {
			'igdb' : 23,
			'thegamesdb' : 16
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sega Game Gear' : { 
		'systemNames' : ['Sega Game Gear', 'Game Gear', 'GG', 'Sega GG'],
		'systemIds' : {
			'igdb' : 35,
			'thegamesdb' : 20
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sega Genesis' : { 
		'systemNames' : ['Sega Genesis', 'Genesis'],
		'systemIds' : {
			'igdb' : 29,
			'thegamesdb' : 18
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sega Master System' : { 
		'systemNames' : ['Sega Master System', 'SMS', 'Master System', 'Sega Mark III', 'Mark III'],
		'systemIds' : {
			'igdb' : 64,
			'thegamesdb' : 35
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sega Mega Drive' : { 
		'systemNames' : ['Sega Mega Drive', 'Mega Drive'],
		'systemIds' : {
			'igdb' : 29,
			'thegamesdb' : 36
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sega Naomi' : { 
		'systemNames' : ['Sega Naomi', 'Naomi'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sega Naomi 2' : { 
		'systemNames' : ['Sega Naomi 2', 'Naomi 2'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sega Pico' : { 
		'systemNames' : ['Sega Pico', 'Pico'],
		'systemIds' : {
			'igdb' : 339,
			'thegamesdb' : 4958
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sega Saturn' : { 
		'systemNames' : ['Sega Saturn', 'Saturn', 'JVC Saturn', 'Hi-Saturn', 'Samsung Saturn', 'V-Saturn'],
		'systemIds' : {
			'igdb' : 32,
			'thegamesdb' : 17
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sega SG-1000' : { 
		'systemNames' : ['Sega SG-1000', 'SG-1000', 'sg1000', 'Sega Game 1000'],
		'systemIds' : {
			'igdb' : 84,
			'thegamesdb' : 4949
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sharp MZ-2200' : { 
		'systemNames' : ['Sharp MZ-2200', 'MZ-2200', 'MZ2200'],
		'systemIds' : {
			'igdb' : 374,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sharp X1' : { 
		'systemNames' : ['Sharp X1', 'x1'],
		'systemIds' : {
			'igdb' : 77,
			'thegamesdb' : 4977
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sharp X68000' : { 
		'systemNames' : ['Sharp X68000', 'x68000'],
		'systemIds' : {
			'igdb' : 121,
			'thegamesdb' : 4931
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sinclair ZX Spectrum' : { 
		'systemNames' : ['Sinclair ZX Spectrum', 'ZX Spectrum', 'ZXS'],
		'systemIds' : {
			'igdb' : 26,
			'thegamesdb' : 4913
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sinclair ZX-81' : { 
		'systemNames' : ['Sinclair ZX-81', 'ZX-81', 'Sinclair ZX81', 'ZX81'],
		'systemIds' : {
			'igdb' : 373,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'SNK Hyper Neo Geo 64' : { 
		'systemNames' : ['SNK Hyper Neo Geo 64', 'Hyper Neo Geo 64'],
		'systemIds' : {
			'igdb' : 135,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'SNK Neo Geo AES' : { 
		'systemNames' : ['SNK Neo Geo AES', 'Neo Geo AES', 'neogeoaes', 'AES', 'Neo Geo'],
		'systemIds' : {
			'igdb' : 80,
			'thegamesdb' : 24
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'SNK Neo Geo CD' : { 
		'systemNames' : ['SNK Neo Geo CD', 'Neo Geo CD'],
		'systemIds' : {
			'igdb' : 136,
			'thegamesdb' : 4956
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'SNK Neo Geo MVS' : { 
		'systemNames' : ['SNK Neo Geo MVS', 'Neo Geo MVS', 'neogeomvs', 'Neo Geo Multi Video System'],
		'systemIds' : {
			'igdb' : 79,
			'thegamesdb' : 24
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'SNK Neo Geo Pocket' : { 
		'systemNames' : ['SNK Neo Geo Pocket', 'Neo Geo Pocket'],
		'systemIds' : {
			'igdb' : 119,
			'thegamesdb' : 4922
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'SNK Neo Geo Pocket Color' : { 
		'systemNames' : ['SNK Neo Geo Pocket Color', 'Neo Geo Pocket Color'],
		'systemIds' : {
			'igdb' : 120,
			'thegamesdb' : 4923
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sol-20' : { 
		'systemNames' : ['Sol-20'],
		'systemIds' : {
			'igdb' : 237,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sony PlayStation' : { 
		'systemNames' : ['Sony PlayStation', 'PlayStation', 'PS', 'PS1', 'PlayStation 1', 'Sony PlayStation 1'],
		'systemIds' : {
			'igdb' : 7,
			'thegamesdb' : 10
			},
		'romExtensions' : ['cbn', 'ccd', 'chd', 'cue', 'exe', 'img', 'mdf', 'pbp', 'toc'], #don't include m3u during scanning
		'romType' : 0,
        'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'duckstation_libretro.dll', #default
                    1 : 'mednafen_psx_libretro.dll', #Beetle PSX
                    2 : 'mednafen_psx_hw_libretro.dll', #Beetle PSX HW
                    3 : 'duckstation_libretro.dll', #DuckStation
                    4 : 'pcsx_rearmed_libretro.dll', #PCSX ReARMed
                    'mednafen_psx_libretro.dll' : {
                        'coreExtensions' : ['ccd', 'chd', 'cue', 'exe', 'm3u', 'pbp', 'toc'],
                        'friendlyName' : 'Sony - Playstation (Beetle PSX)'
                        },
                    'mednafen_psx_hw_libretro.dll' : {
                        'coreExtensions' : ['ccd', 'chd', 'cue', 'exe', 'm3u', 'pbp', 'toc'],
                        'friendlyName' : 'Sony - Playstation (Beetle PSX HW)'
                        },
                    'duckstation_libretro.dll' : {
                        'coreExtensions' : ['chd', 'cue', 'm3u'],
                        'friendlyName' : 'Sony - Playstation (DuckStation)'
                        },
                    'pcsx_rearmed_libretro.dll' : {
                        'coreExtensions' : ['cbn', 'ccd', 'cue', 'img', 'm3u', 'mdf', 'pbp', 'toc'],
                        'friendlyName' : 'Sony - Playstation (PCSX ReARMed)'
                        }
                    }
                }
            }
        },
    'Sony PlayStation 2' : { 
		'systemNames' : ['Sony PlayStation 2', 'PlayStation 2', 'PS2'],
		'systemIds' : {
			'igdb' : 8,
			'thegamesdb' : 11
			},
		'romExtensions' : ['ciso', 'cue', 'elf', 'iso'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' :
            {'retroarch' :
                {'cores' :
                    {'PCSX2' : {
                        'coreExtensions' : ['ciso', 'cue', 'elf', 'iso'],
                        'friendlyName' : 'Sony - Playstation 2 (PCSX2)'
                        }
                    }
                }
            }
        },
    'Sony PlayStation 3' : { 
		'systemNames' : ['Sony PlayStation 3', 'PlayStation 3', 'PS3'],
		'systemIds' : {
			'igdb' : 9,
			'thegamesdb' : 12
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sony PlayStation 4' : { 
		'systemNames' : ['Sony PlayStation 4', 'PlayStation 4', 'PS4'],
		'systemIds' : {
			'igdb' : 48,
			'thegamesdb' : 4919
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sony PlayStation 5' : { 
		'systemNames' : ['Sony PlayStation 5', 'PlayStation 5', 'PS5'],
		'systemIds' : {
			'igdb' : 167,
			'thegamesdb' : 4980
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sony PlayStation Network' : { 
		'systemNames' : ['Sony PlayStation Network', 'PlayStation Network', 'psn'],
		'systemIds' : {
			'igdb' : 45,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sony PSP' : { 
		'systemNames' : ['Sony PSP', 'PlayStation Portable', 'PSP', 'Sony PlayStation Portable'],
		'systemIds' : {
			'igdb' : 38,
			'thegamesdb' : 13
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' :
            {'retroarch' :
                {'cores' :
                    {'PPSSPP' : {
                        'coreExtensions' : ['cso', 'elf', 'iso', 'pbp', 'prx'],
                        'friendlyName' : 'Sony - Playstation Portable (PPSSPP)'
                        }
                    }
                }
            }
		},
    'Sony PlayStation Vita' : { 
		'systemNames' : ['Sony PlayStation Vita', 'PlayStation Vita', 'Vita', 'PS Vita'],
		'systemIds' : {
			'igdb' : 46,
			'thegamesdb' : 39
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Sony PlayStation VR' : { 
		'systemNames' : ['Sony PlayStation VR', 'PlayStation VR'],
		'systemIds' : {
			'igdb' : 165,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Steam VR' : { 
		'systemNames' : ['Steam VR'],
		'systemIds' : {
			'igdb' : 163,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Super Nintendo Entertainment System' : { 
		'systemNames' : ['Super Nintendo Entertainment System', 'Super Nintendo Entertainment System (SNES)', 'SNES'],
		'systemIds' : {
			'igdb' : 19,
			'thegamesdb' : 6
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'SwanCrystal' : { 
		'systemNames' : ['SwanCrystal'],
		'systemIds' : {
			'igdb' : 124,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Tandy TRS-80' : { 
		'systemNames' : ['Tandy TRS-80', 'TRS-80'],
		'systemIds' : {
			'igdb' : 126,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Tandy TRS-80 Color Computer' : { 
		'systemNames' : ['Tandy TRS-80 Color Computer', 'TRS-80 Color Computer', 'Tandy Color Computer'],
		'systemIds' : {
			'igdb' : 151,
			'thegamesdb' : 4941
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Tandy Visual Interactive System' : { 
		'systemNames' : ['Tandy Visual Interactive System', 'Tandy VIS'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4982
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Tapwave Zodiac' : { 
		'systemNames' : ['Tapwave Zodiac', 'zod', 'Zodiac'],
		'systemIds' : {
			'igdb' : 44,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Tatung Einstein' : { 
		'systemNames' : ['Tatung Einstein'],
		'systemIds' : {
			'igdb' : 155,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Texas Instruments TI-99/4A' : { 
		'systemNames' : ['Texas Instruments TI-99/4A', 'Texas Instruments TI-99', 'ti-99'],
		'systemIds' : {
			'igdb' : 129,
			'thegamesdb' : 4953
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Thomson MO5' : { 
		'systemNames' : ['Thomson MO5'],
		'systemIds' : {
			'igdb' : 156,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Tomy Tutor' : { 
		'systemNames' : ['Tomy Tutor'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4960
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Watara Supervision' : { 
		'systemNames' : ['Watara Supervision'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4959
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Web browser' : { 
		'systemNames' : ['Web browser', 'browser', 'Internet'],
		'systemIds' : {
			'igdb' : 82,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Windows Mixed Reality' : { 
		'systemNames' : ['Windows Mixed Reality'],
		'systemIds' : {
			'igdb' : 161,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Windows Phone' : { 
		'systemNames' : ['Windows Phone', 'Win Phone', 'WP'],
		'systemIds' : {
			'igdb' : 74,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'WonderSwan' : { 
		'systemNames' : ['WonderSwan', 'Bandai WonderSwan'],
		'systemIds' : {
			'igdb' : 57,
			'thegamesdb' : 4925
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'WonderSwan Color' : { 
		'systemNames' : ['WonderSwan Color', 'Bandai WonderSwan Color'],
		'systemIds' : {
			'igdb' : 123,
			'thegamesdb' : 4926
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'XAVIX Port' : { 
		'systemNames' : ['XAVIX Port'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4984
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Zeebo' : { 
		'systemNames' : ['Zeebo'],
		'systemIds' : {
			'igdb' : 240,
			'thegamesdb' : None
			},
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
}
