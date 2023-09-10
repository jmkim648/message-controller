import time
import keyboard
import requests
from open_discord_chat import * 
import datetime
from bs4 import BeautifulSoup

chat_member = {
    '강경모': 'https://github.com/ggengmo',
    '김나영': 'https://github.com/nayeongdev',
    '김재민': 'https://github.com/jmkim648',
    '오정배': 'https://github.com/Alexmint001',
    '황병헌': 'https://github.com/Ruler-H',
    '남정식': 'https://github.com/sk7556',
    '김창환': 'https://github.com/Blood-donation-day',
    '이수빈': 'https://github.com/hantang820',
    '김찬양': 'https://github.com/Kimchanyang524'
}

# 잔디 확인 메시지 발송
def check_github_message():
    find_and_tab_discord()  # from open_discord_chat.py
    people_to_call = search_member_github()
    type_and_enter(people_to_call)

# member ithub주소에서 잔디부분 확인, 잔디 비어있을 경우 list에 넣어서 반환
def search_member_github():
    member_list = []
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")

    for name, github in chat_member.items():
        url = github
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            data_find = soup.find(f'td', {'data-date': today_date})
            text = data_find.get_text()
            if text[:2] == 'No':
                member_list.append(name)
        else : 
            print(response.status_code)
    return member_list

#디스코드 focus 후 메시지 발송
def type_and_enter(list):
    text = '잔디봇: '
    if list is None:
        text += '오늘 잔디 모두 확인했습니다. 수고하셨습니다!'
        keyboard.write(text)
    else:
        keyboard.write(text)
        call_person(list)
    time.sleep(0.1)
    keyboard.press_and_release('enter')

# ~~님 ~~님, 오늘 잔디~~ text 생성
def call_person(list):
    for item in list:
        text = '@' + item
        keyboard.write(text)
        time.sleep(0.1)
        keyboard.press_and_release('tab')
    text = '님, 오늘 잔디 안 심겨있습니다. 확인해주세요!'
    keyboard.write(text)
