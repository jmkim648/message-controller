import time
import win32gui
import keyboard


discord_open_chat = '"1일 1커밋 목표로 같이 스터디하실 분들 모집합니다" | [ESTsoft] 백엔드 개발자 오르미 3기 - Discord'


def find_and_tab_discord():
    hwnd_main = win32gui.FindWindow(None, discord_open_chat)
    if hwnd_main is not None:
        win32gui.SetForegroundWindow(hwnd_main)
    time.sleep(0.5)
    keyboard.press_and_release('tab')