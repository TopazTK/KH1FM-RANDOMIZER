import tkinter as tk
from tkinter import filedialog
import csv
import json
from pprint import pprint

root = tk.Tk()
root.withdraw()

lua_map = {
    "shorten_go_mode": "1fmRandoShortenGoMode.lua",
    "one_hp": "1fm1HP.lua",
    "four_by_three": "1fm4By3.lua",
    "beep_hack": "1fmBeepHack.lua",
    "consistent_finishers": "1fmConsistentFinishers.lua",
    "early_skip": "1fmEarlySkip.lua",
    "fast_camera": "1fmFastCamera.lua",
    "faster_animations": "1fmFasterAnims.lua",
    "unlock_0_volume": "1fmUnlock0Volume.lua",
    "unskippable": "1fmUnskippable.lua",
    "auto_save": "1fmRandoAutoSave.lua",
    "warp_anywhere": "1fmRandoWarpAnywhere.lua"}


def get_settings_data(settings_file = None):
    while not settings_file:
        settings_file = filedialog.askopenfilename(filetypes =[('JSON', '*.json')], title = "KH1 Randomizer Settings JSON")
        if not settings_file:
            print("Error, please select a valid KH1 settings file")
    with open(settings_file, mode='r') as file:
        settings_data = json.load(file)
    return settings_data

def get_lua_str(lua_file_name):
    with open('./Template Luas/' + lua_file_name, mode = 'r') as file:
        lua_str = file.read()
    return lua_str

def output_lua_file(lua_str, lua_file_name):
    with open('./Working/scripts/' + lua_file_name, mode = 'w') as file:
        file.write(lua_str)

def write_toggleable_luas(settings_file = None):
    settings_data = get_settings_data(settings_file)
    for key in lua_map.keys():
        if settings_data[key]:
            lua_str = get_lua_str(lua_map[key])
            output_lua_file(lua_str, lua_map[key])

if __name__ == "__main__":
    write_toggleable_luas()