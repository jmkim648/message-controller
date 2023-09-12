import time
import win32gui
import keyboard


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

def find_and_tab_discord(app_name):
    hwnd_main = win32gui.FindWindow(None, app_name)
    if hwnd_main is not None:
        keyboard.press("alt")
        win32gui.SetForegroundWindow(hwnd_main)
        keyboard.release("alt")
    time.sleep(0.5)
    keyboard.press_and_release('tab')