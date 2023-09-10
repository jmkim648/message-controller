import time
import schedule
import pystray
from PIL import Image
from check_github import *
from play_ladder import *


image = Image.open("./img/favicon.ico")


def exit_app(icon, item):
    # 필요하다면 종료 전 데이터 정리
    icon.stop()

def main():
    schedule.every().day.at("22:00").do(call_people_to_plant) # from check_github.py

    menu = (
        pystray.MenuItem('Play ladder', play_ladder),
        pystray.MenuItem('Exit', exit_app)
    )

    icon = pystray.Icon("잔디봇", image, "잔디봇", menu)
    icon.run()

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    main()

