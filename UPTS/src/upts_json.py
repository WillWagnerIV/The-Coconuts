from os import walk

import pandas as pd
from pandas.io.json import json_normalize

import upts_games

def list_json(jsonpath):

    filelist = []
    jsonlist = []
    for (dirpath, dirnames, filenames) in walk(jsonpath):
        filelist.extend(filenames)
        
    for filename in filelist:
        # print (filename[-5:])
        if filename[-5:] == ".json":
            gn = filename[:-5]
            temp_game = upts_games.upts_game (game_name=gn)
            jsonlist.append(temp_game)

    return jsonlist