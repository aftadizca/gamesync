import json
from gdrive import checkFolderBackup, drive
import os


class GameList:
    def __init__(self, title, location):
        self.title = title
        self.location = location


def get_str_input(text):
    while True:
        try:
            value = str(input(text))
            if value:
                return value
            else:
                raise ValueError
        except ValueError:
            print("Invalid input")


def add_game(title, location):
    bkp = checkFolderBackup()
    # title = get_str_input("Game title : ")
    # location = get_str_input("Game location : ")

    if not os.path.isdir(location):
        print("Game location not found")
        return

    gameList = []

    fileGameList = drive.CreateFile({"id": bkp["fileId"]})
    content = fileGameList.GetContentString()
    if content:
        gameList = json.loads(fileGameList.GetContentString())
        if [game for game in gameList if game["title"] == title]:
            print("Game already in the list")
            return
        gameList.append(GameList(title, location).__dict__)
    else:
        gameList.append(GameList(title, location).__dict__)

    fileGameList.SetContentString(json.dumps(gameList))
    fileGameList.Upload()
