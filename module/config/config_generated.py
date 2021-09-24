import datetime

# This file was automatically generated by module/config/db.py.
# Don't modify it manually.


class GeneratedConfig:
    """
    Auto generated configuration
    """

    # Func `Alas`
    Scheduler_Enable = False
    Scheduler_NextRun = datetime.datetime(2020, 1, 1, 0, 0)
    Scheduler_Command = 'Alas'
    Scheduler_SuccessInterval = 0
    Scheduler_FailureInterval = 120
    Scheduler_ServerUpdate = '00:00'
    Emulator_Serial = '127.0.0.1:5555'
    Emulator_PackageName = 'com.bilibili.azurlane'
    Emulator_ScreenshotMethod = 'ADB'  # ADB, uiautomator2, aScreenCap
    Emulator_ControlMethod = 'minitouch'  # ADB, uiautomator2, minitouch
    Error_HandleError = True
    Error_SaveError = True
    Error_ScreenshotLength = 1
    Optimization_CombatScreenshotInterval = 2
    DropRecord_SaveFolder = './screenshots'
    DropRecord_AzurStatsID = None
    DropRecord_SaveResearch = False
    DropRecord_UploadResearch = False
    DropRecord_SaveCommission = False
    DropRecord_UploadCommission = False
    DropRecord_SaveCombat = False

    # Func `General`
    Retirement_Enable = True
    Retirement_RetireMode = 'one_click_retire'  # one_click_retire, enhance, old_retire
    Retirement_RetireAmount = 'retire_all'  # retire_all, retire_10
    Retirement_EnhanceFavourite = False
    Retirement_EnhanceFilter = None
    Retirement_EnhanceCheckPerCategory = 2
    Retirement_OldRetireN = True
    Retirement_OldRetireR = True
    Retirement_OldRetireSR = False
    Retirement_OldRetireSSR = False

    # Func `Restart`

    # Func `Main`
    Campaign_Name = '7-2'
    Campaign_Event = 'campaign_main'
    Campaign_Mode = 'normal'  # normal, hard
    Campaign_UseClearMode = True
    Campaign_UseFleetLock = True
    Campaign_UseAutoSearch = False
    Campaign_Use2xBook = False
    Campaign_AmbushEvade = True
    StopCondition_RunCount = 0
    StopCondition_OilLimit = 1000
    StopCondition_MapAchievement = 'non_stop'  # non_stop, 100_percent_clear, map_3_stars, threat_safe, threat_safe_without_3_stars
    StopCondition_GetNewShip = False
    StopCondition_ReachLevel120 = False
    Fleet_Fleet1 = 1  # 1, 2, 3, 4, 5, 6
    Fleet_Fleet1Formation = 'double_line'  # line_ahead, double_line, diamond
    Fleet_Fleet1Mode = 'combat_auto'  # combat_auto, combat_manual, stand_still_in_the_middle, hide_in_bottom_left
    Fleet_Fleet1Step = 3  # 2, 3, 4, 5
    Fleet_Fleet2 = 2  # 0, 1, 2, 3, 4, 5, 6
    Fleet_Fleet2Formation = 'double_line'  # line_ahead, double_line, diamond
    Fleet_Fleet2Mode = 'combat_auto'  # combat_auto, combat_manual, stand_still_in_the_middle, hide_in_bottom_left
    Fleet_Fleet2Step = 2  # 2, 3, 4, 5
    Fleet_FleetOrder = 'fleet1_mob_fleet2_boss'  # fleet1_mob_fleet2_boss, fleet1_all_fleet2_standby
    Fleet_AutoSearchFleetOrder = 'fleet1_mob_fleet2_boss'  # fleet1_mob_fleet2_boss, fleet1_boss_fleet2_mob, fleet1_all_fleet2_standby, fleet1_standby_fleet2_all
    Submarine_Fleet = 0  # 0, 1, 2
    Submarine_Mode = 'do_not_use'  # do_not_use, hunt_only, every_combat
    Emotion_CalculateEmotion = True
    Emotion_IgnoreLowEmotionWarn = False
    Emotion_Fleet1Value = 119
    Emotion_Fleet1Record = datetime.datetime(2020, 1, 1, 0, 0)
    Emotion_Fleet1Control = 'prevent_yellow_face'  # keep_exp_bonus, prevent_green_face, prevent_yellow_face, prevent_red_face
    Emotion_Fleet1Recover = 'not_in_dormitory'  # not_in_dormitory, dormitory_floor_1, dormitory_floor_2
    Emotion_Fleet1Oath = False
    Emotion_Fleet2Value = 119
    Emotion_Fleet2Record = datetime.datetime(2020, 1, 1, 0, 0)
    Emotion_Fleet2Control = 'prevent_yellow_face'  # keep_exp_bonus, prevent_green_face, prevent_yellow_face, prevent_red_face
    Emotion_Fleet2Recover = 'not_in_dormitory'  # not_in_dormitory, dormitory_floor_1, dormitory_floor_2
    Emotion_Fleet2Oath = False
    HpControl_UseHpBalance = False
    HpControl_UseEmergencyRepair = False
    HpControl_UseLowHpRetreat = False
    HpControl_HpBalanceThreshold = 0.2
    HpControl_HpBalanceWeight = '1000, 1000, 1000'
    HpControl_RepairUseSingleThreshold = 0.3
    HpControl_RepairUseMultiThreshold = 0.6
    HpControl_LowHpRetreatThreshold = 0.3

    # Func `GemsFarming`
    GemsFarming_FlagshipChange = True
    GemsFarming_FlagshipEquipChange = False
    GemsFarming_VanguardChange = False
    GemsFarming_VanguardEquipChange = False
    GemsFarming_LowEmotionRetreat = True
    GemsFarming_CommonCV = 'any'  # any, langley, bogue, ranger, hermes

    # Func `Commission`
    Commission_DoMajorCommission = False
    Commission_CommissionFilter = 'DailyEvent\n> Gem-8 > Gem-4 > Gem-2\n> Box-6 > Box-3 > Box-1\n> DailyCube-0:30 > UrgentCube-1:30 > DailyCube-1:30 > UrgentCube-1:45 > UrgentCube-2:15\n> UrgentCube-3 > DailyCube-3 > UrgentCube-4 > UrgentCube-6\n> Major\n> DailyResource > DailyChip\n> UrgentBook-2:30 > UrgentBook-2 > UrgentBook-1:20 > UrgentBook-1:40\n> Daily-0:20 > Daily-0:30 > Daily-1:00 > Daily-1:30 > Daily-2:00\n> NightOil > NightCube\n> shortest'

    # Func `Tactical`
    Tactical_TacticalFilter = 'SameT3 > SameT2 > SameT1\n> BlueT2 > YellowT2 > RedT2\n> BlueT3 > YellowT3 > RedT3\n> BlueT1 > YellowT1 > RedT1\n> first'

    # Func `Research`
    Research_UseCube = False
    Research_UseCoin = True
    Research_UsePart = True
    Research_PresetFilter = 'series_4'  # custom, series_4, series_3, series_3_than_2
    Research_CustomFilter = '0.5 > reset > shortest'

    # Func `Dorm`
    Dorm_Collect = True
    Dorm_Feed = True
    Dorm_FeedFilter = '20000 > 10000 > 5000 > 3000 > 2000 > 1000'

    # Func `Meowfficer`
    Meowfficer_BuyAmount = 1
    Meowfficer_TrainMeowfficer = False
    Meowfficer_FortChoreMeowfficer = True

    # Func `Guild`
    Logistics_Enable = True
    Logistics_ExchangeFilter = 'PlateTorpedoT1 > PlateAntiAirT1 > PlatePlaneT1 > PlateGunT1 > PlateGeneralT1\n> PlateTorpedoT2 > PlateAntiAirT2 > PlatePlaneT2 > PlateGunT2 > PlateGeneralT2\n> PlateTorpedoT3 > PlateAntiAirT3 > PlatePlaneT3 > PlateGunT3 > PlateGeneralT3\n> OxyCola > Coolant > Merit > Coins > Oil'
    Operation_Enable = True
    Operation_JoinThreshold = 1
    Operation_AttackBoss = True
    Operation_BossFleetRecommend = False

    # Func `Reward`
    Reward_CollectOil = True
    Reward_CollectCoin = True
    Reward_CollectMission = True

    # Func `Shop`
    GeneralShop_UseGems = False
    GeneralShop_Refresh = False
    GeneralShop_Filter = 'BookRedT3 > BookYellowT3 > BookBlueT3 > BookRedT2\n> Cube\n> FoodT6 > FoodT5'
    GuildShop_Refresh = True
    GuildShop_Filter = 'PlateT4 > BookT3 > PRBP > CatT3 > Chips > BookT2 > Retrofit > FoodT6 > FoodT5 > CatT2 > BoxT4'
    GuildShop_BOX_T3 = 'ironblood'  # eagle, royal, sakura, ironblood
    GuildShop_BOX_T4 = 'ironblood'  # eagle, royal, sakura, ironblood
    GuildShop_BOOK_T2 = 'red'  # red, blue, yellow
    GuildShop_BOOK_T3 = 'red'  # red, blue, yellow
    GuildShop_RETROFIT_T2 = 'cl'  # dd, cl, bb, cv
    GuildShop_RETROFIT_T3 = 'cl'  # dd, cl, bb, cv
    GuildShop_PLATE_T2 = 'general'  # general, gun, torpedo, antiair, plane
    GuildShop_PLATE_T3 = 'general'  # general, gun, torpedo, antiair, plane
    GuildShop_PLATE_T4 = 'gun'  # general, gun, torpedo, antiair, plane
    GuildShop_PR1 = 'neptune'  # neptune, monarch, ibuki, izumo, roon, saintlouis
    GuildShop_PR2 = 'seattle'  # seattle, georgia, kitakaze, gascogne
    GuildShop_PR3 = 'champagne'  # champagne, anchorage, august, marcopolo
    MedalShop_Filter = 'DR > PRY\n> BookRedT3 > BookYellowT3 > BookBlueT3 > BookRedT2 > BookYellowT2 > BookBlueT2\n> BulinT2 > RetrofitT3 > PlateGeneralT3\n> FoodT6 > FoodT5'
    MeritShop_Refresh = False
    MeritShop_Filter = 'Cube'

    # Func `Shipyard`
    Shipyard_ResearchSeries = 1
    Shipyard_ShipIndex = 0
    Shipyard_BuyAmount = 2

    # Func `Daily`
    Daily_UseDailySkip = True
    Daily_EscortMission = 'first'  # no, first, second, third
    Daily_EscortMissionFleet = 5  # 1, 2, 3, 4, 5, 6
    Daily_AdvanceMission = 'first'  # no, first, second, third
    Daily_AdvanceMissionFleet = 5  # 1, 2, 3, 4, 5, 6
    Daily_FierceAssault = 'first'  # no, first, second, third
    Daily_FierceAssaultFleet = 5  # 1, 2, 3, 4, 5, 6
    Daily_TacticalTraining = 'second'  # no, first, second, third
    Daily_TacticalTrainingFleet = 5  # 1, 2, 3, 4, 5, 6
    Daily_SupplyLineDisruption = 'second'  # no, first, second, third

    # Func `Hard`
    Hard_HardStage = '11-4'
    Hard_HardFleet = 1  # 1, 2

    # Func `Exercise`
    Exercise_OpponentChooseMode = 'max_exp'  # max_exp, easiest, leftmost, easiest_else_exp
    Exercise_OpponentTrial = 1
    Exercise_ExercisePreserve = 0
    Exercise_LowHpThreshold = 0.4
    Exercise_LowHpConfirmWait = 0.1
    OpponentRefresh_Count = 0
    OpponentRefresh_Record = datetime.datetime(2020, 1, 1, 0, 0)
