"""This module contains the PalWorldSettings class."""


class PalWorldSettings:
    """Class for Palworld settings. This class is used to manage the default settings string,
    default values, and descriptions for the Palworld game."""

    def __init__(self):
        self.default_settings_string = '[/Script/Pal.PalGameWorldSettings]\nOptionSettings=(Difficulty=None,DayTimeSpeedRate=1.000000,NightTimeSpeedRate=1.000000,ExpRate=1.000000,PalCaptureRate=1.000000,PalSpawnNumRate=1.000000,PalDamageRateAttack=1.000000,PalDamageRateDefense=1.000000,PlayerDamageRateAttack=1.000000,PlayerDamageRateDefense=1.000000,PlayerStomachDecreaceRate=1.000000,PlayerStaminaDecreaceRate=1.000000,PlayerAutoHPRegeneRate=1.000000,PlayerAutoHpRegeneRateInSleep=1.000000,PalStomachDecreaceRate=1.000000,PalStaminaDecreaceRate=1.000000,PalAutoHPRegeneRate=1.000000,PalAutoHpRegeneRateInSleep=1.000000,BuildObjectDamageRate=1.000000,BuildObjectDeteriorationDamageRate=1.000000,CollectionDropRate=1.000000,CollectionObjectHpRate=1.000000,CollectionObjectRespawnSpeedRate=1.000000,EnemyDropItemRate=1.000000,DeathPenalty=All,bEnablePlayerToPlayerDamage=False,bEnableFriendlyFire=False,bEnableInvaderEnemy=True,bActiveUNKO=False,bEnableAimAssistPad=True,bEnableAimAssistKeyboard=False,DropItemMaxNum=3000,DropItemMaxNum_UNKO=100,BaseCampMaxNum=128,BaseCampWorkerMaxNum=15,DropItemAliveMaxHours=1.000000,bAutoResetGuildNoOnlinePlayers=False,AutoResetGuildTimeNoOnlinePlayers=72.000000,GuildPlayerMaxNum=20,PalEggDefaultHatchingTime=72.000000,WorkSpeedRate=1.000000,bIsMultiplay=False,bIsPvP=False,bCanPickupOtherGuildDeathPenaltyDrop=False,bEnableNonLoginPenalty=True,bEnableFastTravel=True,bIsStartLocationSelectByMap=True,bExistPlayerAfterLogout=False,bEnableDefenseOtherGuildPlayer=False,CoopPlayerMaxNum=4,ServerPlayerMaxNum=32,ServerName="Default Palworld Server",ServerDescription="",AdminPassword="",ServerPassword="",PublicPort=8211,PublicIP="",RCONEnabled=False,RCONPort=25575,Region="",bUseAuth=True,BanListURL="https://api.palworldgame.com/api/banlist.txt")'  # pylint: disable=line-too-long
        self.default_values = {
            "Difficulty": "None",
            "DayTimeSpeedRate": "1.000000",
            "NightTimeSpeedRate": "1.000000",
            "ExpRate": "1.000000",
            "PalCaptureRate": "1.000000",
            "PalSpawnNumRate": "1.000000",
            "PalDamageRateAttack": "1.000000",
            "PalDamageRateDefense": "1.000000",
            "PlayerDamageRateAttack": "1.000000",
            "PlayerDamageRateDefense": "1.000000",
            "PlayerStomachDecreaceRate": "1.000000",
            "PlayerStaminaDecreaceRate": "1.000000",
            "PlayerAutoHPRegeneRate": "1.000000",
            "PlayerAutoHpRegeneRateInSleep": "1.000000",
            "PalStomachDecreaceRate": "1.000000",
            "PalStaminaDecreaceRate": "1.000000",
            "PalAutoHPRegeneRate": "1.000000",
            "PalAutoHpRegeneRateInSleep": "1.000000",
            "BuildObjectDamageRate": "1.000000",
            "BuildObjectDeteriorationDamageRate": "1.000000",
            "CollectionDropRate": "1.000000",
            "CollectionObjectHpRate": "1.000000",
            "CollectionObjectRespawnSpeedRate": "1.000000",
            "EnemyDropItemRate": "1.000000",
            "DeathPenalty": "All",
            "bEnablePlayerToPlayerDamage": "False",
            "bEnableFriendlyFire": "False",
            "bEnableInvaderEnemy": "True",
            "bActiveUNKO": "False",
            "bEnableAimAssistPad": "True",
            "bEnableAimAssistKeyboard": "False",
            "DropItemMaxNum": "3000",
            "DropItemMaxNum_UNKO": "100",
            "BaseCampMaxNum": "128",
            "BaseCampWorkerMaxNum": "15",
            "DropItemAliveMaxHours": "1.000000",
            "bAutoResetGuildNoOnlinePlayers": "False",
            "AutoResetGuildTimeNoOnlinePlayers": "72.000000",
            "GuildPlayerMaxNum": "20",
            "PalEggDefaultHatchingTime": "72.000000",
            "WorkSpeedRate": "1.000000",
            "bIsMultiplay": "False",
            "bIsPvP": "False",
            "bCanPickupOtherGuildDeathPenaltyDrop": "False",
            "bEnableNonLoginPenalty": "True",
            "bEnableFastTravel": "True",
            "bIsStartLocationSelectByMap": "True",
            "bExistPlayerAfterLogout": "False",
            "bEnableDefenseOtherGuildPlayer": "False",
            "CoopPlayerMaxNum": "4",
            "ServerPlayerMaxNum": "32",
            "ServerName": '"Default Palworld Server"',
            "ServerDescription": '""',
            "AdminPassword": '""',
            "ServerPassword": '""',
            "PublicPort": "8211",
            "PublicIP": '""',
            "RCONEnabled": "False",
            "RCONPort": "25575",
            "Region": '""',
            "bUseAuth": "True",
            "BanListURL": '"https://api.palworldgame.com/api/banlist.txt"',
        }
        self.descriptions = {
            "Difficulty": "Adjusts the overall difficulty of the game.",
            "DayTimeSpeedRate": "Modifies the speed of in-game time during the day.",
            "NightTimeSpeedRate": "Modifies the speed of in-game time during the night.",
            "ExpRate": "Changes the experience gain rate for both players and creatures.",
            "PalCaptureRate": "Adjusts the rate at which Pal creatures can be captured.",
            "PalSpawnNumRate": "Adjusts the rate at which Pal creatures spawn.",
            "PalDamageRateAttack": "Fine-tunes Pal creature damage dealt.",
            "PalDamageRateDefense": "Fine-tunes Pal creature damage received.",
            "PlayerDamageRateAttack": "Fine-tunes player damage dealt.",
            "PlayerDamageRateDefense": "Fine-tunes player damage received.",
            "PlayerStomachDecreaseRate": "Adjusts the rate at which the player's stomach decreases.",
            "PlayerStaminaDecreaseRate": "Adjusts the rate at which the player's stamina decreases.",
            "PlayerAutoHPRegeneRate": "Adjusts the rate of automatic player health regeneration.",
            "PlayerAutoHpRegeneRateInSleep": "Adjusts the rate of automatic player health regeneration during sleep.",
            "PalStomachDecreaseRate": "Adjusts the rate at which Pal creature stomach decreases.",
            "PalStaminaDecreaseRate": "Adjusts the rate at which Pal creature stamina decreases.",
            "PalAutoHPRegeneRate": "Adjusts the rate of automatic Pal creature health regeneration.",
            "PalAutoHpRegeneRateInSleep": "Adjusts the rate of automatic Pal creature health regeneration during sleep.",
            "BuildObjectDamageRate": "Adjusts the rate at which built objects take damage.",
            "BuildObjectDeteriorationDamageRate": "Adjusts the rate at which built objects deteriorate.",
            "CollectionDropRate": "Adjusts the drop rate of collected items.",
            "CollectionObjectHpRate": "Adjusts the health of collected objects.",
            "CollectionObjectRespawnSpeedRate": "Adjusts the respawn speed of collected objects.",
            "EnemyDropItemRate": "Adjusts the drop rate of items from defeated enemies.",
            "DeathPenalty": "Defines the penalty upon player death (e.g., All, None).",
            "bEnablePlayerToPlayerDamage": "Enables or disables player-to-player damage.",
            "bEnableFriendlyFire": "Enables or disables friendly fire.",
            "bEnableInvaderEnemy": "Enables or disables invader enemies.",
            "bActiveUNKO": "Activates or deactivates UNKO (Unidentified Nocturnal Knock-off).",
            "bEnableAimAssistPad": "Enables or disables aim assist for controllers.",
            "bEnableAimAssistKeyboard": "Enables or disables aim assist for keyboards.",
            "DropItemMaxNum": "Sets the maximum number of dropped items in the game.",
            "DropItemMaxNum_UNKO": "Sets the maximum number of dropped UNKO items in the game.",
            "BaseCampMaxNum": "Sets the maximum number of base camps that can be built.",
            "BaseCampWorkerMaxNum": "Sets the maximum number of workers in a base camp.",
            "DropItemAliveMaxHours": "Sets the maximum time items remain alive after being dropped.",
            "bAutoResetGuildNoOnlinePlayers": "Automatically resets guilds with no online players.",
            "AutoResetGuildTimeNoOnlinePlayers": "Sets the time after which guilds with no online players are automatically reset.",
            "GuildPlayerMaxNum": "Sets the maximum number of players in a guild.",
            "PalEggDefaultHatchingTime": "Sets the default hatching time for Pal eggs.",
            "WorkSpeedRate": "Adjusts the overall work speed in the game.",
            "bIsMultiplay": "Enables or disables multiplayer mode.",
            "bIsPvP": "Enables or disables player versus player (PvP) mode.",
            "bCanPickupOtherGuildDeathPenaltyDrop": "Enables or disables the pickup of death penalty drops from other guilds.",
            "bEnableNonLoginPenalty": "Enables or disables non-login penalties.",
            "bEnableFastTravel": "Enables or disables fast travel.",
            "bIsStartLocationSelectByMap": "Enables or disables the selection of starting locations on the map.",
            "bExistPlayerAfterLogout": "Enables or disables the existence of players after logout.",
            "bEnableDefenseOtherGuildPlayer": "Enables or disables the defense of other guild players.",
            "CoopPlayerMaxNum": "Sets the maximum number of cooperative players in a session.",
            "ServerPlayerMaxNum": "Sets the maximum number of players allowed on the server.",
            "ServerName": "Sets the name of the Palworld server.",
            "ServerDescription": "Provides a description for the Palworld server.",
            "AdminPassword": "Sets the password for server administration.",
            "ServerPassword": "Sets the password for joining the Palworld server.",
            "PublicPort": "Sets the public port for the Palworld server.",
            "PublicIP": "Sets the public IP address for the Palworld server.",
            "RCONEnabled": "Enables or disables Remote Console (RCON) for server administration.",
            "RCONPort": "Sets the port for Remote Console (RCON) communication.",
            "Region": "Sets the region for the Palworld server.",
            "bUseAuth": "Enables or disables server authentication.",
            "BanListURL": "Sets the URL for the server's ban list.",
        }
