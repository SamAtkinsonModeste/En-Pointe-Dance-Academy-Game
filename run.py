# importing json, emoji library ans coloured, cprint fro termcolor
import json
import emoji
import os
from termcolor import colored, cprint
from pyfiglet import Figlet

# font variables
georgiall_font = Figlet(font='georgiall')
doom_font = Figlet(font='doom')
bolger_font = Figlet(font='bolger')

# colours for the print colour function
colours = ['light_grey', 'light_red', 'light_green', 'light_blue', 'light_magenta', 'light_cyan', 'light_yellow']

# story text in json file
with open('dialog-reactions.json', 'r') as file:
    data = json.load(file)