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
    for item in data.member.items():
        result_array.append(item[0])
    random.shuffle(result_array)

    for index, item in enumerate(result_array):
        if index < 4:
            team_one.append(item)
        else:
            team_two.append(item)
        
    find_and_tab_discord(data.chat_name)
    #1팀 텍스트
    text = '1팀 : '
    for item in team_one:
        text += item
        text += ' '
    keyboard.write(text)
    time.sleep(0.1)
    keyboard.press_and_release('enter')

    #2팀 텍스트
    text = '2팀 : '
    for item in team_two:
        text += item
        text += ' '
    keyboard.write(text)
    time.sleep(0.1)
    keyboard.press_and_release('enter')
