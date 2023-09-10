import time
import win32gui
import keyboard


discord_open_chat = '"1일 1커밋 목표로 같이 스터디하실 분들 모집합니다" | [ESTsoft] 백엔드 개발자 오르미 3기 - Discord'

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


# print("\n".join("{: 9d} {}".format(h, t) for t, h in getWindowList()))

def find_and_tab_discord():
    hwnd_main = win32gui.FindWindow(None, discord_open_chat)
    if hwnd_main is not None:
        win32gui.SetForegroundWindow(hwnd_main)
    time.sleep(0.5)
    keyboard.press_and_release('tab')