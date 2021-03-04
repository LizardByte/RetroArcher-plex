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

dEncoderMapping = {
    '0' : 'h264_nvenc',
    '1' : 'h264_qsv',
    '2' : 'h264_videotoolbox',
    '3' : 'libx264',
    '4' : 'mpeg2_qsv',
    '5' : 'mpeg2video'
}

dDefaultSettings = {
	'sSourceRomDirectory' : '',
	
	'lExcludedTerms' : '[BIOS], Action Replay, Game Genie, Game Saver, GameBooster, GameShark',
    'lIncludeRegions' : '',
    'lExcludeRegions' : '',
    'lIncludeLanguages' : '',
    'lExcludeLanguages' : '',
    'lExcludeTags' : 'Beta, Demo, Kiosk, Proto',
    'eFfmpegEncoder' : '0',
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
	
    #these are needed to ensure we don't scan any unsupported systems
    'scanner_3do_interactive_multiplayer' : 'True',
    'scanner_amstrad_cpc' : 'True',
    'scanner_arcade' : 'True',
    'scanner_arcade_daphne' : 'True',
    'scanner_arcade_finalburn' : 'True',
    'scanner_arcade_mame' : 'True',
    'scanner_atari_2600' : 'True',
    'scanner_atari_5200' : 'True',
    'scanner_atari_7800' : 'True',
    'scanner_atari_800' : 'True',
    'scanner_atari_jaguar' : 'True',
    'scanner_atari_jaguar_cd' : 'True',
    'scanner_atari_lynx' : 'True',
    'scanner_atari_st' : 'True',
    'scanner_atari_xe' : 'True',
    'scanner_cave_story_engine' : 'True',
    'scanner_chailove_engine' : 'True',
    'scanner_colecovision' : 'True',
    'scanner_commodore_amiga' : 'True',
    'scanner_commodore_128' : 'True',
    'scanner_commodore_64' : 'True',
    'scanner_commodore_64_supercpu' : 'True',
    'scanner_commodore_pet' : 'True',
    'scanner_commodore_plus_4' : 'True',
    'scanner_commodore_vic-20' : 'True',
    'scanner_doom_engine' : 'True',
    'scanner_fairchild_channel_f' : 'True',
    'scanner_gce_vectrex' : 'True',
    'scanner_lua_engine' : 'True',
    'scanner_magnovox_odyssey_2' : 'True',
    'scanner_mattel_intellivision' : 'True',
    'scanner_microsoft_dos' : 'True',
    'scanner_microsoft_msx' : 'True',
    'scanner_microsoft_msx2' : 'True',
    'scanner_microsoft_msx2_plus' : 'True',
    'scanner_microsoft_msx_turbor' : 'True',
    'scanner_nec_pc-8801' : 'True',
    'scanner_nec_pc-9801' : 'True',
    'scanner_nec_pc-fx' : 'True',
    'scanner_nec_pc_engine' : 'True',
    'scanner_nec_pc_engine_cd' : 'True',
    'scanner_nec_pc_engine_supergrafx' : 'True',
    'scanner_nec_turbografx-16' : 'True',
    'scanner_nec_turbografx-cd' : 'True',
    'scanner_nintendo_3ds' : 'True',
    'scanner_nintendo_64' : 'True',
    'scanner_nintendo_gamecube' : 'True',
    'scanner_nintendo_game_and_watch' : 'True',
    'scanner_nintendo_wii' : 'True',
    'scanner_outrun_engine' : 'True',
	'scanner_sega_sg-1000' : 'True',
	'scanner_sony_playstation' : 'True',
	'scanner_sony_playstation_2' : 'True',
	'scanner_sony_psp' : 'True',
	'scanner_wonderswan' : 'True',
	'scanner_wonderswan_color' : 'True',
	
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
        'romExtensions' : ['chd', 'cue', 'iso'],
        'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'opera_libretro.dll', #default
                    1 : 'opera_libretro.dll', #Opera
                    'opera_libretro.dll' : {
                        'coreExtensions' : ['iso', 'bin', 'chd', 'cue'],
                        'friendlyName' : 'The 3DO Company - 3DO (Opera)'
                        }
                    }
                }
            }
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
		'romExtensions' : ['cdt', 'cpr', 'dsk', 'kcr', 'sna', 'tap', 'voc', 'zip'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'cap32_libretro.dll', #default
                    1 : 'cap32_libretro.dll', #Caprice32
                    2 : 'crocods_libretro.dll', #CrocoDS
                    'cap32_libretro.dll' : {
                        'coreExtensions' : ['dsk', 'sna', 'zip', 'tap', 'cdt', 'voc', 'cpr', 'm3u'],
                        'friendlyName' : 'Amstrad - CPC (Caprice32)'
                        },
                    'crocods_libretro.dll' : {
                        'coreExtensions' : ['dsk', 'sna', 'kcr'],
                        'friendlyName' : 'Amstrad - CPC (CrocoDS)'
                        }
                    }
                }
            }
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
		'romExtensions' : ['7z', 'ccd', 'chd', 'cmd', 'cue', 'iso', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mame2000_libretro.dll', #default
                    1 : 'daphne_libretro.dll', #Daphne
                    2 : 'fbalpha2012_cps1_libretro.dll', #FB Alpha 2012 CPS-1
                    3 : 'fbalpha2012_cps2_libretro.dll', #FB Alpha 2012 CPS-2
                    4 : 'fbalpha2012_cps3_libretro.dll', #FB Alpha 2012 CPS-3
                    5 : 'fbalpha2012_neogeo_libretro.dll', #FB Alpha 2012 Neo Geo
                    6 : 'fbalpha2012_libretro.dll', #FB Alpha 2012
                    7 : 'fbneo_libretro.dll', #FinalBurn Neo
                    8 : 'hbmame_libretro.dll', #HBMAME
                    9 : 'mamearcade_libretro.dll', #MAME - Current
                    10 : 'mame2000_libretro.dll', #MAME 2000
                    11 : 'mame2003_midway_libretro.dll', #MAME 2003 - Midway
                    12 : 'mame2003_libretro.dll', #MAME 2003
                    13 : 'mame2003_plus_libretro.dll', #MAME 2003-Plus
                    14 : 'mame2010_libretro.dll', #MAME 2010
                    15 : 'mame2015_libretro.dll', #MAME 2015
                    16 : 'mame2016_libretro.dll', #MAME 2016
                    'daphne_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (Daphne)'
                        },
                    'fbalpha2012_cps1_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (FB Alpha 2012 CPS-1)'
                        },
                    'fbalpha2012_cps2_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (FB Alpha 2012 CPS-2)'
                        },
                    'fbalpha2012_cps3_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (FB Alpha 2012 CPS-3)'
                        },
                    'fbalpha2012_neogeo_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (FB Alpha 2012 Neo Geo)'
                        },
                    'fbalpha2012_libretro.dll' : {
                        'coreExtensions' : ['iso', 'zip', '7z'],
                        'friendlyName' : 'Arcade (FB Alpha 2012)'
                        },
                    'fbneo_libretro.dll' : {
                        'coreExtensions' : ['zip', '7z', 'cue', 'ccd'],
                        'friendlyName' : 'Arcade (FinalBurn Neo)'
                        },
                    'hbmame_libretro.dll' : {
                        'coreExtensions' : ['zip', 'chd', '7z', 'cmd'],
                        'friendlyName' : 'Arcade (HBMAME)'
                        },
                    'mamearcade_libretro.dll' : {
                        'coreExtensions' : ['zip', 'chd', '7z', 'cmd'],
                        'friendlyName' : 'Arcade (Mame - Current)'
                        },
                    'mame2000_libretro.dll' : {
                        'coreExtensions' : ['zip', '7z', 'chd'],
                        'friendlyName' : 'Arcade (MAME 2000)'
                        },
                    'mame2003_midway_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (MAME 2003 - Midway)'
                        },
                    'mame2003_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (MAME 2003)'
                        },
                    'mame2003_plus_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (MAME 2003-Plus)'
                        },
                    'mame2010_libretro.dll' : {
                        'coreExtensions' : ['zip', '7z', 'chd'],
                        'friendlyName' : 'Arcade (MAME 2010)'
                        },
                    'mame2015_libretro.dll' : {
                        'coreExtensions' : ['zip', 'chd', '7z', 'cmd'],
                        'friendlyName' : 'Arcade (MAME 2015)'
                        },
                    'mame2016_libretro.dll' : {
                        'coreExtensions' : ['zip', 'chd', '7z', 'cmd'],
                        'friendlyName' : 'Arcade (MAME 2016)'
                        }
                    }
                }
            }
		},
    'Arcade - Daphne' : { 
		'systemNames' : ['Daphne'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
				'romExtensions' : ['zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'daphne_libretro.dll', #default
                    1 : 'daphne_libretro.dll', #Daphne
                    'daphne_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (Daphne)'
                        }
                    }
                }
            }
		},
    'Arcade - FinalBurn' : { 
		'systemNames' : ['Final Burn Alpha', 'FBA', 'Final Burn Neo', 'FinalBurn Neo' 'FBN'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
        'romExtensions' : ['7z', 'ccd', 'cue', 'iso', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'fbneo_libretro.dll', #default
                    1 : 'fbalpha2012_cps1_libretro.dll', #FB Alpha 2012 CPS-1
                    2 : 'fbalpha2012_cps2_libretro.dll', #FB Alpha 2012 CPS-2
                    3 : 'fbalpha2012_cps3_libretro.dll', #FB Alpha 2012 CPS-3
                    4 : 'fbalpha2012_neogeo_libretro.dll', #FB Alpha 2012 Neo Geo
                    5 : 'fbalpha2012_libretro.dll', #FB Alpha 2012
                    6 : 'fbneo_libretro.dll', #FinalBurn Neo
                    'fbalpha2012_cps1_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (FB Alpha 2012 CPS-1)'
                        },
                    'fbalpha2012_cps2_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (FB Alpha 2012 CPS-2)'
                        },
                    'fbalpha2012_cps3_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (FB Alpha 2012 CPS-3)'
                        },
                    'fbalpha2012_neogeo_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (FB Alpha 2012 Neo Geo)'
                        },
                    'fbalpha2012_libretro.dll' : {
                        'coreExtensions' : ['iso', 'zip', '7z'],
                        'friendlyName' : 'Arcade (FB Alpha 2012)'
                        },
                    'fbneo_libretro.dll' : {
                        'coreExtensions' : ['zip', '7z', 'cue', 'ccd'],
                        'friendlyName' : 'Arcade (FinalBurn Neo)'
                        }
                    }
                }
            }
		},
    'Arcade - MAME' : { 
		'systemNames' : ['MAME'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
        'romExtensions' : ['7z', 'chd', 'cmd', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mame2000_libretro.dll', #default
                    1 : 'hbmame_libretro.dll', #HBMAME
                    2 : 'mamearcade_libretro.dll', #MAME - Current
                    3 : 'mame2000_libretro.dll', #MAME 2000
                    4 : 'mame2003_midway_libretro.dll', #MAME 2003 - Midway
                    5 : 'mame2003_libretro.dll', #MAME 2003
                    6 : 'mame2003_plus_libretro.dll', #MAME 2003-Plus
                    7 : 'mame2010_libretro.dll', #MAME 2010
                    8 : 'mame2015_libretro.dll', #MAME 2015
                    9 : 'mame2016_libretro.dll', #MAME 2016
                    'hbmame_libretro.dll' : {
                        'coreExtensions' : ['zip', 'chd', '7z', 'cmd'],
                        'friendlyName' : 'Arcade (HBMAME)'
                        },
                    'mamearcade_libretro.dll' : {
                        'coreExtensions' : ['zip', 'chd', '7z', 'cmd'],
                        'friendlyName' : 'Arcade (Mame - Current)'
                        },
                    'mame2000_libretro.dll' : {
                        'coreExtensions' : ['zip', '7z', 'chd'],
                        'friendlyName' : 'Arcade (MAME 2000)'
                        },
                    'mame2003_midway_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (MAME 2003 - Midway)'
                        },
                    'mame2003_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (MAME 2003)'
                        },
                    'mame2003_plus_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Arcade (MAME 2003-Plus)'
                        },
                    'mame2010_libretro.dll' : {
                        'coreExtensions' : ['zip', '7z', 'chd'],
                        'friendlyName' : 'Arcade (MAME 2010)'
                        },
                    'mame2015_libretro.dll' : {
                        'coreExtensions' : ['zip', 'chd', '7z', 'cmd'],
                        'friendlyName' : 'Arcade (MAME 2015)'
                        },
                    'mame2016_libretro.dll' : {
                        'coreExtensions' : ['zip', 'chd', '7z', 'cmd'],
                        'friendlyName' : 'Arcade (MAME 2016)'
                        }
                    }
                }
            }
		},
    'Atari 2600' : { 
		'systemNames' : ['Atari 2600', 'Atari2600'],
		'systemIds' : {
			'igdb' : 59,
			'thegamesdb' : 22
			},
		'romExtensions' : ['a26', 'bin'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'stella_libretro.dll', #default
                    1 : 'stella_libretro.dll', #Stella
                    'stella_libretro.dll' : {
                        'coreExtensions' : ['a26', 'bin'],
                        'friendlyName' : 'Atari - 2600 (Stella)'
                        }
                    }
                }
            }
		},
    'Atari 5200' : { 
		'systemNames' : ['Atari 5200', 'Atari5200'],
		'systemIds' : {
			'igdb' : 66,
			'thegamesdb' : 26
			},
		'romExtensions' : ['a52', 'atr', 'atx', 'bin', 'cas', 'cdm', 'xex', 'xfd', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'atari800_libretro.dll', #default
                    1 : 'atari800_libretro.dll', #Stella
                    'atari800_libretro.dll' : {
                        'coreExtensions' : ['xfd', 'atr', 'cdm', 'cas', 'bin', 'a52', 'zip', 'atx', 'car', 'com', 'xex'],
                        'friendlyName' : 'Atari - 5200 (Atari800)'
                        }
                    }
                }
            }
		},
    'Atari 7800' : { 
		'systemNames' : ['Atari 7800', 'Atari7800', 'Atari 7800 ProSystem'],
		'systemIds' : {
			'igdb' : 60,
			'thegamesdb' : 27
			},
		'romExtensions' : ['a78', 'bin'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'prosystem_libretro.dll', #default
                    1 : 'prosystem_libretro.dll', #Stella
                    'prosystem_libretro.dll' : {
                        'coreExtensions' : ['a78', 'bin'],
                        'friendlyName' : 'Atari - 7800 (ProSystem)'
                        }
                    }
                }
            }
		},
    'Atari 800' : { 
		'systemNames' : ['Atari 800', 'Atari 8-bit', 'Atari800', 'Atari8bit'],
		'systemIds' : {
			'igdb' : 64,
			'thegamesdb' : 4943
			},
		'romExtensions' : ['a52', 'atr', 'atx', 'bin', 'cas', 'cdm', 'xex', 'xfd', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'atari800_libretro.dll', #default
                    1 : 'atari800_libretro.dll', #Stella
                    'atari800_libretro.dll' : {
                        'coreExtensions' : ['xfd', 'atr', 'cdm', 'cas', 'bin', 'a52', 'zip', 'atx', 'car', 'com', 'xex'],
                        'friendlyName' : 'Atari - 5200 (Atari800)'
                        }
                    }
                }
            }
		},
    'Atari Jaguar' : { 
		'systemNames' : ['Atari Jaguar', 'Jaguar'],
		'systemIds' : {
			'igdb' : 62,
			'thegamesdb' : 28
			},
		'romExtensions' : ['abs', 'bin', 'cof', 'j64', 'jag', 'prg', 'rom'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'virtualjaguar_libretro.dll', #default
                    1 : 'virtualjaguar_libretro.dll', #Stella
                    'virtualjaguar_libretro.dll' : {
                        'coreExtensions' : ['j64', 'jag', 'rom', 'abs', 'cof', 'bin', 'prg'],
                        'friendlyName' : 'Atari - Jaguar (Virtual Jaguar)'
                        }
                    }
                }
            }
		},
    'Atari Jaguar CD' : { 
		'systemNames' : ['Atari Jaguar CD', 'Jaguar CD'],
		'systemIds' : {
			'igdb' : 62,
			'thegamesdb' : 29
			},
		'romExtensions' : ['abs', 'bin', 'cof', 'j64', 'jag', 'prg', 'rom'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'virtualjaguar_libretro.dll', #default
                    1 : 'virtualjaguar_libretro.dll', #Virtual Jaguar
                    'virtualjaguar_libretro.dll' : {
                        'coreExtensions' : ['j64', 'jag', 'rom', 'abs', 'cof', 'bin', 'prg'],
                        'friendlyName' : 'Atari - Jaguar (Virtual Jaguar)'
                        }
                    }
                }
            }
		},
    'Atari Lynx' : { 
		'systemNames' : ['Atari Lynx', 'Lynx'],
		'systemIds' : {
			'igdb' : 61,
			'thegamesdb' : 4924
			},
		'romExtensions' : ['lnx', 'o'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mednafen_lynx_libretro.dll', #default
                    1 : 'mednafen_lynx_libretro.dll', #Beetle Lynx
                    2 : 'handy_libretro.dll', #Handy
                    'mednafen_lynx_libretro.dll' : {
                        'coreExtensions' : ['lnx', 'o'],
                        'friendlyName' : 'Atari - Lynx (Beetle Lynx)'
                        },
                    'handy_libretro.dll' : {
                        'coreExtensions' : ['lnx', 'o'],
                        'friendlyName' : 'Atari - Lynx (Handy)'
                        }
                    }
                }
            }
		},
    'Atari ST' : { 
		'systemNames' : ['Atari ST', 'Atari ST/STE', 'Atari-ST', 'Atari-STE', 'Atari STE'],
		'systemIds' : {
			'igdb' : 63,
			'thegamesdb' : 4937
			},
		'romExtensions' : ['dim', 'ipf', 'msa', 'st', 'stx', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'hatari_libretro.dll', #default
                    1 : 'hatari_libretro.dll', #Hatari
                    'hatari_libretro.dll' : {
                        'coreExtensions' : ['st', 'msa', 'zip', 'stx', 'dim', 'ipf', 'm3u'],
                        'friendlyName' : 'Atari - ST/STE/TT/Falcon (Hatari)'
                        }
                    }
                }
            }
		},
    'Atari XE' : { 
		'systemNames' : ['Atari XE', 'Atari-XE'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 30
			},
		'romExtensions' : ['a52', 'atr', 'atx', 'bin', 'cas', 'cdm', 'xex', 'xfd', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'atari800_libretro.dll', #default
                    1 : 'atari800_libretro.dll', #Stella
                    'atari800_libretro.dll' : {
                        'coreExtensions' : ['xfd|atr|cdm|cas|bin|a52|zip|atx|car|com|xex'],
                        'friendlyName' : 'Atari - 5200 (Atari800)'
                        }
                    }
                }
            }
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
    'Cave Story Engine' : { 
		'systemNames' : ['Cave Story', 'Cavestory'],
		'systemIds' : {
			'igdb' : 6,
			'thegamesdb' : 1
			},
		'romExtensions' : ['exe'],
		'romType' : 1,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'nxengine_libretro.dll', #default
                    1 : 'nxengine_libretro.dll', #NX Engine
                    'nxengine_libretro.dll' : {
                        'coreExtensions' : ['exe'],
                        'friendlyName' : 'Cave Story (NX Engine)'
                        }
                    }
                }
            }
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
    'ChaiLove Engine' : { 
		'systemNames' : ['ChaiLove', 'Chai'],
		'systemIds' : {
			'igdb' : 6,
			'thegamesdb' : 1
			},
		'romExtensions' : ['chai', 'chailove'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'chailove_libretro.dll', #default
                    1 : 'chailove_libretro.dll', #ChaiLove
                    'chailove_libretro.dll' : {
                        'coreExtensions' : ['chai', 'chailove'],
                        'friendlyName' : 'ChaiLove'
                        }
                    }
                }
            }
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
		'romExtensions' : ['rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sg', 'sc'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'bluemsx_libretro.dll', #default
                    1 : 'bluemsx_libretro.dll', #blueMSX
                    'bluemsx_libretro.dll' : {
                        'coreExtensions' : ['rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sg', 'sc', 'm3u'],
                        'friendlyName' : 'MSX/SVI/ColecoVision/SG-1000 (blueMSX)'
                        }
                    }
                }
            }
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
		'romExtensions' : ['d64', 'd71', 'd80', 'd81', 'd82', 'g64', 'g41', 'x64', 't64', 'tap', 'prg', 'p00', 'crt', 'bin', 'zip', 'gz', 'd6z', 'd7z', 'd8z', 'g6z', 'g4z', 'x6z', 'cmd', 'vfl', 'vsf', 'nib', 'nbz', 'lnx'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'vice_x64_libretro.dll', #default
                    1 : 'frodo_libretro.dll', #Frodo
                    2 : 'vice_x64_libretro.dll', #VICE x64, fast
                    3 : 'vice_x64sc_libretro.dll', #VICE x64, accurate
                    'frodo_libretro.dll' : {
                        'coreExtensions' : ['d64', 't64', 'x64', 'p00', 'lnx', 'zip'],
                        'friendlyName' : 'Commodore - C64 (Frodo)'
                        },
                    'vice_x64_libretro.dll' : {
                        'coreExtensions' : ['d64', 'd71', 'd80', 'd81', 'd82', 'g64', 'g41', 'x64', 't64', 'tap', 'prg', 'p00', 'crt', 'bin', 'zip', 'gz', 'd6z', 'd7z', 'd8z', 'g6z', 'g4z', 'x6z', 'cmd', 'm3u', 'vfl', 'vsf', 'nib', 'nbz'],
                        'friendlyName' : 'Commodore - C64 (VICE x64, fast)'
                        },
                    'vice_x64sc_libretro.dll' : {
                        'coreExtensions' : ['d64', 'd71', 'd80', 'd81', 'd82', 'g64', 'g41', 'x64', 't64', 'tap', 'prg', 'p00', 'crt', 'bin', 'zip', 'gz', 'd6z', 'd7z', 'd8z', 'g6z', 'g4z', 'x6z', 'cmd', 'm3u', 'vfl', 'vsf', 'nib', 'nbz'],
                        'friendlyName' : 'Commodore - C64 (VICE x64sc, accurate)'
                        }
                    }
                }
            }
		},
    'Commodore 64 SuperCPU' : { 
		'systemNames' : ['Commodore 64 SuperCPU', 'C64 SuperCPU'],
		'systemIds' : {
			'igdb' : 15,
			'thegamesdb' : 40
			},
		'romExtensions' : ['d64', 'd71', 'd80', 'd81', 'd82', 'g64', 'g41', 'x64', 't64', 'tap', 'prg', 'p00', 'crt', 'bin', 'zip', 'gz', 'd6z', 'd7z', 'd8z', 'g6z', 'g4z', 'x6z', 'cmd', 'vfl', 'vsf', 'nib', 'nbz', 'lnx'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'vice_xscpu64_libretro.dll', #default
                    1 : 'vice_xscpu64_libretro.dll', #VICE xscpu64
                    'vice_x64sc_libretro.dll' : {
                        'coreExtensions' : ['d64', 'd71', 'd80', 'd81', 'd82', 'g64', 'g41', 'x64', 't64', 'tap', 'prg', 'p00', 'crt', 'bin', 'zip', 'gz', 'd6z', 'd7z', 'd8z', 'g6z', 'g4z', 'x6z', 'cmd', 'm3u', 'vfl', 'vsf', 'nib', 'nbz'],
                        'friendlyName' : 'Commodore - C64 SuperCPU (VICE xscpu64)'
                        }
                    }
                }
            }
		},
    'Commodore 128' : { 
		'systemNames' : ['Commodore 128', 'C128'],
		'systemIds' : {
			'igdb' : 15,
			'thegamesdb' : 4946
			},
		'romExtensions' : ['d64', 'd71', 'd80', 'd81', 'd82', 'g64', 'g41', 'x64', 't64', 'tap', 'prg', 'p00', 'crt', 'bin', 'zip', 'gz', 'd6z', 'd7z', 'd8z', 'g6z', 'g4z', 'x6z', 'cmd', 'vfl', 'vsf', 'nib', 'nbz'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'vice_x128_libretro.dll', #default
                    1 : 'vice_x128_libretro.dll', #VICE x128
                    'vice_x128_libretro.dll' : {
                        'coreExtensions' : ['d64', 'd71', 'd80', 'd81', 'd82', 'g64', 'g41', 'x64', 't64', 'tap', 'prg', 'p00', 'crt', 'bin', 'zip', 'gz', 'd6z', 'd7z', 'd8z', 'g6z', 'g4z', 'x6z', 'cmd', 'm3u', 'vfl', 'vsf', 'nib', 'nbz'],
                        'friendlyName' : 'Commodore - C128 (VICE x128)'
                        }
                    }
                }
            }
		},
    'Commodore Amiga' : { 
		'systemNames' : ['Commodore Amiga', 'Amiga'],
		'systemIds' : {
			'igdb' : 16,
			'thegamesdb' : 4911
			},
		'romExtensions' : ['adf', 'adz', 'dms', 'fdi', 'ipf', 'hdf', 'hdz', 'lha', 'slave', 'info', 'cue', 'ccd', 'nrg', 'mds', 'iso', 'chd', 'uae', 'zip', '7z'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'puae_libretro.dll', #default
                    1 : 'puae_libretro.dll', #NX Engine
                    'puae_libretro.dll' : {
                        'coreExtensions' : ['adf', 'adz', 'dms', 'fdi', 'ipf', 'hdf', 'hdz', 'lha', 'slave', 'info', 'cue', 'ccd', 'nrg', 'mds', 'iso', 'chd', 'uae', 'm3u', 'zip', '7z'],
                        'friendlyName' : 'Commodore - Amiga (PUAE)'
                        }
                    }
                }
            }
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
		'romExtensions' : ['d64', 'd71', 'd80', 'd81', 'd82', 'g64', 'g41', 'x64', 't64', 'tap', 'prg', 'p00', 'crt', 'bin', 'zip', 'gz', 'd6z', 'd7z', 'd8z', 'g6z', 'g4z', 'x6z', 'cmd', 'vfl', 'vsf', 'nib', 'nbz'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'vice_xpet_libretro.dll', #default
                    1 : 'vice_xpet_libretro.dll', #VICE xpet
                    'vice_xpet_libretro.dll' : {
                        'coreExtensions' : ['d64', 'd71', 'd80', 'd81', 'd82', 'g64', 'g41', 'x64', 't64', 'tap', 'prg', 'p00', 'crt', 'bin', 'zip', 'gz', 'd6z', 'd7z', 'd8z', 'g6z', 'g4z', 'x6z', 'cmd', 'm3u', 'vfl', 'vsf', 'nib', 'nbz'],
                        'friendlyName' : 'Commodore - C128 (VICE xpet)'
                        }
                    }
                }
            }
		},
    'Commodore Plus 4' : { 
		'systemNames' : ['Commodore Plus 4', 'Commodore Plus/4', 'C+4'],
		'systemIds' : {
			'igdb' : 94,
			'thegamesdb' : None
			},
		'romExtensions' : ['d64', 'd71', 'd80', 'd81', 'd82', 'g64', 'g41', 'x64', 't64', 'tap', 'prg', 'p00', 'crt', 'bin', 'zip', 'gz', 'd6z', 'd7z', 'd8z', 'g6z', 'g4z', 'x6z', 'cmd', 'vfl', 'vsf', 'nib', 'nbz'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'vice_xplus4_libretro.dll', #default
                    1 : 'vice_xplus4_libretro.dll', #VICE xplus4
                    'vice_xplus4_libretro.dll' : {
                        'coreExtensions' : ['d64', 'd71', 'd80', 'd81', 'd82', 'g64', 'g41', 'x64', 't64', 'tap', 'prg', 'p00', 'crt', 'bin', 'zip', 'gz', 'd6z', 'd7z', 'd8z', 'g6z', 'g4z', 'x6z', 'cmd', 'm3u', 'vfl', 'vsf', 'nib', 'nbz'],
                        'friendlyName' : 'Commodore - PLUS/4 (VICE xplus4)'
                        }
                    }
                }
            }
		},
    'Commodore VIC-20' : { 
		'systemNames' : ['Commodore VIC-20', 'vic-20'],
		'systemIds' : {
			'igdb' : 71,
			'thegamesdb' : 4945
			},
		'romExtensions' : ['d64', 'd71', 'd80', 'd81', 'd82', 'g64', 'g41', 'x64', 't64', 'tap', 'prg', 'p00', 'crt', 'bin', 'zip', 'gz', 'd6z', 'd7z', 'd8z', 'g6z', 'g4z', 'x6z', 'cmd', 'vfl', 'vsf', 'nib', 'nbz'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'vice_xvic_libretro.dll', #default
                    1 : 'vice_xvic_libretro.dll', #VICE xvic
                    'vice_xvic_libretro.dll' : {
                        'coreExtensions' : ['d64', 'd71', 'd80', 'd81', 'd82', 'g64', 'g41', 'x64', 't64', 'tap', 'prg', 'p00', 'crt', 'bin', 'zip', 'gz', 'd6z', 'd7z', 'd8z', 'g6z', 'g4z', 'x6z', 'cmd', 'm3u', 'vfl', 'vsf', 'nib', 'nbz'],
                        'friendlyName' : 'Commodore - VIC-20 (VICE xvic)'
                        }
                    }
                }
            }
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
    'Doom Engine' : { 
		'systemNames' : ['Doom', 'Doom Engine'],
		'systemIds' : {
			'igdb' : 6,
			'thegamesdb' : 1
			},
		'romExtensions' : ['wad'],
		'romType' : 1,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'prboom_libretro.dll', #default
                    1 : 'prboom_libretro.dll', #PrBoom
                    'prboom_libretro.dll' : {
                        'coreExtensions' : ['iwad', 'pwad', 'wad'],
                        'friendlyName' : 'Doom (PrBoom)'
                        }
                    }
                }
            }
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
		'systemNames' : ['Fairchild Channel F', 'Channel F'],
		'systemIds' : {
			'igdb' : 127,
			'thegamesdb' : 4928
			},
		'romExtensions' : ['bin', 'chf'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'freechaf_libretro.dll', #default
                    1 : 'freechaf_libretro.dll', #FreeChaF
                    'freechaf_libretro.dll' : {
                        'coreExtensions' : ['bin', 'chf'],
                        'friendlyName' : 'Fairchild ChannelF (FreeChaF)'
                        }
                    }
                }
            }
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
		'romExtensions' : ['bin', 'vec'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'vecx_libretro.dll', #default
                    1 : 'vecx_libretro.dll', #vecx
                    'vecx_libretro.dll' : {
                        'coreExtensions' : ['bin', 'vec'],
                        'friendlyName' : 'GCE - Vectrex (vecx)'
                        }
                    }
                }
            }
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
    'Lua Engine' : { 
		'systemNames' : ['Lua Engine', 'Lua', 'Lutro'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : None
			},
		'romExtensions' : ['lutro', 'lua'],
		'romType' : 1,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'lutro_libretro.dll', #default
                    1 : 'lutro_libretro.dll', #Lutro
                    'lutro_libretro.dll' : {
                        'coreExtensions' : ['lutro', 'lua'],
                        'friendlyName' : 'Lua Engine (Lutro)'
                        }
                    }
                }
            }
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
		'romExtensions' : ['bin'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'o2em_libretro.dll', #default
                    1 : 'o2em_libretro.dll', #O2EM
                    'o2em_libretro.dll' : {
                        'coreExtensions' : ['bin'],
                        'friendlyName' : 'Magnavox - Odyssey2 / Phillips Videopac+ (O2EM)'
                        }
                    }
                }
            }
		},
    'Mattel Intellivision' : { 
		'systemNames' : ['Mattel Intellivision', 'Intellivision'],
		'systemIds' : {
			'igdb' : 67,
			'thegamesdb' : 32
			},
		'romExtensions' : ['int', 'bin', 'rom'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'freeintv_libretro.dll', #default
                    1 : 'freeintv_libretro.dll', #FreeIntv
                    'freeintv_libretro.dll' : {
                        'coreExtensions' : ['int', 'bin', 'rom'],
                        'friendlyName' : 'Mattel - Intellivision (FreeIntv)'
                        }
                    }
                }
            }
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
		'romExtensions' : ['zip', 'dosz', 'exe', 'conf', 'com', 'bat', 'iso', 'cue', 'ins', 'img', 'ima', 'vhd', 'm3u8'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'dosbox_libretro.dll', #default
                    1 : 'dosbox_libretro.dll', #DOSBox
                    2 : 'dosbox_core_libretro.dll', #DOSBox-core
                    3 : 'dosbox_pure_libretro.dll', #DOSBox-Pure
                    4 : 'dosbox_svn_ce_libretro.dll', #DOSBox-SVN CE
                    3 : 'dosbox_svn_libretro.dll', #DOSBox-SVN
                    'dosbox_libretro.dll' : {
                        'coreExtensions' : ['exe', 'com', 'bat', 'conf'],
                        'friendlyName' : 'DOS (DOSBox)'
                        },
                    'dosbox_core_libretro.dll' : {
                        'coreExtensions' : ['exe', 'com', 'bat', 'conf', 'cue', 'iso'],
                        'friendlyName' : 'DOS (DOSBox-core)'
                        },
                    'dosbox_pure_libretro.dll' : {
                        'coreExtensions' : ['zip', 'dosz', 'exe', 'com', 'bat', 'iso', 'cue', 'ins', 'img', 'ima', 'vhd', 'm3u', 'm3u8'],
                        'friendlyName' : 'DOS (DOSBox-Pure)'
                        },
                    'dosbox_svn_ce_libretro.dll' : {
                        'coreExtensions' : ['exe', 'com', 'bat', 'conf', 'cue', 'iso'],
                        'friendlyName' : 'DOS (DOSBox-SVN CE)'
                        },
                    'dosbox_svn_libretro.dll' : {
                        'coreExtensions' : ['exe', 'com', 'bat', 'conf', 'cue', 'iso'],
                        'friendlyName' : 'DOS (DOSBox-SVN)'
                        }
                    }
                }
            }
		},
    'Microsoft MSX' : { 
		'systemNames' : ['Microsoft MSX', 'MSX'],
		'systemIds' : {
			'igdb' : 27,
			'thegamesdb' : 4929
			},
		'romExtensions' : ['rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sg', 'sc'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'bluemsx_libretro.dll', #default
                    1 : 'bluemsx_libretro.dll', #blueMSX
                    2 : 'fmsx_libretro.dll', #FreeIntv
                    'bluemsx_libretro.dll' : {
                        'coreExtensions' : ['rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sg', 'sc', 'm3u'],
                        'friendlyName' : 'MSX/SVI/ColecoVision/SG-1000 (blueMSX)'
                        },
                    'fmsx_libretro.dll' : {
                        'coreExtensions' : ['rom', 'mx1', 'mx2', 'dsk', 'cas'],
                        'friendlyName' : 'Microsoft - MSX (fMSX)'
                        }
                    }
                }
            }
		},
    'Microsoft MSX2' : { 
		'systemNames' : ['Microsoft MSX2', 'MSX2'],
		'systemIds' : {
			'igdb' : 53,
			'thegamesdb' : 4929
			},
		'romExtensions' : ['rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sg', 'sc'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'bluemsx_libretro.dll', #default
                    1 : 'bluemsx_libretro.dll', #blueMSX
                    2 : 'fmsx_libretro.dll', #FreeIntv
                    'bluemsx_libretro.dll' : {
                        'coreExtensions' : ['rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sg', 'sc', 'm3u'],
                        'friendlyName' : 'MSX/SVI/ColecoVision/SG-1000 (blueMSX)'
                        },
                    'fmsx_libretro.dll' : {
                        'coreExtensions' : ['rom', 'mx1', 'mx2', 'dsk', 'cas'],
                        'friendlyName' : 'Microsoft - MSX (fMSX)'
                        }
                    }
                }
            }
		},
    'Microsoft MSX2 PLUS' : { 
		'systemNames' : ['Microsoft MSX2 PLUS', 'Microsoft MSX2+', 'MSX2+'],
		'systemIds' : {
			'igdb' : 53,
			'thegamesdb' : 4929
			},
		'romExtensions' : ['rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sg', 'sc'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'bluemsx_libretro.dll', #default
                    1 : 'bluemsx_libretro.dll', #blueMSX
                    2 : 'fmsx_libretro.dll', #FreeIntv
                    'bluemsx_libretro.dll' : {
                        'coreExtensions' : ['rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sg', 'sc', 'm3u'],
                        'friendlyName' : 'MSX/SVI/ColecoVision/SG-1000 (blueMSX)'
                        },
                    'fmsx_libretro.dll' : {
                        'coreExtensions' : ['rom', 'mx1', 'mx2', 'dsk', 'cas'],
                        'friendlyName' : 'Microsoft - MSX (fMSX)'
                        }
                    }
                }
            }
		},
    'Microsoft MSX TurboR' : { 
		'systemNames' : ['Microsoft MSX TurboR', 'MSX TurboR'],
		'systemIds' : {
			'igdb' : 53,
			'thegamesdb' : 4929
			},
		'romExtensions' : ['rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sg', 'sc'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'bluemsx_libretro.dll', #default
                    1 : 'bluemsx_libretro.dll', #blueMSX
                    2 : 'fmsx_libretro.dll', #FreeIntv
                    'bluemsx_libretro.dll' : {
                        'coreExtensions' : ['rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sg', 'sc', 'm3u'],
                        'friendlyName' : 'MSX/SVI/ColecoVision/SG-1000 (blueMSX)'
                        },
                    'fmsx_libretro.dll' : {
                        'coreExtensions' : ['rom', 'mx1', 'mx2', 'dsk', 'cas'],
                        'friendlyName' : 'Microsoft - MSX (fMSX)'
                        }
                    }
                }
            }
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
		'systemNames' : ['NEC PC-8801', 'PC-8801', 'PC-88', 'PC-8000', 'PC-8800'],
		'systemIds' : {
			'igdb' : 125,
			'thegamesdb' : 4933
			},
		'romExtensions' : ['d88', 'u88'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'quasi88_libretro.dll', #default
                    1 : 'quasi88_libretro.dll', #QUASI88
                    'quasi88_libretro.dll' : {
                        'coreExtensions' : ['d88', 'u88', 'm3u'],
                        'friendlyName' : 'NEC - PC-8000 / PC-8800 series (QUASI88)'
                        }
                    }
                }
            }
		},
    'NEC PC-9801' : { 
		'systemNames' : ['NEC PC-9801', 'PC-9801', 'PC-98'],
		'systemIds' : {
			'igdb' : 149,
			'thegamesdb' : 4934
			},
		'romExtensions' : ['d98', 'zip', '98d', 'fdi', 'fdd', '2hd', 'tfd', 'd88', '88d', 'hdm', 'xdf', 'dup', 'cmd', 'hdi', 'thd', 'nhd', 'hdd'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'nekop2_libretro.dll', #default
                    1 : 'nekop2_libretro.dll', #Neko Project II
                    2 : 'np2kai_libretro.dll', #Neko Project II Kai
                    'nekop2_libretro.dll' : {
                        'coreExtensions' : ['d98', 'zip', '98d', 'fdi', 'fdd', '2hd', 'tfd', 'd88', '88d', 'hdm', 'xdf', 'dup', 'cmd', 'hdi', 'thd', 'nhd', 'hdd'],
                        'friendlyName' : 'NEC - PC-98 (Neko Project II)'
                        },
                    'np2kai_libretro.dll' : {
                        'coreExtensions' : ['d98', 'zip', '98d', 'fdi', 'fdd', '2hd', 'tfd', 'd88', '88d', 'hdm', 'xdf', 'dup', 'cmd', 'hdi', 'thd', 'nhd', 'hdd', 'hdn'],
                        'friendlyName' : 'NEC - PC-98 (Neko Project II Kai)'
                        }
                    }
                }
            }
		},
    'NEC PC-FX' : { 
		'systemNames' : ['NEC PC-FX', 'PC-FX'],
		'systemIds' : {
			'igdb' : 274,
			'thegamesdb' : 4930
			},
		'romExtensions' : ['cue', 'ccd', 'toc', 'chd'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mednafen_pcfx_libretro.dll', #default
                    1 : 'mednafen_pcfx_libretro.dll', #Beetle PC-FX
                    'mednafen_pcfx_libretro.dll' : {
                        'coreExtensions' : ['cue', 'ccd', 'toc', 'chd'],
                        'friendlyName' : 'NEC - PC-FX (Beetle PC-FX)'
                        }
                    }
                }
            }
		},
    'NEC PC Engine' : { 
		'systemNames' : ['NEC PC Engine', 'PC Engine'],
		'systemIds' : {
			'igdb' : 86,
			'thegamesdb' : 34
			},
		'romExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'chd', 'sgx'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mednafen_pce_libretro.dll', #default
                    1 : 'mednafen_pce_libretro.dll', #Beetle PCE
                    2 : 'mednafen_pce_fast_libretro.dll', #Beetle PCE FAST
                    3 : 'mednafen_supergrafx_libretro.dll', #Beetle SuperGrafx
                    'mednafen_pce_libretro.dll' : {
                        'coreExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'bin', 'chd'],
                        'friendlyName' : 'NEC - PC Engine / SuperGrafx / CD (Beetle PCE)'
                        },
                    'mednafen_pce_fast_libretro.dll' : {
                        'coreExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'bin', 'chd'],
                        'friendlyName' : 'NEC - PC Engine / CD (Beetle PCE FAST)'
                        },
                    'mednafen_supergrafx_libretro.dll' : {
                        'coreExtensions' : ['pce', 'sgx', 'cue', 'ccd', 'chd'],
                        'friendlyName' : 'NEC - PC Engine SuperGrafx (Beetle SuperGrafx)'
                        }
                    }
                }
            }
		},
    'NEC PC Engine CD' : { 
		'systemNames' : ['NEC PC Engine CD', 'PC Engine CD'],
		'systemIds' : {
			'igdb' : 150,
			'thegamesdb' : 4955
			},
		'romExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'chd', 'sgx'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mednafen_pce_libretro.dll', #default
                    1 : 'mednafen_pce_libretro.dll', #Beetle PCE
                    2 : 'mednafen_pce_fast_libretro.dll', #Beetle PCE FAST
                    3 : 'mednafen_supergrafx_libretro.dll', #Beetle SuperGrafx
                    'mednafen_pce_libretro.dll' : {
                        'coreExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'bin', 'chd'],
                        'friendlyName' : 'NEC - PC Engine / SuperGrafx / CD (Beetle PCE)'
                        },
                    'mednafen_pce_fast_libretro.dll' : {
                        'coreExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'bin', 'chd'],
                        'friendlyName' : 'NEC - PC Engine / CD (Beetle PCE FAST)'
                        },
                    'mednafen_supergrafx_libretro.dll' : {
                        'coreExtensions' : ['pce', 'sgx', 'cue', 'ccd', 'chd'],
                        'friendlyName' : 'NEC - PC Engine SuperGrafx (Beetle SuperGrafx)'
                        }
                    }
                }
            }
		},
    'NEC PC Engine SuperGrafx' : { 
		'systemNames' : ['NEC PC Engine SuperGrafx', 'PC Engine SuperGrafx'],
		'systemIds' : {
			'igdb' : 128,
			'thegamesdb' : None
			},
		'romExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'chd', 'sgx'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mednafen_pce_libretro.dll', #default
                    1 : 'mednafen_pce_libretro.dll', #Beetle PCE
                    2 : 'mednafen_supergrafx_libretro.dll', #Beetle SuperGrafx
                    'mednafen_pce_libretro.dll' : {
                        'coreExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'bin', 'chd'],
                        'friendlyName' : 'NEC - PC Engine / SuperGrafx / CD (Beetle PCE)'
                        },
                    'mednafen_pce_fast_libretro.dll' : {
                        'coreExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'bin', 'chd'],
                        'friendlyName' : 'NEC - PC Engine / CD (Beetle PCE FAST)'
                        },
                    'mednafen_supergrafx_libretro.dll' : {
                        'coreExtensions' : ['pce', 'sgx', 'cue', 'ccd', 'chd'],
                        'friendlyName' : 'NEC - PC Engine SuperGrafx (Beetle SuperGrafx)'
                        }
                    }
                }
            }
		},
    'NEC TurboGrafx-16' : { 
		'systemNames' : ['NEC TurboGrafx-16', 'TurboGrafx-16', 'turbografx16'],
		'systemIds' : {
			'igdb' : 86,
			'thegamesdb' : 34
			},
		'romExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'chd', 'sgx'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mednafen_pce_libretro.dll', #default
                    1 : 'mednafen_pce_libretro.dll', #Beetle PCE
                    2 : 'mednafen_pce_fast_libretro.dll', #Beetle PCE FAST
                    3 : 'mednafen_supergrafx_libretro.dll', #Beetle SuperGrafx
                    'mednafen_pce_libretro.dll' : {
                        'coreExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'bin', 'chd'],
                        'friendlyName' : 'NEC - PC Engine / SuperGrafx / CD (Beetle PCE)'
                        },
                    'mednafen_pce_fast_libretro.dll' : {
                        'coreExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'bin', 'chd'],
                        'friendlyName' : 'NEC - PC Engine / CD (Beetle PCE FAST)'
                        },
                    'mednafen_supergrafx_libretro.dll' : {
                        'coreExtensions' : ['pce', 'sgx', 'cue', 'ccd', 'chd'],
                        'friendlyName' : 'NEC - PC Engine SuperGrafx (Beetle SuperGrafx)'
                        }
                    }
                }
            }
		},
    'NEC TurboGrafx-CD' : { 
		'systemNames' : ['NEC TurboGrafx-CD', 'TurboGrafx-CD', 'NEC TurboGrafx-CD32', 'TurboGrafx-CD32'],
		'systemIds' : {
			'igdb' : 150,
			'thegamesdb' : 4955
			},
		'romExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'chd', 'sgx'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mednafen_pce_libretro.dll', #default
                    1 : 'mednafen_pce_libretro.dll', #Beetle PCE
                    2 : 'mednafen_pce_fast_libretro.dll', #Beetle PCE FAST
                    3 : 'mednafen_supergrafx_libretro.dll', #Beetle SuperGrafx
                    'mednafen_pce_libretro.dll' : {
                        'coreExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'bin', 'chd'],
                        'friendlyName' : 'NEC - PC Engine / SuperGrafx / CD (Beetle PCE)'
                        },
                    'mednafen_pce_fast_libretro.dll' : {
                        'coreExtensions' : ['pce', 'cue', 'ccd', 'iso', 'img', 'bin', 'chd'],
                        'friendlyName' : 'NEC - PC Engine / CD (Beetle PCE FAST)'
                        },
                    'mednafen_supergrafx_libretro.dll' : {
                        'coreExtensions' : ['pce', 'sgx', 'cue', 'ccd', 'chd'],
                        'friendlyName' : 'NEC - PC Engine SuperGrafx (Beetle SuperGrafx)'
                        }
                    }
                }
            }
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
		'romExtensions' : ['3ds', '3dsx', 'elf', 'axf', 'cci', 'cxi', 'app'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'citra_libretro.dll', #default
                    1 : 'citra_libretro.dll', #Citra
                    2 : 'citra_canary_libretro.dll', #Citra Canary/Experimental
                    'citra_libretro.dll' : {
                        'coreExtensions' : ['3ds', '3dsx', 'elf', 'axf', 'cci', 'cxi', 'app'],
                        'friendlyName' : 'Nintendo - 3DS (Citra)'
                        },
                    'citra_canary_libretro.dll' : {
                        'coreExtensions' : ['3ds', '3dsx', 'elf', 'axf', 'cci', 'cxi', 'app'],
                        'friendlyName' : 'Nintendo - 3DS (Citra Canary/Experimental)'
                        }
                    }
                }
            }
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
    'Nintendo Game and Watch' : { 
		'systemNames' : ['Nintendo Game and Watch', 'Nintendo Game & Watch', 'Game & Watch', 'Game and Watch', 'Tricotronic'],
		'systemIds' : {
			'igdb' : 307,
			'thegamesdb' : 4950
			},
		'romExtensions' : ['mgw'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'gw_libretro.dll', #default
                    1 : 'gw_libretro.dll', #GW
                    'gw_libretro.dll' : {
                        'coreExtensions' : ['mgw'],
                        'friendlyName' : 'Handheld Electronic (GW)'
                        }
                    }
                }
            }
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
    'OutRun Engine' : { 
		'systemNames' : ['Cannonball'],
		'systemIds' : {
			'igdb' : 13,
			'thegamesdb' : 1
			},
		'romExtensions' : ['game'],
		'romType' : 1,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'cannonball_libretro.dll', #default
                    1 : 'cannonball_libretro.dll', #Cannonball
                    'cannonball_libretro.dll' : {
                        'coreExtensions' : ['game', '88'],
                        'friendlyName' : 'Cannonball'
                        }
                    }
                }
            }
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
		'romExtensions' : ['rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sg', 'sc'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'bluemsx_libretro.dll', #default
                    1 : 'bluemsx_libretro.dll', #blueMSX
                    'bluemsx_libretro.dll' : {
                        'coreExtensions' : ['rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sg', 'sc', 'm3u'],
                        'friendlyName' : 'MSX/SVI/ColecoVision/SG-1000 (blueMSX)'
                        }
                    }
                }
            }
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
		'romExtensions' : ['cbn', 'ccd', 'chd', 'cue', 'exe', 'img', 'mdf', 'pbp', 'toc'], #don't include bin during scanning
		'romType' : 0,
        'multiDisk' : True, #creates and adds m3u
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'duckstation_libretro.dll', #default
                    1 : 'mednafen_psx_libretro.dll', #Beetle PSX
                    2 : 'mednafen_psx_hw_libretro.dll', #Beetle PSX HW
                    3 : 'duckstation_libretro.dll', #SwanStation
                    4 : 'pcsx_rearmed_libretro.dll', #PCSX ReARMed
                    'mednafen_psx_libretro.dll' : {
                        'coreExtensions' : ['cue', 'toc', 'm3u', 'ccd', 'exe', 'pbp', 'chd'],
                        'friendlyName' : 'Sony - Playstation (Beetle PSX)'
                        },
                    'mednafen_psx_hw_libretro.dll' : {
                        'coreExtensions' : ['cue', 'toc', 'm3u', 'ccd', 'exe', 'pbp', 'chd'],
                        'friendlyName' : 'Sony - Playstation (Beetle PSX HW)'
                        },
                    'duckstation_libretro.dll' : {
                        'coreExtensions' : ['cue', 'bin', 'img', 'chd', 'm3u'],
                        'friendlyName' : 'Sony - Playstation (SwanStation)'
                        },
                    'pcsx_rearmed_libretro.dll' : {
                        'coreExtensions' : ['bin', 'cue', 'img', 'mdf', 'pbp', 'toc', 'cbn', 'm3u', 'ccd', 'chd'],
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
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'pcsx2_libretro.dll', #default
                    1 : 'pcsx2_libretro.dll', #Beetle Cygne
                    'pcsx2_libretro.dll' : {
                        'coreExtensions' : ['ciso', 'cue', 'elf', 'iso'],
                        'friendlyName' : 'Sony - PlayStation 2 (PCSX2)'
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
		'romExtensions' : ['elf', 'iso', 'cso', 'prx', 'pbp'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'ppsspp_libretro.dll', #default
                    1 : 'ppsspp_libretro.dll', #Beetle Cygne
                    'ppsspp_libretro.dll' : {
                        'coreExtensions' : ['elf', 'iso', 'cso', 'prx', 'pbp'],
                        'friendlyName' : 'Sony - PlayStation Portable (PPSSPP)'
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
		'romExtensions' : ['pc2', 'ws', 'wsc'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mednafen_wswan_libretro.dll', #default
                    1 : 'mednafen_wswan_libretro.dll', #Beetle Cygne
                    'mednafen_wswan_libretro.dll' : {
                        'coreExtensions' : ['ws', 'wsc', 'pc2'],
                        'friendlyName' : 'Bandai - WonderSwan/Color (Beetle Cygne)'
                        }
                    }
                }
            }
		},
    'WonderSwan Color' : { 
		'systemNames' : ['WonderSwan Color', 'Bandai WonderSwan Color'],
		'systemIds' : {
			'igdb' : 123,
			'thegamesdb' : 4926
			},
		'romExtensions' : ['pc2', 'ws', 'wsc'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mednafen_wswan_libretro.dll', #default
                    1 : 'mednafen_wswan_libretro.dll', #Beetle Cygne
                    'mednafen_wswan_libretro.dll' : {
                        'coreExtensions' : ['ws', 'wsc', 'pc2'],
                        'friendlyName' : 'Bandai - WonderSwan/Color (Beetle Cygne)'
                        }
                    }
                }
            }
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
