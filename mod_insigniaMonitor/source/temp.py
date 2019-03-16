# -*- coding: utf-8 -*-
ACHIEVEMENT_CONDITIONS = {
    # медаль                  # условие, текущее значение, граница проверки
    'warrior'                 : {'minFrags': [6, 0, 4]},
    'invader'                 : {'minCapturePts': [80, 0, 60]},
    'sniper'                  : {'minAccuracy': [0.85, 0.0, 0.85],
                                 'minShots'   : [10, 0, 7],
                                 'minDamage'  : [1000, 0, 700]},
    'sniper2'                 : {'minAccuracy'             : [0.85, 0.0, 0.85],
                                 'minDamage'               : [1000, 0, 700],
                                 'minHitsWithDamagePercent': [0.8, 0.0, 0.8],
                                 'sniperDistance'          : [300.0, 0, 300.0],
                                 'minShots'                : [8, 0, 6]},
    'mainGun'                 : {'minDamage'                  : [1000, 0, 1000],
                                 'minDamageToTotalHealthRatio': [0.2, 0, 0.2]},
    'defender'                : {'minPoints': [70, 0, 50]},
    'steelwall'               : {'minDamage': [1000, 0, 700],
                                 'minHits'  : [11, 0, 7]},
    'supporter'               : {'minAssists': [6, 0, 4]},
    'scout'                   : {'minDetections': [9, 0, 5]},
    'evileye'                 : {'minAssists': [6, 0, 3]},
    'medalRadleyWalters'      : {'minLevel': [5, 0, 5],
                                 'minKills': [8, 0, 6],
                                 'maxKills': [9, 0, 6]},
    'medalLafayettePool'      : {'minLevel': [5, 0, 5],
                                 'minKills': [10, 0, 9],
                                 'maxKills': [13, 0, 9]},
    'heroesOfRassenay'        : {'minKills': [14, 0, 13],
                                 'maxKills': [255, 0, 13]},
    'medalOrlik'              : {'minVictimLevelDelta': [1, 0, 1],
                                 'minKills'           : [2, 0, 1]},
    'medalLehvaslaiho'        : {'minVictimLevelDelta': [1, 0, 1],
                                 'minKills'           : [2, 0, 1],
                                 'maxKills'           : [2, 0, 1]},
    'medalOskin'              : {'minVictimLevelDelta': [1, 0, 1],
                                 'minKills'           : [3, 0, 2],
                                 'maxKills'           : [3, 0, 2]},
    'medalNikolas'            : {'minVictimLevelDelta': [1, 0, 1],
                                 'minKills'           : [4, 0, 3],
                                 'maxKills'           : [255, 0, 3]},
    'medalHalonen'            : {'minVictimLevelDelta': [2, 0, 2],
                                 'minKills'           : [2, 0, 1]},
    'medalPascucci'           : {'minKills': [2, 0, 1],
                                 'maxKills': [2, 0, 1]},
    'medalDumitru'            : {'minKills': [3, 0, 2],
                                 'maxKills': [255, 0, 2]},
    'medalBurda'              : {'minVictimLevelDelta': [1, 0, 1],
                                 'minKills'           : [3, 0, 2],
                                 'maxKills'           : [255, 0, 2]},
    'medalBillotte'           : {'hpPercentage': [20, 0, 20],
                                 'minCrits'    : [5, 0, 3],
                                 'minKills'    : [2, 0, 1],
                                 'maxKills'    : [2, 0, 1]},
    'medalBrunoPietro'        : {'hpPercentage': [20, 0, 20],
                                 'minCrits'    : [5, 0, 3],
                                 'minKills'    : [3, 0, 2],
                                 'maxKills'    : [4, 0, 2]},
    'medalTarczay'            : {'hpPercentage': [20, 0, 20],
                                 'minCrits'    : [5, 0, 3],
                                 'minKills'    : [5, 0, 4],
                                 'maxKills'    : [255, 0, 4]},
    'medalKolobanov'          : {'teamDiff': [5, 0, 5]},
    'medalBrothersInArms'     : {'minKills': [3, 0, 3]},
    'medalCrucialContribution': {'minKills': [12, 0, 9]},
    'medalDeLanglade'         : {'minKills': [4, 0, 2]},
    'medalTamadaYoshio'       : {'minKills'           : [2, 0, 1],
                                 'maxKills'           : [255, 0, 1],
                                 'minVictimLevelDelta': [1, 0, 1]},
    'kamikaze'                : {'levelDelta': [1, 0, 1]},
    'huntsman'                : {'minKills': [3, 0, 2]},
    'bombardier'              : {'minKills': [2, 0, 1]},
    'luckyDevil'              : {'radius': [10.99, 0, 10.99]},
    'ironMan'                 : {'minHits': [10, 0, 7]},
    'sturdy'                  : {'minHealth': [10.0, 0, 10.0]},
    'alaric'                  : {'minKills'    : [2, 0, 1],
                                 'minMonuments': [1, 0, 1]},
    'lumberjack'              : {'minKills': [3, 0, 2],
                                 'minTrees': [30, 0, 20]},
    'wolfAmongSheep'          : {'minDamage': [1, 0, 1]},
    'geniusForWar'            : {'minXP': [1, 0, 1]},
    'willToWinSpirit'         : {'enemyCount': [3, 0, 3]},
    'fightingReconnaissance'  : {'maxPosInTopDamager': [3, 0, 3],
                                 'minSpottedCount'   : [2, 0, 1]},
    'monolith'                : {'maxSpeed_ms': [11 / 3.6, 0, 11 / 3.6]},
    'medalAntiSpgFire'        : {'minKills': [2, 0, 2]},
    'medalStark'              : {'minKills': [2, 0, 2],
                                 'hits'    : [2, 0, 2]},
    'medalGore'               : {'minDamageRate': [8, 0, 8],
                                 'minDamage'    : [2000, 0, 1600]},
    'medalCoolBlood'          : {'maxDistance': [100, 0, 100],
                                 'minKills'   : [2, 0, 1]},
    'promisingFighter'        : {'maxPosInTopXPGainer': [3, 0, 3]},
    'heavyFire'               : {'maxPosInTopDamager': [3, 0, 3]},
    'fighter'                 : {'minKills': [4, 0, 3],
                                 'maxKills': [5, 0, 3]},
    'duelist'                 : {'minKills': [2, 0, 1]},
    'bonecrusher'             : {'minCrits': [5, 0, 5]},
    'charmed'                 : {'minVehs': [4, 0, 4]},
    'tacticalAdvantage'       : {'maxLevel': [7, 0, 7]},
    'secretOperations'        : {'minGroupLen': [2, 0, 2]},
    'shoulderToShoulder'      : {'minKills'      : [12, 0, 12],
                                 'minDamageDealt': [30000, 0, 28000]},
    'aloneInTheField'         : {'minDamageDealt': [10000, 0, 9000]},
    'fallenFlags'             : {'minFlags': [4, 0, 4]},
    'effectiveSupport'        : {'minDamageDealt': [2000, 0, 1800]},
    'falloutDieHard'          : {'minKills'      : [5, 0, 5],
                                 'minDamageDealt': [10000, 0, 10000]},
    'predator'                : {'minKills': [5, 0, 5]},
    'champion'                : {'minKills'       : [5, 0, 5],
                                 'minDamageDealt' : [10000, 0, 10000],
                                 'minFlagsCapture': [3, 0, 3]},
    'bannerman'               : {'minFlagsCapture': [4, 0, 4]},
    'ironShield'              : {'minDamage'         : [1800, 0, 1800],
                                 'DestructibleEntity': [150, 0, 150],
                                 'SectorBase'        : [50, 0, 50]},
    'occupyingForce'          : {'minBasePoints': [100, 0, 100]},
    'supremeGun'              : {'minDamageDealt': [10000, 0, 10000]},
    'smallArmy'               : {'minVehiclesDestroyed': [20, 0, 20]}}
ACHIEVEMENT_CONDITIONS_EXT = {'warrior'           : {'minFrags': [8, 0, 6]},
                              'heroesOfRassenay'  : {'minKills': [21, 0, 18],
                                                     'maxKills': [255, 0, 18]},
                              'medalLafayettePool': {'minLevel': [5, 0, 5],
                                                     'minKills': [13, 0, 10],
                                                     'maxKills': [20, 0, 10]},
                              'medalRadleyWalters': {'minLevel': [5, 0, 5],
                                                     'minKills': [10, 0, 8],
                                                     'maxKills': [12, 0, 8]}}