import time
import keyboard
import requests
from open_discord_chat import * 
from bs4 import BeautifulSoup


# chat_member = {
#     'name': ['강경모', '김나영', '김재민', '오정배', '황병헌', '남정식', '김창환', '이수빈', '김찬양'],
#     'github': ['https://github.com/ggengmo', 'https://github.com/nayeongdev', 'https://github.com/jmkim648',
#                       'https://github.com/Alexmint001', 'https://github.com/Ruler-H', 'https://github.com/sk7556',
#                       'https://github.com/Blood-donation-day', 'https://github.com/hantang820', 'https://github.com/Kimchanyang524']
# }
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


def check_github_message():
    find_and_tab_discord()  # from open_discord_chat.py
    people_to_call = []
    type_and_enter(people_to_call)

# member github 스크랩
def search_member_github():
    for name, github in chat_member.items():
        url = github
        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            print(soup)

        else : 
            print(response.status_code)
    print("제작중")


#디스코드 focus 후 메시지 발송
def type_and_enter(list):
    text = '잔디봇: '
    if list is None:
        text += '오늘 잔디 모두 확인했습니다. 수고하셨습니다.'
        keyboard.write(text)
    else:
        keyboard.write(text)
        call_person(list)
    time.sleep(0.5)
    keyboard.press_and_release('enter')

# ~~님 ~~님, 오늘 잔디~~ text 생성
def call_person(list):
    for item in list:
        text = '@' + item
        keyboard.write(text)
        time.sleep(0.5)
        keyboard.press_and_release('tab')
    text = '님, 오늘 잔디 안 심겨있습니다. 확인해주세요.'
    keyboard.write(text)
