# -*- coding: utf-8 -*-
#dictionaries
dSiteShortNames1 = {
    0 : 'igdb'
    }
                   
dSiteShortNames2 = {
    'igdb' : 0
   }

dict_enum_agent_map = { #for metadata agent
    'SearchSite' : { #make sure keys are lowercase
        'igdb' : 0
       },
    'PreferredRatingSystem' : {
        'ESRB' : {
            'igdb' : 1
            },
        'PEGI' : {
            'igdb' : 2
            }
        },
    'ThemeSource' : {
        'none' : '0',
        'Local' : '1'
        }
    }

dict_enum_settings_map = { #for retroarcher script
    'FfmpegEncoder' : { #used by retroarcher.py so numbers first
        '0' : 'h264_nvenc',
        '1' : 'h264_qsv',
        '2' : 'h264_videotoolbox',
        '3' : 'libx264',
        '4' : 'mpeg2_qsv',
        '5' : 'mpeg2video'
        },
    'GameStreamApp' : { #used by retroarcher.py so numbers first
        '0' : 'Moonlight'
        },
    'GameStreamHost' : { #used by retroarcher.py so numbers first
        '0' : 'GeForce Experience',
        '1' : 'Open-Stream',
        '2' : 'Sunshine'
        },
    'LogLevel' : {
        '0' : 0,
        '1' : 10,
        '2' : 20,
        '3' : 30,
        '4' : 40,
        '5' : 50
        }
    }

dDefaultSettings = {
	'dir_SourceRomDirectory' : '',
	
	'enum_FfmpegEncoder' : '0', #h264_nvenc
	'int_FfmpegLength' : '30',
	'int_FfmpegTextSize' : '24',
	'str_FfmpegTextColor' : 'white',
	'str_FfmpegTextX' : '20',
	'str_FfmpegTextY' : '20',
	'bool_FfmpegTextBox' : 'True',
	'str_FfmpegTextBoxColor' : 'black@0.5',
	'str_FfmpegTextBoxBorder' : '5',
	'int_BufferSize' : '65536',
	
	'enum_SearchSite' : '0', #IGDB
    'url_IgdbCreds' : 'https://raw.githubusercontent.com/RetroArcher/RetroArcher.proxy/main/igdb.json',

	'str_YouTubeApiKey' : 'AIzaSyCYss6qpH_Ru6XHSiuUTEJU6r5G63IDJ-4',
	
	'enum_PreferredRatingSystem' : '0', #ESRB
	
	'bool_PlatformAsCollection' : 'True',
	
	'enum_ThemesSource' : '1', #Local
	'dir_SourceThemeDirectory' : '',
    
    'bool_GetExtraObject' : 'True',
	
	'str_MoonlightAppName' : 'Desktop',
    'str_MoonlightAppId' : '',
    'str_MoonlightPcUuid' : '',
    'int_PortScanThreads' : '200',
	
	'bool_GameStreamEnabled' : 'False',
	'url_GameStreamServerAddress' : 'http://localhost:47989/serverinfo',
	'list_GameStreamWhiteList' : '',
	'list_GameStreamBlackList' : '',
	'enum_GameStreamApp' : '0', #moonlight
	'enum_GameStreamHost' : '0', #GeForce Experience
	
    'enum_LogLevel' : '1',
    
	'url_PlexServer' : 'http://localhost:32400',
	'str_PlexToken' : '',
    
    'dir_app_retroarch' : '',
    'str_binary_retroarch' : 'retroarch',
    'dir_app_cemu' : '',
    'str_binary_cemu' : 'Cemu',
    'dir_app_rpcs3' : '',
    'str_binary_rpcs3' : 'rpcs3',
	
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
	'scanner_magnavox_odyssey_2' : 'True',
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
	'scanner_nintendo_ds' : 'True',
	'scanner_nintendo_entertainment_system' : 'True',
	'scanner_nintendo_famicom_disk_system' : 'True',
	'scanner_nintendo_family_computer' : 'True',
	'scanner_nintendo_game_boy' : 'True',
	'scanner_nintendo_game_boy_advance' : 'True',
	'scanner_nintendo_game_boy_color' : 'True',
	'scanner_nintendo_gamecube' : 'True',
	'scanner_nintendo_game_and_watch' : 'True',
	'scanner_nintendo_pokemon_mini' : 'True',
	'scanner_nintendo_super_famicom' : 'True',
	'scanner_nintendo_super_famicom_satellaview' : 'True',
	'scanner_nintendo_virtual_boy' : 'True',
	'scanner_nintendo_wii' : 'True',
	'scanner_nintendo_wii_u' : 'True',
	'scanner_outrun_engine' : 'True',
	'scanner_quake_1_engine' : 'True',
	'scanner_quake_ii_engine' : 'True',
	'scanner_quake_iii_engine' : 'True',
	'scanner_rick_dangerous_engine' : 'True',
	'scanner_rpg_maker' : 'True',
	'scanner_scummvm' : 'True',
	'scanner_sega_32x' : 'True',
	'scanner_sega_cd' : 'True',
	'scanner_sega_dreamcast' : 'True',
	'scanner_sega_game_gear' : 'True',
	'scanner_sega_genesis' : 'True',
	'scanner_sega_master_system' : 'True',
	'scanner_sega_mega_drive' : 'True',
	'scanner_sega_naomi' : 'True',
	'scanner_sega_pico' : 'True',
	'scanner_sega_saturn' : 'True',
	'scanner_sega_sg-1000' : 'True',
	'scanner_sega_st-v' : 'True',
	'scanner_sharp_x1' : 'True',
	'scanner_sharp_x68000' : 'True',
	'scanner_sinclair_zx_81' : 'True',
	'scanner_sinclair_zx_spectrum' : 'True',
	'scanner_snk_neo_geo_cd' : 'True',
	'scanner_snk_neo_geo_pocket' : 'True',
	'scanner_snk_neo_geo_pocket_color' : 'True',
	'scanner_sony_playstation' : 'True',
	'scanner_sony_playstation_2' : 'True',
	'scanner_sony_playstation_3' : 'True',
	'scanner_sony_psp' : 'True',
	'scanner_star_trek_voyager_engine' : 'True',
	'scanner_super_nintendo_entertainment_system' : 'True',
	'scanner_tapwave_zodiac' : 'True',
	'scanner_thomson_mo5' : 'True',
	'scanner_tomb_raider_classic_engine' : 'True',
	'scanner_wolfenstein_3d_engine' : 'True',
	'scanner_wonderswan' : 'True',
	'scanner_wonderswan_color' : 'True'
}

dPlatformMapping = {
    '1292 Advanced Programmable Video System' : {
        'systemNames' : ['1292 Advanced Programmable Video System'],
        'systemIds' : {
            'igdb' : 139,
            'thegamesdb' : None
            },
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Entex Select-A-Game' : { 
		'systemNames' : ['Entex Select-A-Game'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4973
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['n64', 'v64', 'z64', 'bin', 'u1', 'ndd', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mupen64plus_next_libretro.dll', #default
                    1 : 'mupen64plus_next_libretro.dll', #Mupen64Plus-Next
                    2 : 'mupen64plus_next_gles3_libretro.dll', #Mupen64Plus-Next GLES3
                    3 : 'parrallel_libretro.dll', #ParaLLEl N64
                    'mupen64plus_next_libretro.dll' : {
                        'coreExtensions' : ['n64', 'v64', 'z64', 'bin', 'u1'],
                        'friendlyName' : 'Nintendo - Nintendo 64 (Mupen64Plus-Next)'
                        },
                    'mupen64plus_next_gles3_libretro.dll' : {
                        'coreExtensions' : ['n64', 'v64', 'z64', 'bin', 'u1'],
                        'friendlyName' : 'Nintendo - Nintendo 64 (Mupen64Plus-Next GLES3)'
                        },
                    'parrallel_libretro.dll' : {
                        'coreExtensions' : ['n64', 'v64', 'z64', 'bin', 'u1', 'ndd'],
                        'friendlyName' : 'Nintendo - Nintendo 64 (ParaLLEl N64)'
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
        'libraryType' : 'Games',
		'romExtensions' : ['nds', 'bin'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'desmume2015_libretro.dll', #default
                    1 : 'desmume2015_libretro.dll', #DeSmuME 2015
                    2 : 'desmume_libretro.dll', #DeSmuME
                    3 : 'melonds_libretro.dll', #melonDS
                    'desmume2015_libretro.dll' : {
                        'coreExtensions' : ['nds', 'bin'],
                        'friendlyName' : 'Nintendo - DS (DeSmuME 2015)'
                        },
                    'desmume_libretro.dll' : {
                        'coreExtensions' : ['nds', 'bin'],
                        'friendlyName' : 'Nintendo - DS (DeSmuME)'
                        },
                    'melonds_libretro.dll' : {
                        'coreExtensions' : ['nds'],
                        'friendlyName' : 'Nintendo - DS (melonDS)'
                        }
                    }
                }
            }
		},
    'Nintendo DSi' : { 
		'systemNames' : ['Nintendo DSi'],
		'systemIds' : {
			'igdb' : 159,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['nes', 'fds', 'unf', 'unif', 'bin', 'rom', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'fceumm_libretro.dll', #default
                    1 : 'emux_nes_libretro.dll', #Emux NES
                    2 : 'fceumm_libretro.dll', #FCEUmm
                    3 : 'mesen_libretro.dll', #Mesen
                    4 : 'nestopia_libretro.dll', #Nestopia UE
                    5 : 'quicknes_libretro.dll', #QuickNES
                    'emux_nes_libretro.dll' : {
                        'coreExtensions' : ['nes', 'bin', 'rom'],
                        'friendlyName' : 'Nintendo - NES / Famicom (Emux NES)'
                        },
                    'fceumm_libretro.dll' : {
                        'coreExtensions' : ['fds', 'nes', 'unif', 'unf'],
                        'friendlyName' : 'Nintendo - NES / Famicom (FCEUmm)'
                        },
                    'mesen_libretro.dll' : {
                        'coreExtensions' : ['nes', 'fds', 'unf', 'unif'],
                        'friendlyName' : 'Nintendo - NES / Famicom (Mesen)'
                        },
                    'nestopia_libretro.dll' : {
                        'coreExtensions' : ['nes', 'fds', 'unf', 'unif'],
                        'friendlyName' : 'Nintendo - NES / Famicom (Nestopia UE)'
                        },
                    'quicknes_libretro.dll' : {
                        'coreExtensions' : ['nes'],
                        'friendlyName' : 'Nintendo - NES / Famicom (QuickNES)'
                        }
                    }
                }
            }
		},
    'Nintendo eShop' : { 
		'systemNames' : ['Nintendo eShop'],
		'systemIds' : {
			'igdb' : 160,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['nes', 'fds', 'unf', 'unif', 'bin', 'rom', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'fceumm_libretro.dll', #default
                    1 : 'emux_nes_libretro.dll', #Emux NES
                    2 : 'fceumm_libretro.dll', #FCEUmm
                    3 : 'mesen_libretro.dll', #Mesen
                    4 : 'nestopia_libretro.dll', #Nestopia UE
                    5 : 'quicknes_libretro.dll', #QuickNES
                    'emux_nes_libretro.dll' : {
                        'coreExtensions' : ['nes', 'bin', 'rom'],
                        'friendlyName' : 'Nintendo - NES / Famicom (Emux NES)'
                        },
                    'fceumm_libretro.dll' : {
                        'coreExtensions' : ['fds', 'nes', 'unif', 'unf'],
                        'friendlyName' : 'Nintendo - NES / Famicom (FCEUmm)'
                        },
                    'mesen_libretro.dll' : {
                        'coreExtensions' : ['nes', 'fds', 'unf', 'unif'],
                        'friendlyName' : 'Nintendo - NES / Famicom (Mesen)'
                        },
                    'nestopia_libretro.dll' : {
                        'coreExtensions' : ['nes', 'fds', 'unf', 'unif'],
                        'friendlyName' : 'Nintendo - NES / Famicom (Nestopia UE)'
                        },
                    'quicknes_libretro.dll' : {
                        'coreExtensions' : ['nes'],
                        'friendlyName' : 'Nintendo - NES / Famicom (QuickNES)'
                        }
                    }
                }
            }
		},
    'Nintendo Family Computer' : { 
		'systemNames' : ['Nintendo Family Computer', 'Family Computer (FAMICOM)', 'FAMICOM', 'Family Computer'],
		'systemIds' : {
			'igdb' : 99,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
		'romExtensions' : ['nes', 'fds', 'unf', 'unif', 'bin', 'rom', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'fceumm_libretro.dll', #default
                    1 : 'emux_nes_libretro.dll', #Emux NES
                    2 : 'fceumm_libretro.dll', #FCEUmm
                    3 : 'mesen_libretro.dll', #Mesen
                    4 : 'nestopia_libretro.dll', #Nestopia UE
                    5 : 'quicknes_libretro.dll', #QuickNES
                    'emux_nes_libretro.dll' : {
                        'coreExtensions' : ['nes', 'bin', 'rom'],
                        'friendlyName' : 'Nintendo - NES / Famicom (Emux NES)'
                        },
                    'fceumm_libretro.dll' : {
                        'coreExtensions' : ['fds', 'nes', 'unif', 'unf'],
                        'friendlyName' : 'Nintendo - NES / Famicom (FCEUmm)'
                        },
                    'mesen_libretro.dll' : {
                        'coreExtensions' : ['nes', 'fds', 'unf', 'unif'],
                        'friendlyName' : 'Nintendo - NES / Famicom (Mesen)'
                        },
                    'nestopia_libretro.dll' : {
                        'coreExtensions' : ['nes', 'fds', 'unf', 'unif'],
                        'friendlyName' : 'Nintendo - NES / Famicom (Nestopia UE)'
                        },
                    'quicknes_libretro.dll' : {
                        'coreExtensions' : ['nes'],
                        'friendlyName' : 'Nintendo - NES / Famicom (QuickNES)'
                        }
                    }
                }
            }
		},
    'Nintendo Game and Watch' : { 
		'systemNames' : ['Nintendo Game and Watch', 'Nintendo Game & Watch', 'Game & Watch', 'Game and Watch', 'Tricotronic'],
		'systemIds' : {
			'igdb' : 307,
			'thegamesdb' : 4950
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['sfc', 'smc', 'fig', 'swc', 'bs', 'gb', 'gbc', 'gbs', 'dmg', 'cgb', 'sgb', 'bin', 'rom', 'gba', 'bml', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'gearboy_libretro.dll', #default
                    1 : 'emux_gb_libretro.dll', #Emux GB
                    2 : 'fixgb_libretro.dll', #fixGB
                    3 : 'gambatte_libretro.dll', #Gambatte
                    4 : 'gearboy_libretro.dll', #Gearboy
                    5 : 'sameboy_libretro.dll', #SameBoy
                    6 : 'tgbdual_libretro.dll', #TGB Dual
                    7 : 'mesen-s_libretro.dll', #Mesen-S
                    8 : 'mgba_libretro.dll', #mGBA
                    9 : 'vbam_libretro.dll', #VBA-M
                    10 : 'higan_sfc_libretro.dll', #higan Accuracy
                    11 : 'higan_sfc_balanced_libretro.dll', #nSide Balanced
                    'emux_gb_libretro.dll' : {
                        'coreExtensions' : ['gb', 'bin', 'rom'],
                        'friendlyName' : 'Nintendo - Game Boy / Color (Emux GB)'
                        },
                    'fixgb_libretro.dll' : {
                        'coreExtensions' : ['gb', 'gbc', 'gbs'],
                        'friendlyName' : 'Nintendo - Game Boy / Color (fixGB)'
                        },
                    'gambatte_libretro.dll' : {
                        'coreExtensions' : ['gb', 'gbc', 'dmg'],
                        'friendlyName' : 'Nintendo - Game Boy / Color (Gambatte)'
                        },
                    'gearboy_libretro.dll' : {
                        'coreExtensions' : ['gb', 'dmg', 'gbc', 'cgb', 'sgb'],
                        'friendlyName' : 'Nintendo - Game Boy / Color (Gearboy)'
                        },
                    'sameboy_libretro.dll' : {
                        'coreExtensions' : ['gb', 'gbc'],
                        'friendlyName' : 'Nintendo - Game Boy / Color (SameBoy)'
                        },
                    'tgbdual_libretro.dll' : {
                        'coreExtensions' : ['gb', 'gbc', 'sgb'],
                        'friendlyName' : 'Nintendo - Game Boy / Color (TGB Dual)'
                        },
                    'mesen-s_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'fig', 'swc', 'bs', 'gb', 'gbc'],
                        'friendlyName' : 'Nintendo - SNES / SFC / Game Boy / Color (Mesen-S)'
                        },
                    'mgba_libretro.dll' : {
                        'coreExtensions' : ['gb', 'gbc', 'gba'],
                        'friendlyName' : 'Nintendo - Game Boy Advance (mGBA)'
                        },
                    'vbam_libretro.dll' : {
                        'coreExtensions' : ['dmg', 'gb', 'gbc', 'cgb', 'sgb', 'gba'],
                        'friendlyName' : 'Nintendo - Game Boy Advance (VBA-M)'
                        },
                    'higan_sfc_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom'],
                        'friendlyName' : 'Nintendo - SNES / Famicom (higan Accuracy)'
                        },
                    'higan_sfc_balanced_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom'],
                        'friendlyName' : 'Nintendo - SNES / Famicom (nSide Balanced)'
                        }
                    }
                }
            }
		},
    'Nintendo Game Boy Advance' : { 
		'systemNames' : ['Nintendo Game Boy Advance', 'Game Boy Advance', 'GBA', 'Nintendo GBA'],
		'systemIds' : {
			'igdb' : 24,
			'thegamesdb' : 5
			},
        'libraryType' : 'Games',
		'romExtensions' : ['dmg', 'gb', 'gbc', 'cgb', 'sgb', 'gba', 'agb', 'bin', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mgba_libretro.dll', #default
                    1 : 'mednafen_gba_libretro.dll', #Beetle GBA
                    2 : 'gpsp_libretro.dll', #gpSP
                    3 : 'meteor_libretro.dll', #Meteor
                    4 : 'mgba_libretro.dll', #mGBA
                    5 : 'vba_next_libretro.dll', #VBA Next
                    6 : 'vbam_libretro.dll', #VBA-M
                    'mednafen_gba_libretro.dll' : {
                        'coreExtensions' : ['gba', 'agb', 'bin'],
                        'friendlyName' : 'Nintendo - Game Boy Advance (Beetle GBA)'
                        },
                    'gpsp_libretro.dll' : {
                        'coreExtensions' : ['gba', 'bin'],
                        'friendlyName' : 'Nintendo - Game Boy Advance (gpSP)'
                        },
                    'meteor_libretro.dll' : {
                        'coreExtensions' : ['gba'],
                        'friendlyName' : 'Nintendo - Game Boy Advance (Meteor)'
                        },
                    'mgba_libretro.dll' : {
                        'coreExtensions' : ['gb', 'gbc', 'gba'],
                        'friendlyName' : 'Nintendo - Game Boy Advance (mGBA)'
                        },
                    'vba_next_libretro.dll' : {
                        'coreExtensions' : ['gba'],
                        'friendlyName' : 'Nintendo - Game Boy Advance (VBA Next)'
                        },
                    'vbam_libretro.dll' : {
                        'coreExtensions' : ['dmg', 'gb', 'gbc', 'cgb', 'sgb', 'gba'],
                        'friendlyName' : 'Nintendo - Game Boy Advance (VBA-M)'
                        }
                    }
                }
            }
		},
    'Nintendo Game Boy Color' : { 
		'systemNames' : ['Nintendo Game Boy Color', 'Game Boy Color', 'GBC', 'Nintendo GBC'],
		'systemIds' : {
			'igdb' : 22,
			'thegamesdb' : 41
			},
        'libraryType' : 'Games',
		'romExtensions' : ['sfc', 'smc', 'fig', 'swc', 'bs', 'gb', 'gbc', 'gbs', 'dmg', 'cgb', 'sgb', 'bin', 'rom', 'gba', 'bml', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'gambatte_libretro.dll', #default
                    1 : 'emux_gb_libretro.dll', #Emux GB
                    2 : 'fixgb_libretro.dll', #fixGB
                    3 : 'gambatte_libretro.dll', #Gambatte
                    4 : 'gearboy_libretro.dll', #Gearboy
                    5 : 'sameboy_libretro.dll', #SameBoy
                    6 : 'tgbdual_libretro.dll', #TGB Dual
                    7 : 'mesen-s_libretro.dll', #Mesen-S
                    8 : 'mgba_libretro.dll', #mGBA
                    9 : 'vbam_libretro.dll', #VBA-M
                    10 : 'higan_sfc_libretro.dll', #higan Accuracy
                    11 : 'higan_sfc_balanced_libretro.dll', #nSide Balanced
                    'emux_gb_libretro.dll' : {
                        'coreExtensions' : ['gb', 'bin', 'rom'],
                        'friendlyName' : 'Nintendo - Game Boy / Color (Emux GB)'
                        },
                    'fixgb_libretro.dll' : {
                        'coreExtensions' : ['gb', 'gbc', 'gbs'],
                        'friendlyName' : 'Nintendo - Game Boy / Color (fixGB)'
                        },
                    'gambatte_libretro.dll' : {
                        'coreExtensions' : ['gb', 'gbc', 'dmg'],
                        'friendlyName' : 'Nintendo - Game Boy / Color (Gambatte)'
                        },
                    'gearboy_libretro.dll' : {
                        'coreExtensions' : ['gb', 'dmg', 'gbc', 'cgb', 'sgb'],
                        'friendlyName' : 'Nintendo - Game Boy / Color (Gearboy)'
                        },
                    'sameboy_libretro.dll' : {
                        'coreExtensions' : ['gb', 'gbc'],
                        'friendlyName' : 'Nintendo - Game Boy / Color (SameBoy)'
                        },
                    'tgbdual_libretro.dll' : {
                        'coreExtensions' : ['gb', 'gbc', 'sgb'],
                        'friendlyName' : 'Nintendo - Game Boy / Color (TGB Dual)'
                        },
                    'mesen-s_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'fig', 'swc', 'bs', 'gb', 'gbc'],
                        'friendlyName' : 'Nintendo - SNES / SFC / Game Boy / Color (Mesen-S)'
                        },
                    'mgba_libretro.dll' : {
                        'coreExtensions' : ['gb', 'gbc', 'gba'],
                        'friendlyName' : 'Nintendo - Game Boy Advance (mGBA)'
                        },
                    'vbam_libretro.dll' : {
                        'coreExtensions' : ['dmg', 'gb', 'gbc', 'cgb', 'sgb', 'gba'],
                        'friendlyName' : 'Nintendo - Game Boy Advance (VBA-M)'
                        },
                    'higan_sfc_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom'],
                        'friendlyName' : 'Nintendo - SNES / Famicom (higan Accuracy)'
                        },
                    'higan_sfc_balanced_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom'],
                        'friendlyName' : 'Nintendo - SNES / Famicom (nSide Balanced)'
                        }
                    }
                }
            }
		},
    'Nintendo GameCube' : { 
		'systemNames' : ['Nintendo GameCube', 'NGC', 'GameCube', 'GC', 'Dolphin'],
		'systemIds' : {
			'igdb' : 21,
			'thegamesdb' : 2
			},
        'libraryType' : 'Games',
		'romExtensions' : ['gcm', 'iso', 'wbfs', 'ciso', 'gcz', 'elf', 'dol', 'dff', 'tgc', 'wad', 'rvz'],
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
                        'coreExtensions' : ['gcm', 'iso', 'wbfs', 'ciso', 'gcz', 'elf', 'dol', 'dff', 'tgc', 'wad', 'rvz', 'm3u'],
                        'friendlyName' : 'Nintendo - GameCube / Wii (Dolphin)'
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['min'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'pokemini_libretro.dll', #default
                    1 : 'pokemini_libretro.dll', #PokeMini
                    'pokemini_libretro.dll' : {
                        'coreExtensions' : ['min'],
                        'friendlyName' : 'Nintendo - Pokemon Mini (PokeMini)'
                        }
                    }
                }
            }
		},
    'Nintendo Super Famicom' : { 
		'systemNames' : ['Nintendo Super Famicom', 'SFAM', 'Super Famicom', 'SFC', 'Super Family Computer', 'NSFAM', 'NSFC', 'Nintendo Super Family Computer'],
		'systemIds' : {
			'igdb' : 58,
			'thegamesdb' : 6
			},
        'libraryType' : 'Games',
		'romExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc', 'bs', 'st', 'gb', 'gbc', 'bml', 'rom', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'snes9x_libretro.dll', #default
                    1 : 'higan_sfc_libretro.dll', #higan Accuracy
                    2 : 'higan_sfc_balanced_libretro.dll', #nSide Balanced
                    3 : 'mednafen_snes_libretro.dll', #Beetle bsnes
                    4 : 'mednafen_supafaust_libretro.dll', #Beetle Supafaust
                    5 : 'bsnes2014_accuracy_libretro.dll', #bsnes 2014 Accuracy
                    6 : 'bsnes2014_balanced_libretro.dll', #bsnes 2014 Balanced
                    7 : 'bsnes2014_performance_libretro.dll', #bsnes 2014 Performance
                    8 : 'bsnes_cplusplus98_libretro.dll', #bsnes C++98(v085)
                    9 : 'bsnes_libretro.dll', #bsnes
                    10 : 'bsnes_hd_beta_libretro.dll', #bsnes-hd beta
                    11 : 'bsnes_mercury_accuracy_libretro.dll', #bsnes-mercury Accuracy
                    12 : 'bsnes_mercury_balanced_libretro.dll', #bsnes-mercury Balanced
                    13 : 'bsnes_mercury_performance_libretro.dll', #bsnes-mercury Performance
                    14 : 'snes9x_libretro.dll', #Snes9x - Current
                    15 : 'snes9x2002_libretro.dll', #Snes9x 2002
                    16 : 'snes9x2005_plus_libretro.dll', #Snes9x 2005 Plus
                    17 : 'snes9x2005_libretro.dll', #Snes9x 2005
                    18 : 'snes9x2010_libretro.dll', #Snes9x 2010
                    19 : 'mesen-s_libretro.dll', #Mesen-S
                    'higan_sfc_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom'],
                        'friendlyName' : 'Nintendo - SNES / Famicom (higan Accuracy)'
                        },
                    'higan_sfc_balanced_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom'],
                        'friendlyName' : 'Nintendo - SNES / Famicom (nSide Balanced)'
                        },
                    'mednafen_snes_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'bs', 'st', 'sfc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Beetle bsnes)'
                        },
                    'mednafen_supafaust_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Beetle Supafaust)'
                        },
                    'bsnes2014_accuracy_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes 2014 Accuracy)'
                        },
                    'bsnes2014_balanced_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes 2014 Balanced)'
                        },
                    'bsnes2014_performance_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes 2014 Performance)'
                        },
                    'bsnes_cplusplus98_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes C++98 (v085))'
                        },
                    'bsnes_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc', 'bs'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes)'
                        },
                    'bsnes_hd_beta_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes-hd beta)'
                        },
                    'bsnes_mercury_accuracy_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes-mercury Accuracy)'
                        },
                    'bsnes_mercury_balanced_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes-mercury Balanced)'
                        },
                    'bsnes_mercury_performance_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes-mercury Performance)'
                        },
                    'snes9x_libretro.dll' : {
                        'coreExtensions' : ['smc', 'sfc', 'swc', 'fig', 'bs', 'st'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x - Current)'
                        },
                    'snes9x2002_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x 2002)'
                        },
                    'snes9x2005_plus_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x 2005 Plus)'
                        },
                    'snes9x2005_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x 2005)'
                        },
                    'snes9x2010_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x 2010)'
                        },
                    'mesen-s_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'fig', 'swc', 'bs', 'gb', 'gbc'],
                        'friendlyName' : 'Nintendo - SNES / SFC / Game Boy / Color (Mesen-S)'
                        }
                    }
                }
            }
		},
    'Nintendo Super Famicom Satellaview' : { 
		'systemNames' : ['Nintendo Super Famicom Satellaview', 'Satellaview'],
		'systemIds' : {
			'igdb' : 306,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
		'romExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc', 'bs', 'st', 'gb', 'gbc', 'bml', 'rom', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'snes9x_libretro.dll', #default
                    1 : 'higan_sfc_libretro.dll', #higan Accuracy
                    2 : 'higan_sfc_balanced_libretro.dll', #nSide Balanced
                    3 : 'mednafen_snes_libretro.dll', #Beetle bsnes
                    4 : 'mednafen_supafaust_libretro.dll', #Beetle Supafaust
                    5 : 'bsnes2014_accuracy_libretro.dll', #bsnes 2014 Accuracy
                    6 : 'bsnes2014_balanced_libretro.dll', #bsnes 2014 Balanced
                    7 : 'bsnes2014_performance_libretro.dll', #bsnes 2014 Performance
                    8 : 'bsnes_cplusplus98_libretro.dll', #bsnes C++98(v085)
                    9 : 'bsnes_libretro.dll', #bsnes
                    10 : 'bsnes_hd_beta_libretro.dll', #bsnes-hd beta
                    11 : 'bsnes_mercury_accuracy_libretro.dll', #bsnes-mercury Accuracy
                    12 : 'bsnes_mercury_balanced_libretro.dll', #bsnes-mercury Balanced
                    13 : 'bsnes_mercury_performance_libretro.dll', #bsnes-mercury Performance
                    14 : 'snes9x_libretro.dll', #Snes9x - Current
                    15 : 'snes9x2002_libretro.dll', #Snes9x 2002
                    16 : 'snes9x2005_plus_libretro.dll', #Snes9x 2005 Plus
                    17 : 'snes9x2005_libretro.dll', #Snes9x 2005
                    18 : 'snes9x2010_libretro.dll', #Snes9x 2010
                    19 : 'mesen-s_libretro.dll', #Mesen-S
                    'higan_sfc_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom'],
                        'friendlyName' : 'Nintendo - SNES / Famicom (higan Accuracy)'
                        },
                    'higan_sfc_balanced_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom'],
                        'friendlyName' : 'Nintendo - SNES / Famicom (nSide Balanced)'
                        },
                    'mednafen_snes_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'bs', 'st', 'sfc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Beetle bsnes)'
                        },
                    'mednafen_supafaust_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Beetle Supafaust)'
                        },
                    'bsnes2014_accuracy_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes 2014 Accuracy)'
                        },
                    'bsnes2014_balanced_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes 2014 Balanced)'
                        },
                    'bsnes2014_performance_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes 2014 Performance)'
                        },
                    'bsnes_cplusplus98_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes C++98 (v085))'
                        },
                    'bsnes_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc', 'bs'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes)'
                        },
                    'bsnes_hd_beta_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes-hd beta)'
                        },
                    'bsnes_mercury_accuracy_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes-mercury Accuracy)'
                        },
                    'bsnes_mercury_balanced_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes-mercury Balanced)'
                        },
                    'bsnes_mercury_performance_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes-mercury Performance)'
                        },
                    'snes9x_libretro.dll' : {
                        'coreExtensions' : ['smc', 'sfc', 'swc', 'fig', 'bs', 'st'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x - Current)'
                        },
                    'snes9x2002_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x 2002)'
                        },
                    'snes9x2005_plus_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x 2005 Plus)'
                        },
                    'snes9x2005_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x 2005)'
                        },
                    'snes9x2010_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x 2010)'
                        },
                    'mesen-s_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'fig', 'swc', 'bs', 'gb', 'gbc'],
                        'friendlyName' : 'Nintendo - SNES / SFC / Game Boy / Color (Mesen-S)'
                        }
                    }
                }
            }
		},
    'Nintendo Switch' : { 
		'systemNames' : ['Nintendo Switch', 'Switch', 'NX'],
		'systemIds' : {
			'igdb' : 130,
			'thegamesdb' : 4971
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['vb', 'vboy', 'bin'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mednafen_vb_libretro.dll', #default
                    1 : 'mednafen_vb_libretro.dll', #Beetle VB
                    'mednafen_vb_libretro.dll' : {
                        'coreExtensions' : ['vb', 'vboy', 'bin'],
                        'friendlyName' : 'Nintendo - Virtual Boy (Beetle VB)'
                        }
                    }
                }
            }
		},
    'Nintendo Virtual Console' : { 
		'systemNames' : ['Nintendo Virtual Console', 'Virtual Console (Nintendo)', 'VC', 'Nintendo VC'],
		'systemIds' : {
			'igdb' : 47,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['gcm', 'iso', 'wbfs', 'ciso', 'gcz', 'elf', 'dol', 'dff', 'tgc', 'wad', 'rvz'],
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
                        'coreExtensions' : ['gcm', 'iso', 'wbfs', 'ciso', 'gcz', 'elf', 'dol', 'dff', 'tgc', 'wad', 'rvz', 'm3u'],
                        'friendlyName' : 'Nintendo - GameCube / Wii (Dolphin)'
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
        'libraryType' : 'Games',
		'romExtensions' : ['rpx', 'wud'],
		'romType' : 0,
		'multiDisk' : False,
		'emulators' : {
            0 : 'cemu', #agent enums to emulator name
            1 : 'cemu',
            'cemu' : {}
            }
		},
    'Nintendo WiiWare' : { 
		'systemNames' : ['Nintendo WiiWare', 'WiiWare'],
		'systemIds' : {
			'igdb' : 56,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Quake 1 Engine' : { 
		'systemNames' : ['Quake 1 Engine', 'Quake Engine', 'Quake', 'Quake I Engine', 'Quake I'],
		'systemIds' : {
			'igdb' : 6,
			'thegamesdb' : 1
			},
        'libraryType' : 'Games',
		'romExtensions' : ['pak'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'tyrquake_libretro.dll', #default
                    1 : 'tyrquake_libretro.dll', #TyrQuake
                    'tyrquake_libretro.dll' : {
                        'coreExtensions' : ['pak'],
                        'friendlyName' : 'Quake (TyrQuake)'
                        }
                    }
                }
            }
		},
    'Quake II Engine' : { 
		'systemNames' : ['Quake II Engine', 'Quake II', 'Quake 2 Engine', 'Quake 2'],
		'systemIds' : {
			'igdb' : 6,
			'thegamesdb' : 1
			},
        'libraryType' : 'Games',
		'romExtensions' : ['pak'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'vitaquake2_libretro.dll', #default
                    1 : 'vitaquake2_libretro.dll', #vitaQuake 2
                    'vitaquake2_libretro.dll' : {
                        'coreExtensions' : ['pak'],
                        'friendlyName' : 'Quake II (vitaQuake 2)'
                        }
                    }
                }
            }
		},
    'Quake III Engine' : { 
		'systemNames' : ['Quake III Engine', 'Quake III', 'Quake 3 Engine', 'Quake 3'],
		'systemIds' : {
			'igdb' : 6,
			'thegamesdb' : 1
			},
        'libraryType' : 'Games',
		'romExtensions' : ['pk3'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'vitaquake3_libretro.dll', #default
                    1 : 'vitaquake3_libretro.dll', #vitaQuake 3
                    'vitaquake3_libretro.dll' : {
                        'coreExtensions' : ['pk3'],
                        'friendlyName' : 'Quake III: Arena (vitaQuake 3)'
                        }
                    }
                }
            }
		},
    'R-Zone' : { 
		'systemNames' : ['R-Zone'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4983
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Rick Dangerous Engine' : { 
		'systemNames' : ['Rick Dangerous Engine', 'Rick Dangerous'],
		'systemIds' : {
			'igdb' : 6,
			'thegamesdb' : 1
			},
        'libraryType' : 'Games',
		'romExtensions' : ['zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'xrick_libretro.dll', #default
                    1 : 'xrick_libretro.dll', #XRick
                    'xrick_libretro.dll' : {
                        'coreExtensions' : ['zip'],
                        'friendlyName' : 'Rick Dangerous (XRick)'
                        }
                    }
                }
            }
		},
    'RPG Maker' : { 
		'systemNames' : ['RPG Maker', 'EasyRPG'],
		'systemIds' : {
			'igdb' : 6,
			'thegamesdb' : 1
			},
        'libraryType' : 'Games',
		'romExtensions' : ['ldb'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'easyrpg_libretro.dll', #default
                    1 : 'easyrpg_libretro.dll', #EasyRPG
                    'easyrpg_libretro.dll' : {
                        'coreExtensions' : ['ldb'],
                        'friendlyName' : 'RPG Maker 2000/2003 (EasyRPG)'
                        }
                    }
                }
            }
		},
    'SAM Coupé' : { 
		'systemNames' : ['SAM Coupé', 'SAM Coupe'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4979
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['0', '1', '2', '3', '5', '6', '8', '16', '25', '99', '101', '102', '418', '455', '512', 'scummvm', 'scumm', 'gam', 'z5', 'dat', 'blb', 'z6', 'RAW', 'ROM', 'taf', 'zblorb', 'dcp', '(a)', 'cup', 'HE0', '(A)', 'D$$', 'STK', 'z8', 'hex', 'VMD', 'TGA', 'ITK', 'SCN', 'INF', 'pic', 'Z5', 'z3', 'blorb', 'ulx', 'DAT', 'cas', 'PIC', 'acd', '006', 'SYS', 'alr', 't3', 'gblorb', 'tab', 'AP', 'CRC', 'EXE', 'z4', 'W32', 'MAC', 'mac', 'WIN', '001', '003', '000', 'bin', 'exe', 'asl', 'AVD', 'INI', 'SND', 'cat', 'ANG', 'CUP', 'SYS16', 'img', 'LB', 'TLK', 'MIX', 'VQA', 'RLB', 'FNT', 'win', 'HE1', 'DMU', 'FON', 'SCR', 'TEX', 'HEP', 'DIR', 'DRV', 'MAP', 'a3c', 'GRV', 'CUR', 'OPT', 'gfx', 'ASK', 'LNG', 'ini', 'RSC', 'SPP', 'CC', 'BND', 'LA0', 'TRS', 'add', 'HRS', 'DFW', 'DR1', 'ALD', '004', '002', '005', 'R02', 'R00', 'C00', 'D00', 'GAM', 'IDX', 'ogg', 'TXT', 'GRA', 'BMV', 'H$$', 'MSG', 'VGA', 'PKD', 'OUT', '99 (PG)', 'SAV', 'PAK', 'BIN', 'CPS', 'SHP', 'DXR', 'dxr', 'gmp', 'SNG', 'C35', 'C06', 'WAV', 'SMK', 'wav', 'CAB', 'game', 'Z6', '(b)', 'slg', 'he2', 'he1', 'HE2', 'SYN', 'PAT', 'NUT', 'nl', 'PRC', 'V56', 'SEQ', 'P56', 'AUD', 'FKR', 'EX1', 'rom', 'LIC', '$00', 'ALL', 'LTK', 'txt', 'acx', 'VXD', 'ACX', 'mpc', 'msd', 'ADF', 'nib', 'HELLO', 'dsk', 'xfd', 'woz', 'd$$', 'SET', 'SOL', 'Pat', 'CFG', 'BSF', 'RES', 'IMD', 'LFL', 'SQU', 'rsc', 'BBM', '2 US', 'OVL', 'OVR', '007', 'PNT', 'pat', 'CHK', 'MDT', 'EMC', 'ADV', 'FDT', 'GMC', 'FMC', 'info', 'HPF', 'hpf', 'INE', 'RBT', 'CSC', 'HEB', 'MID', 'lfl', 'LEC', 'HNM', 'QA', '009', 'PRF', 'EGA', 'MHK', 'd64', 'prg', 'LZC', 'flac', 'IMS', 'REC', 'MOR', 'doc', 'HAG', 'AGA', 'BLB', 'TABLE', 'PAL', 'PRG', 'CLG', 'ORB', 'BRO', 'bro', 'PH1', 'DEF', 'IN', 'jpg', 'TOC', 'j2', 'Text', 'CEL', 'he0', 'AVI', '1C', '1c', 'BAK', 'L9', 'CGA', 'HRC', 'mhk', 'RED', 'SM0', 'SM1', 'SOU', 'RRM', 'LIB', " Seuss's  ABC", 'CNV', 'VOC', 'OGG', 'GME', 'GERMAN', 'SHR', 'FRENCH', 'DNR', 'DSK', 'dnr', 'CAT', 'V16', 'cab', 'CLU', 'b25c', 'RL', 'mp3', 'FRM', 'SOG', 'HEX', 'mma', 'st', 'MPC', 'IMG', 'ENC', 'SPR', 'AD', 'C', 'CON', 'PGM', 'Z', 'RL2', 'MMM', 'OBJ', 'ZFS', 'zfs', 'STR', 'z2', 'z1'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'scummvm_libretro.dll', #default
                    1 : 'scummvm_libretro.dll', #ScummVM
                    'scummvm_libretro.dll' : {
                        'coreExtensions' : ['0', '1', '2', '3', '5', '6', '8', '16', '25', '99', '101', '102', '418', '455', '512', 'scummvm', 'scumm', 'gam', 'z5', 'dat', 'blb', 'z6', 'RAW', 'ROM', 'taf', 'zblorb', 'dcp', '(a)', 'cup', 'HE0', '(A)', 'D$$', 'STK', 'z8', 'hex', 'VMD', 'TGA', 'ITK', 'SCN', 'INF', 'pic', 'Z5', 'z3', 'blorb', 'ulx', 'DAT', 'cas', 'PIC', 'acd', '006', 'SYS', 'alr', 't3', 'gblorb', 'tab', 'AP', 'CRC', 'EXE', 'z4', 'W32', 'MAC', 'mac', 'WIN', '001', '003', '000', 'bin', 'exe', 'asl', 'AVD', 'INI', 'SND', 'cat', 'ANG', 'CUP', 'SYS16', 'img', 'LB', 'TLK', 'MIX', 'VQA', 'RLB', 'FNT', 'win', 'HE1', 'DMU', 'FON', 'SCR', 'TEX', 'HEP', 'DIR', 'DRV', 'MAP', 'a3c', 'GRV', 'CUR', 'OPT', 'gfx', 'ASK', 'LNG', 'ini', 'RSC', 'SPP', 'CC', 'BND', 'LA0', 'TRS', 'add', 'HRS', 'DFW', 'DR1', 'ALD', '004', '002', '005', 'R02', 'R00', 'C00', 'D00', 'GAM', 'IDX', 'ogg', 'TXT', 'GRA', 'BMV', 'H$$', 'MSG', 'VGA', 'PKD', 'OUT', '99 (PG)', 'SAV', 'PAK', 'BIN', 'CPS', 'SHP', 'DXR', 'dxr', 'gmp', 'SNG', 'C35', 'C06', 'WAV', 'SMK', 'wav', 'CAB', 'game', 'Z6', '(b)', 'slg', 'he2', 'he1', 'HE2', 'SYN', 'PAT', 'NUT', 'nl', 'PRC', 'V56', 'SEQ', 'P56', 'AUD', 'FKR', 'EX1', 'rom', 'LIC', '$00', 'ALL', 'LTK', 'txt', 'acx', 'VXD', 'ACX', 'mpc', 'msd', 'ADF', 'nib', 'HELLO', 'dsk', 'xfd', 'woz', 'd$$', 'SET', 'SOL', 'Pat', 'CFG', 'BSF', 'RES', 'IMD', 'LFL', 'SQU', 'rsc', 'BBM', '2 US', 'OVL', 'OVR', '007', 'PNT', 'pat', 'CHK', 'MDT', 'EMC', 'ADV', 'FDT', 'GMC', 'FMC', 'info', 'HPF', 'hpf', 'INE', 'RBT', 'CSC', 'HEB', 'MID', 'lfl', 'LEC', 'HNM', 'QA', '009', 'PRF', 'EGA', 'MHK', 'd64', 'prg', 'LZC', 'flac', 'IMS', 'REC', 'MOR', 'doc', 'HAG', 'AGA', 'BLB', 'TABLE', 'PAL', 'PRG', 'CLG', 'ORB', 'BRO', 'bro', 'PH1', 'DEF', 'IN', 'jpg', 'TOC', 'j2', 'Text', 'CEL', 'he0', 'AVI', '1C', '1c', 'BAK', 'L9', 'CGA', 'HRC', 'mhk', 'RED', 'SM0', 'SM1', 'SOU', 'RRM', 'LIB', " Seuss's  ABC", 'CNV', 'VOC', 'OGG', 'GME', 'GERMAN', 'SHR', 'FRENCH', 'DNR', 'DSK', 'dnr', 'CAT', 'V16', 'cab', 'CLU', 'b25c', 'RL', 'mp3', 'FRM', 'SOG', 'HEX', 'mma', 'st', 'MPC', 'IMG', 'ENC', 'SPR', 'AD', 'C', 'CON', 'PGM', 'Z', 'RL2', 'MMM', 'OBJ', 'ZFS', 'zfs', 'STR', 'z2', 'z1'],
                        'friendlyName' : 'ScummVM'
                        }
                    }
                }
            }
		},
    'SDS Sigma 7' : { 
		'systemNames' : ['SDS Sigma 7', 'sdssigma7'],
		'systemIds' : {
			'igdb' : 106,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['gen', 'smd', 'md', '32x', 'cue', 'iso', 'sms', '68k'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'picodrive_libretro.dll', #default
                    1 : 'picodrive_libretro.dll', #PicoDrive
                    'picodrive_libretro.dll' : {
                        'coreExtensions' : ['bin', 'gen', 'smd', 'md', '32x', 'cue', 'iso', 'sms', '68k'],
                        'friendlyName' : 'Sega - MS/MD/CD/32X (PicoDrive)'
                        }
                    }
                }
            }
		},
    'Sega CD' : { 
		'systemNames' : ['Sega CD', 'segacd', 'Mega CD'],
		'systemIds' : {
			'igdb' : 78,
			'thegamesdb' : 21
			},
        'libraryType' : 'Games',
		'romExtensions' : ['mdx', 'md', 'smd', 'gen', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd', '32x'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'genesis_plus_gx_libretro.dll', #default
                    1 : 'genesis_plus_gx_libretro.dll', #Genesis Plus GX
                    2 : 'picodrive_libretro.dll', #PicoDrive
                    'genesis_plus_gx_libretro.dll' : {
                        'coreExtensions' : ['mdx', 'md', 'smd', 'gen', 'bin', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd'],
                        'friendlyName' : 'Sega - MS/GG/MD/CD (Genesis Plus GX)'
                        },
                    'picodrive_libretro.dll' : {
                        'coreExtensions' : ['bin', 'gen', 'smd', 'md', '32x', 'cue', 'iso', 'sms', '68k'],
                        'friendlyName' : 'Sega - MS/MD/CD/32X (PicoDrive)'
                        }
                    }
                }
            }
		},
    'Sega Dreamcast' : { 
		'systemNames' : ['Sega Dreamcast', 'Dreamcast', 'DC'],
		'systemIds' : {
			'igdb' : 23,
			'thegamesdb' : 16
			},
        'libraryType' : 'Games',
		'romExtensions' : ['chd', 'cdi', 'iso', 'elf', 'cue', 'gdi', 'lst', 'zip', 'dat', '7z'], #removed bin... use cue files
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'flycast_libretro.dll', #default
                    1 : 'flycast_libretro.dll', #Flycast
                    2 : 'flycast_gles2_libretro.dll', #Flycast GLES2
                    'flycast_libretro.dll' : {
                        'coreExtensions' : ['chd', 'cdi', 'iso', 'elf', 'bin', 'cue', 'gdi', 'lst', 'zip', 'dat', '7z', 'm3u'],
                        'friendlyName' : 'Sega - Dreamcast/NAOMI (Flycast)'
                        },
                    'flycast_gles2_libretro.dll' : {
                        'coreExtensions' : ['chd', 'cdi', 'iso', 'elf', 'bin', 'cue', 'gdi', 'lst', 'zip', 'dat', '7z', 'm3u'],
                        'friendlyName' : 'Sega - Dreamcast/NAOMI (Flycast GLES2)'
                        }
                    }
                }
            }
		},
    'Sega Game Gear' : { 
		'systemNames' : ['Sega Game Gear', 'Game Gear', 'GG', 'Sega GG'],
		'systemIds' : {
			'igdb' : 35,
			'thegamesdb' : 20
			},
        'libraryType' : 'Games',
		'romExtensions' : ['mdx', 'md', 'smd', 'gen', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd', 'rom', 'col', ],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'smsplus_libretro.dll', #default
                    1 : 'smsplus_libretro.dll', #SMS Plus GX
                    2 : 'genesis_plus_gx_libretro.dll', #Genesis Plus GX
                    3 : 'gearsystem_libretro.dll', #Gearsystem
                    'smsplus_libretro.dll' : {
                        'coreExtensions' : ['sms', 'bin', 'rom', 'col', 'gg', 'sg'],
                        'friendlyName' : 'Sega - MS/GG (SMS Plus GX)'
                        },
                    'genesis_plus_gx_libretro.dll' : {
                        'coreExtensions' : ['mdx', 'md', 'smd', 'gen', 'bin', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd'],
                        'friendlyName' : 'Sega - MS/GG/MD/CD (Genesis Plus GX)'
                        },
                    'gearsystem_libretro.dll' : {
                        'coreExtensions' : ['sms', 'gg', 'sg', 'bin', 'rom'],
                        'friendlyName' : 'Sega - MS/GG/SG-1000 (Gearsystem)'
                        }
                    }
                }
            }
		},
    'Sega Genesis' : { 
		'systemNames' : ['Sega Genesis', 'Genesis'],
		'systemIds' : {
			'igdb' : 29,
			'thegamesdb' : 18
			},
        'libraryType' : 'Games',
		'romExtensions' : ['mdx', 'md', 'smd', 'gen', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd', '32x', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'genesis_plus_gx_libretro.dll', #default
                    1 : 'blastem_libretro.dll', #BlastEm
                    2 : 'genesis_plus_gx_libretro.dll', #Genesis Plus GX
                    3 : 'picodrive_libretro.dll', #PicoDrive
                    'blastem_libretro.dll' : {
                        'coreExtensions' : ['md', 'bin', 'smd', 'gen'],
                        'friendlyName' : 'Sega - Mega Drive - Genesis (BlastEm)'
                        },
                    'genesis_plus_gx_libretro.dll' : {
                        'coreExtensions' : ['mdx', 'md', 'smd', 'gen', 'bin', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd'],
                        'friendlyName' : 'Sega - MS/GG/MD/CD (Genesis Plus GX)'
                        },
                    'picodrive_libretro.dll' : {
                        'coreExtensions' : ['bin', 'gen', 'smd', 'md', '32x', 'cue', 'iso', 'sms', '68k'],
                        'friendlyName' : 'Sega - MS/MD/CD/32X (PicoDrive)'
                        }
                    }
                }
            }
		},
    'Sega Master System' : { 
		'systemNames' : ['Sega Master System', 'SMS', 'Master System', 'Sega Mark III', 'Mark III'],
		'systemIds' : {
			'igdb' : 64,
			'thegamesdb' : 35
			},
        'libraryType' : 'Games',
		'romExtensions' : ['mdx', 'md', 'smd', 'gen', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd', 'rom', 'col', '32x', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'genesis_plus_gx_libretro.dll', #default
                    1 : 'emux_sms_libretro.dll', #Emux SMS
                    2 : 'smsplus_libretro.dll', #SMS Plus GX
                    3 : 'genesis_plus_gx_libretro.dll', #Genesis Plus GX
                    4 : 'gearsystem_libretro.dll', #Gearsystem
                    5 : 'picodrive_libretro.dll', #PicoDrive
                    'emux_sms_libretro.dll' : {
                        'coreExtensions' : ['sms', 'bms', 'bin', 'rom'],
                        'friendlyName' : 'Sega - Master System (Emux SMS)'
                        },
                    'smsplus_libretro.dll' : {
                        'coreExtensions' : ['sms', 'bin', 'rom', 'col', 'gg', 'sg'],
                        'friendlyName' : 'Sega - MS/GG (SMS Plus GX)'
                        },
                    'genesis_plus_gx_libretro.dll' : {
                        'coreExtensions' : ['mdx', 'md', 'smd', 'gen', 'bin', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd'],
                        'friendlyName' : 'Sega - MS/GG/MD/CD (Genesis Plus GX)'
                        },
                    'gearsystem_libretro.dll' : {
                        'coreExtensions' : ['sms', 'gg', 'sg', 'bin', 'rom'],
                        'friendlyName' : 'Sega - MS/GG/SG-1000 (Gearsystem)'
                        },
                    'picodrive_libretro.dll' : {
                        'coreExtensions' : ['bin', 'gen', 'smd', 'md', '32x', 'cue', 'iso', 'sms', '68k'],
                        'friendlyName' : 'Sega - MS/MD/CD/32X (PicoDrive)'
                        }
                    }
                }
            }
		},
    'Sega Mega Drive' : { 
		'systemNames' : ['Sega Mega Drive', 'Mega Drive'],
		'systemIds' : {
			'igdb' : 29,
			'thegamesdb' : 36
			},
        'libraryType' : 'Games',
		'romExtensions' : ['mdx', 'md', 'smd', 'gen', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd', '32x', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'genesis_plus_gx_libretro.dll', #default
                    1 : 'blastem_libretro.dll', #BlastEm
                    2 : 'genesis_plus_gx_libretro.dll', #Genesis Plus GX
                    3 : 'picodrive_libretro.dll', #PicoDrive
                    'blastem_libretro.dll' : {
                        'coreExtensions' : ['md', 'bin', 'smd', 'gen'],
                        'friendlyName' : 'Sega - Mega Drive - Genesis (BlastEm)'
                        },
                    'genesis_plus_gx_libretro.dll' : {
                        'coreExtensions' : ['mdx', 'md', 'smd', 'gen', 'bin', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd'],
                        'friendlyName' : 'Sega - MS/GG/MD/CD (Genesis Plus GX)'
                        },
                    'picodrive_libretro.dll' : {
                        'coreExtensions' : ['bin', 'gen', 'smd', 'md', '32x', 'cue', 'iso', 'sms', '68k'],
                        'friendlyName' : 'Sega - MS/MD/CD/32X (PicoDrive)'
                        }
                    }
                }
            }
		},
    'Sega Naomi' : { 
		'systemNames' : ['Sega Naomi', 'Naomi'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
        'libraryType' : 'Games',
		'romExtensions' : ['chd', 'cdi', 'iso', 'elf', 'bin', 'cue', 'gdi', 'lst', 'zip', 'dat', '7z'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'flycast_libretro.dll', #default
                    1 : 'flycast_libretro.dll', #Flycast
                    2 : 'flycast_gles2_libretro.dll', #Flycast GLES2
                    'flycast_libretro.dll' : {
                        'coreExtensions' : ['chd', 'cdi', 'iso', 'elf', 'bin', 'cue', 'gdi', 'lst', 'zip', 'dat', '7z', 'm3u'],
                        'friendlyName' : 'Sega - Dreamcast/NAOMI (Flycast)'
                        },
                    'flycast_gles2_libretro.dll' : {
                        'coreExtensions' : ['chd', 'cdi', 'iso', 'elf', 'bin', 'cue', 'gdi', 'lst', 'zip', 'dat', '7z', 'm3u'],
                        'friendlyName' : 'Sega - Dreamcast/NAOMI (Flycast GLES2)'
                        }
                    }
                }
            }
		},
    'Sega Naomi 2' : { 
		'systemNames' : ['Sega Naomi 2', 'Naomi 2'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['mdx', 'md', 'smd', 'gen', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd', '32x'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'genesis_plus_gx_libretro.dll', #default
                    1 : 'genesis_plus_gx_libretro.dll', #Genesis Plus GX
                    2 : 'picodrive_libretro.dll', #PicoDrive
                    'genesis_plus_gx_libretro.dll' : {
                        'coreExtensions' : ['mdx', 'md', 'smd', 'gen', 'bin', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd'],
                        'friendlyName' : 'Sega - MS/GG/MD/CD (Genesis Plus GX)'
                        },
                    'picodrive_libretro.dll' : {
                        'coreExtensions' : ['bin', 'gen', 'smd', 'md', '32x', 'cue', 'iso', 'sms', '68k'],
                        'friendlyName' : 'Sega - MS/MD/CD/32X (PicoDrive)'
                        }
                    }
                }
            }
		},
    'Sega Saturn' : { 
		'systemNames' : ['Sega Saturn', 'Saturn', 'JVC Saturn', 'Hi-Saturn', 'Samsung Saturn', 'V-Saturn'],
		'systemIds' : {
			'igdb' : 32,
			'thegamesdb' : 17
			},
        'libraryType' : 'Games',
		'romExtensions' : ['toc', 'ccd', 'chd', 'cue', 'iso', 'mds', 'zip'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mednafen_saturn_libretro.dll', #default
                    1 : 'mednafen_saturn_libretro.dll', #Beetle Saturn
                    2 : 'yabasanshiro_libretro.dll', #YabaSanshiro
                    3 : 'yabause_libretro.dll', #Yabause
                    4 : 'kronos_libretro.dll', #Kronos
                    'mednafen_saturn_libretro.dll' : {
                        'coreExtensions' : ['ccd', 'chd', 'cue', 'toc', 'm3u'],
                        'friendlyName' : 'Sega - Saturn (Beetle Saturn)'
                        },
                    'yabasanshiro_libretro.dll' : {
                        'coreExtensions' : ['bin', 'ccd', 'chd', 'cue', 'iso', 'mds', 'zip'],
                        'friendlyName' : 'Sega - Saturn (YabaSanshiro)'
                        },
                    'yabause_libretro.dll' : {
                        'coreExtensions' : ['bin', 'ccd', 'chd', 'cue', 'iso', 'mds', 'zip'],
                        'friendlyName' : 'Sega - Saturn (Yabause)'
                        },
                    'kronos_libretro.dll' : {
                        'coreExtensions' : ['ccd', 'chd', 'cue', 'iso', 'mds', 'zip', 'm3u'],
                        'friendlyName' : 'Sega - Saturn/ST-V (Kronos)'
                        }
                    }
                }
            }
		},
    'Sega SG-1000' : { 
		'systemNames' : ['Sega SG-1000', 'SG-1000', 'sg1000', 'Sega Game 1000'],
		'systemIds' : {
			'igdb' : 84,
			'thegamesdb' : 4949
			},
        'libraryType' : 'Games',
		'romExtensions' : ['mdx', 'md', 'smd', 'gen', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd', 'rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sc', 'zip'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'genesis_plus_gx_libretro.dll', #default
                    1 : 'bluemsx_libretro.dll', #blueMSX
                    2 : 'genesis_plus_gx_libretro.dll', #Genesis Plus GX
                    3 : 'gearsystem_libretro.dll', #Gearsystem
                    'bluemsx_libretro.dll' : {
                        'coreExtensions' : ['rom', 'ri', 'mx1', 'mx2', 'col', 'dsk', 'cas', 'sg', 'sc', 'm3u'],
                        'friendlyName' : 'MSX/SVI/ColecoVision/SG-1000 (blueMSX)'
                        },
                    'genesis_plus_gx_libretro.dll' : {
                        'coreExtensions' : ['mdx', 'md', 'smd', 'gen', 'bin', 'cue', 'iso', 'sms', 'bms', 'gg', 'sg', '68k', 'chd'],
                        'friendlyName' : 'Sega - MS/GG/MD/CD (Genesis Plus GX)'
                        },
                    'gearsystem_libretro.dll' : {
                        'coreExtensions' : ['sms', 'gg', 'sg', 'bin', 'rom'],
                        'friendlyName' : 'Sega - MS/GG/SG-1000 (Gearsystem)'
                        }
                    }
                }
            }
		},
    'Sega ST-V' : { 
		'systemNames' : ['Sega ST-V', 'Sega Titan Video', 'STV'],
		'systemIds' : {
			'igdb' : 52,
			'thegamesdb' : 23
			},
        'libraryType' : 'Games',
		'romExtensions' : ['ccd', 'chd', 'cue', 'iso', 'mds', 'zip'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'kronos_libretro.dll', #default
                    1 : 'kronos_libretro.dll', #Kronos
                    'kronos_libretro.dll' : {
                        'coreExtensions' : ['ccd', 'chd', 'cue', 'iso', 'mds', 'zip', 'm3u'],
                        'friendlyName' : 'Sega - Saturn/ST-V (Kronos)'
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['dx1', 'zip', '2d', '2hd', 'tfd', 'd88', '88d', 'hdm', 'xdf', 'dup', 'tap', 'cmd'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'x1_libretro.dll', #default
                    1 : 'x1_libretro.dll', #X Millennium
                    'x1_libretro.dll' : {
                        'coreExtensions' : ['dx1', 'zip', '2d', '2hd', 'tfd', 'd88', '88d', 'hdm', 'xdf', 'dup', 'tap', 'cmd'],
                        'friendlyName' : 'Sharp X1 (X Millennium)'
                        }
                    }
                }
            }
		},
    'Sharp X68000' : { 
		'systemNames' : ['Sharp X68000', 'x68000'],
		'systemIds' : {
			'igdb' : 121,
			'thegamesdb' : 4931
			},
        'libraryType' : 'Games',
		'romExtensions' : ['dim', 'zip', 'img', 'd88', '88d', 'hdm', 'dup', '2hd', 'xdf', 'hdf', 'cmd'],
		'romType' : 0,
		'multiDisk' : True,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'pk68k_libretro.dll', #default
                    1 : 'pk68k_libretro.dll', #PX68k
                    'pk68k_libretro.dll' : {
                        'coreExtensions' : ['dim', 'zip', 'img', 'd88', '88d', 'hdm', 'dup', '2hd', 'xdf', 'hdf', 'cmd', 'm3u'],
                        'friendlyName' : 'Sharp - X68000 (PX68k)'
                        }
                    }
                }
            }
		},
    'Sinclair ZX 81' : { 
		'systemNames' : ['Sinclair ZX 81', 'ZX 81', 'Sinclair ZX81', 'ZX81'],
		'systemIds' : {
			'igdb' : 373,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
		'romExtensions' : ['p', 'tzx', 't81'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : '81_libretro.dll', #default
                    1 : '81_libretro.dll', #EightyOne
                    '81_libretro.dll' : {
                        'coreExtensions' : ['p', 'tzx', 't81'],
                        'friendlyName' : 'Sinclair - ZX 81 (EightyOne)'
                        }
                    }
                }
            }
		},
    'Sinclair ZX Spectrum' : { 
		'systemNames' : ['Sinclair ZX Spectrum', 'ZX Spectrum', 'ZXS'],
		'systemIds' : {
			'igdb' : 26,
			'thegamesdb' : 4913
			},
        'libraryType' : 'Games',
		'romExtensions' : ['tzx', 'tap', 'z80', 'rzx', 'scl', 'trd'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'fuse_libretro.dll', #default
                    1 : 'fuse_libretro.dll', #Fuse
                    'fuse_libretro.dll' : {
                        'coreExtensions' : ['tzx', 'tap', 'z80', 'rzx', 'scl', 'trd'],
                        'friendlyName' : 'Sinclair - ZX Spectrum (Fuse)'
                        }
                    }
                }
            }
		},
    'SNK Hyper Neo Geo 64' : { 
		'systemNames' : ['SNK Hyper Neo Geo 64', 'Hyper Neo Geo 64'],
		'systemIds' : {
			'igdb' : 135,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['cue', 'chd'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'neocd_libretro.dll', #default
                    1 : 'neocd_libretro.dll', #NeoCD
                    'neocd_libretro.dll' : {
                        'coreExtensions' : ['cue', 'chd'],
                        'friendlyName' : 'SNK - Neo Geo CD (NeoCD)'
                        }
                    }
                }
            }
		},
    'SNK Neo Geo MVS' : { 
		'systemNames' : ['SNK Neo Geo MVS', 'Neo Geo MVS', 'neogeomvs', 'Neo Geo Multi Video System'],
		'systemIds' : {
			'igdb' : 79,
			'thegamesdb' : 24
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['ngp', 'ngc', 'ngpc', 'npc'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mednafen_ngp_libretro.dll', #default
                    1 : 'mednafen_ngp_libretro.dll', #Beetle NeoPop
                    2 : 'race_libretro.dll', #RACE
                    'mednafen_ngp_libretro.dll' : {
                        'coreExtensions' : ['ngp', 'ngc', 'ngpc', 'npc'],
                        'friendlyName' : 'SNK - Neo Geo Pocket / Color (Beetle NeoPop)'
                        },
                    'race_libretro.dll' : {
                        'coreExtensions' : ['ngp', 'ngc', 'ngpc', 'npc'],
                        'friendlyName' : 'SNK - Neo Geo Pocket / Color (RACE)'
                        }
                    }
                }
            }
		},
    'SNK Neo Geo Pocket Color' : { 
		'systemNames' : ['SNK Neo Geo Pocket Color', 'Neo Geo Pocket Color'],
		'systemIds' : {
			'igdb' : 120,
			'thegamesdb' : 4923
			},
        'libraryType' : 'Games',
		'romExtensions' : ['ngp', 'ngc', 'ngpc', 'npc'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mednafen_ngp_libretro.dll', #default
                    1 : 'mednafen_ngp_libretro.dll', #Beetle NeoPop
                    2 : 'race_libretro.dll', #RACE
                    'mednafen_ngp_libretro.dll' : {
                        'coreExtensions' : ['ngp', 'ngc', 'ngpc', 'npc'],
                        'friendlyName' : 'SNK - Neo Geo Pocket / Color (Beetle NeoPop)'
                        },
                    'race_libretro.dll' : {
                        'coreExtensions' : ['ngp', 'ngc', 'ngpc', 'npc'],
                        'friendlyName' : 'SNK - Neo Geo Pocket / Color (RACE)'
                        }
                    }
                }
            }
		},
    'Sol-20' : { 
		'systemNames' : ['Sol-20'],
		'systemIds' : {
			'igdb' : 237,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['ciso', 'cue', 'elf', 'iso', 'isz', 'cso'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'pcsx2_libretro.dll', #default
                    1 : 'pcsx2_libretro.dll', #PCSX2
                    2 : 'play_libretro.dll', #Play!
                    'pcsx2_libretro.dll' : {
                        'coreExtensions' : ['elf', 'iso', 'ciso', 'cue', 'bin'],
                        'friendlyName' : 'Sony - PlayStation 2 (PCSX2)'
                        },
                    'play_libretro.dll' : {
                        'coreExtensions' : ['iso', 'isz', 'cso', 'bin', 'elf'],
                        'friendlyName' : 'Sony - PlayStation 2 (Play!)'
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
        'libraryType' : 'Games',
		'romExtensions' : ['bin'],
		'romType' : 1,
		'multiDisk' : False,
        'emulators' : {
            0 : 'rpcs3', #agent enums to emulator name
            1 : 'rpcs3',
            'rpcs3' : {}
            }
		},
    'Sony PlayStation 4' : { 
		'systemNames' : ['Sony PlayStation 4', 'PlayStation 4', 'PS4'],
		'systemIds' : {
			'igdb' : 48,
			'thegamesdb' : 4919
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['elf', 'iso', 'cso', 'prx', 'pbp'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'ppsspp_libretro.dll', #default
                    1 : 'ppsspp_libretro.dll', #PPSSPP
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Star Trek Voyager Engine' : { 
		'systemNames' : ['Star Trek Voyager Engine', 'Star Trek Voyager'],
		'systemIds' : {
			'igdb' : 6,
			'thegamesdb' : 1
			},
        'libraryType' : 'Games',
		'romExtensions' : ['pk3'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'vitavoyager_libretro.dll', #default
                    1 : 'vitavoyager_libretro.dll', #vitaVoyager
                    'vitavoyager_libretro.dll' : {
                        'coreExtensions' : ['pk3'],
                        'friendlyName' : 'Star Trek: Voyager - Elite Force (vitaVoyager)'
                        }
                    }
                }
            }
		},
    'Steam VR' : { 
		'systemNames' : ['Steam VR'],
		'systemIds' : {
			'igdb' : 163,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc', 'bs', 'st', 'gb', 'gbc', 'bml', 'rom', 'zip'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'snes9x_libretro.dll', #default
                    1 : 'higan_sfc_libretro.dll', #higan Accuracy
                    2 : 'higan_sfc_balanced_libretro.dll', #nSide Balanced
                    3 : 'mednafen_snes_libretro.dll', #Beetle bsnes
                    4 : 'mednafen_supafaust_libretro.dll', #Beetle Supafaust
                    5 : 'bsnes2014_accuracy_libretro.dll', #bsnes 2014 Accuracy
                    6 : 'bsnes2014_balanced_libretro.dll', #bsnes 2014 Balanced
                    7 : 'bsnes2014_performance_libretro.dll', #bsnes 2014 Performance
                    8 : 'bsnes_cplusplus98_libretro.dll', #bsnes C++98(v085)
                    9 : 'bsnes_libretro.dll', #bsnes
                    10 : 'bsnes_hd_beta_libretro.dll', #bsnes-hd beta
                    11 : 'bsnes_mercury_accuracy_libretro.dll', #bsnes-mercury Accuracy
                    12 : 'bsnes_mercury_balanced_libretro.dll', #bsnes-mercury Balanced
                    13 : 'bsnes_mercury_performance_libretro.dll', #bsnes-mercury Performance
                    14 : 'snes9x_libretro.dll', #Snes9x - Current
                    15 : 'snes9x2002_libretro.dll', #Snes9x 2002
                    16 : 'snes9x2005_plus_libretro.dll', #Snes9x 2005 Plus
                    17 : 'snes9x2005_libretro.dll', #Snes9x 2005
                    18 : 'snes9x2010_libretro.dll', #Snes9x 2010
                    19 : 'mesen-s_libretro.dll', #Mesen-S
                    'higan_sfc_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom'],
                        'friendlyName' : 'Nintendo - SNES / Famicom (higan Accuracy)'
                        },
                    'higan_sfc_balanced_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc', 'bml', 'rom'],
                        'friendlyName' : 'Nintendo - SNES / Famicom (nSide Balanced)'
                        },
                    'mednafen_snes_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'bs', 'st', 'sfc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Beetle bsnes)'
                        },
                    'mednafen_supafaust_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Beetle Supafaust)'
                        },
                    'bsnes2014_accuracy_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes 2014 Accuracy)'
                        },
                    'bsnes2014_balanced_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes 2014 Balanced)'
                        },
                    'bsnes2014_performance_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes 2014 Performance)'
                        },
                    'bsnes_cplusplus98_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes C++98 (v085))'
                        },
                    'bsnes_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc', 'bs'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes)'
                        },
                    'bsnes_hd_beta_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'gb', 'gbc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes-hd beta)'
                        },
                    'bsnes_mercury_accuracy_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes-mercury Accuracy)'
                        },
                    'bsnes_mercury_balanced_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes-mercury Balanced)'
                        },
                    'bsnes_mercury_performance_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'bml'],
                        'friendlyName' : 'Nintendo - SNES / SFC (bsnes-mercury Performance)'
                        },
                    'snes9x_libretro.dll' : {
                        'coreExtensions' : ['smc', 'sfc', 'swc', 'fig', 'bs', 'st'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x - Current)'
                        },
                    'snes9x2002_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x 2002)'
                        },
                    'snes9x2005_plus_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x 2005 Plus)'
                        },
                    'snes9x2005_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x 2005)'
                        },
                    'snes9x2010_libretro.dll' : {
                        'coreExtensions' : ['smc', 'fig', 'sfc', 'gd3', 'gd7', 'dx2', 'bsx', 'swc'],
                        'friendlyName' : 'Nintendo - SNES / SFC (Snes9x 2010)'
                        },
                    'mesen-s_libretro.dll' : {
                        'coreExtensions' : ['sfc', 'smc', 'fig', 'swc', 'bs', 'gb', 'gbc'],
                        'friendlyName' : 'Nintendo - SNES / SFC / Game Boy / Color (Mesen-S)'
                        }
                    }
                }
            }
		},
    'SwanCrystal' : { 
		'systemNames' : ['SwanCrystal'],
		'systemIds' : {
			'igdb' : 124,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Tapwave Zodiac' : { 
		'systemNames' : ['Tapwave Zodiac', 'zod', 'Zodiac', 'Palm OS'],
		'systemIds' : {
			'igdb' : 44,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
		'romExtensions' : ['prc', 'pqa', 'img'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'mu_libretro.dll', #default
                    1 : 'mu_libretro.dll', #Mu
                    'mu_libretro.dll' : {
                        'coreExtensions' : ['prc', 'pqa', 'img'],
                        'friendlyName' : 'Palm OS (Mu)'
                        }
                    }
                }
            }
		},
    'Tatung Einstein' : { 
		'systemNames' : ['Tatung Einstein'],
		'systemIds' : {
			'igdb' : 155,
			'thegamesdb' : None
			},
        'libraryType' : 'Games',
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Texas Instruments TI-99-4A' : { 
		'systemNames' : ['Texas Instruments TI-99-4A', 'Texas Instruments TI-99', 'ti-99'],
		'systemIds' : {
			'igdb' : 129,
			'thegamesdb' : 4953
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : ['fd', 'sap', 'k7', 'm7', 'm5', 'rom'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'theodore_libretro.dll', #default
                    1 : 'theodore_libretro.dll', #Theodore
                    'theodore_libretro.dll' : {
                        'coreExtensions' : ['fd', 'sap', 'k7', 'm7', 'm5', 'rom'],
                        'friendlyName' : 'Thomson - MO/TO (Theodore)'
                        }
                    }
                }
            }
		},
    'Tomb Raider Classic Engine' : { 
		'systemNames' : ['Tomb Raider Classic Engine', 'Tomb Raider Engine', 'Tomb Raider Classic', 'Tomb Raider'],
		'systemIds' : {
			'igdb' : 6,
			'thegamesdb' : 1
			},
        'libraryType' : 'Games',
		'romExtensions' : ['phd', 'psx', 'tr2'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'openlara_libretro.dll', #default
                    1 : 'openlara_libretro.dll', #OpenLara
                    'openlara_libretro.dll' : {
                        'coreExtensions' : ['phd', 'psx', 'tr2'],
                        'friendlyName' : 'Tomb Raider (OpenLara)'
                        }
                    }
                }
            }
		},
    'Tomy Tutor' : { 
		'systemNames' : ['Tomy Tutor'],
		'systemIds' : {
			'igdb' : None,
			'thegamesdb' : 4960
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
    'Wolfenstein 3D Engine' : { 
		'systemNames' : ['Wolfenstein 3D Engine', 'Wolfenstein 3D'],
		'systemIds' : {
			'igdb' : 6,
			'thegamesdb' : 1
			},
        'libraryType' : 'Games',
		'romExtensions' : ['wl6', 'n3d', 'sod', 'sdm', 'wl1', 'pk3', 'exe'],
		'romType' : 0,
		'multiDisk' : False,
        'emulators' : {
            0 : 'retroarch', #agent enums to emulator name
            1 : 'retroarch',
            'retroarch' :
                {'cores' : {
                    0 : 'ecwolf_libretro.dll', #default
                    1 : 'ecwolf_libretro.dll', #ECWolf
                    'ecwolf_libretro.dll' : {
                        'coreExtensions' : ['wl6', 'n3d', 'sod', 'sdm', 'wl1', 'pk3', 'exe'],
                        'friendlyName' : 'Wolfenstein 3D (ECWolf)'
                        }
                    }
                }
            }
		},
    'WonderSwan' : { 
		'systemNames' : ['WonderSwan', 'Bandai WonderSwan'],
		'systemIds' : {
			'igdb' : 57,
			'thegamesdb' : 4925
			},
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
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
        'libraryType' : 'Games',
		'romExtensions' : [],
		'romType' : 0,
		'multiDisk' : False
		},
}
