import time
import schedule
from check_github import *
# import check_github

# chat_command = ['사다리', '잔디']

# # 핸들 리스트 받아오기
# def getWindowList():
#     def callback(hwnd, hwnd_list: list):
#         title = win32gui.GetWindowText(hwnd)
#         if win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd) and title:
#             hwnd_list.append((title, hwnd))
#         return True
#     output = []
#     win32gui.EnumWindows(callback, output)
#     return output

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

def main():
    # print("\n".join("{: 9d} {}".format(h, t) for t, h in getWindowList()))

    schedule.every().day.at("22:00").do(check_github_message) # from check_github.py
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    # main()
    print("제작중")

