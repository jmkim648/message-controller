import keyboard
import random
import time
from data import data
from find_app_handle import * 

result_array = []
#1팀 4명, 2팀 5명
team_one = []
team_two = []

def play_ladder():
    result_array = list(data.member.keys())
    random.shuffle(result_array)
    team_one = result_array[:4]
    team_two = result_array[4:]

    find_and_tab_discord(data.chat_name)
    text = '<사다리 게임>'
    write_and_enter(text)
    #1팀 텍스트
    text = '1팀 : '
    for item in team_one:
        text += item
        text += ' '
    write_and_enter(text)
    #2팀 텍스트
    text = '2팀 : '
    for item in team_two:
        text += item
        text += ' '
    write_and_enter(text)

def write_and_enter(text):
    keyboard.write(text)
    time.sleep(0.1)
    keyboard.press_and_release('enter')