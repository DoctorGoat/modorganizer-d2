import mobase
from PyQt6.QtCore import QFileInfo

from ..basic_game import BasicGame


class Diablo2(BasicGame):
    Name = "Diablo 2 Plugin"
    Author = "hazel"
    Version = "lmao"

    GameName = "DiabloII"
    GameShortName = "diablo2"
    GameNexusName = "diablo2"
    GameNexusId = 1303
    GameSteamId = 413150
    GameGogId = 1453375253
    GameBinary = "Diablo II.exe"
    GameDataPath = "mods"
    GameDocumentsDirectory = "%GAME_PATH%/plugins"
    GameSavesDirectory = "%GAME_PATH%/Save"
    GameSupportURL = (
        r"https://github.com/ModOrganizer2/modorganizer-basic_games/tree/master/games"
        "Game:"
    )

    def init(self, organizer: mobase.IOrganizer):
        super().init(organizer)
        return True

    def executables(self):
        return [
            mobase.ExecutableInfo(
                "game.exe", QFileInfo(self.gameDirectory(), "game.exe")
            ),
            mobase.ExecutableInfo(
                "Diablo 2", QFileInfo(self.gameDirectory(), "Diablo II.exe")
            ),
			mobase.ExecutableInfo(
                "d2vidtest", QFileInfo(self.gameDirectory(), "d2vidtest.exe")
            ),
        ]
