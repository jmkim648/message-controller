from check_github import *
from play_ladder import *
import pystray
import sys
from PIL import Image

def exit_app(icon, item):
    # 필요하다면 종료 전 데이터 정리
    icon.stop()
    sys.exit(0)

def main():
    image = Image.open("./img/favicon.ico")

    menu = (
        pystray.MenuItem('Plant grass', call_people_to_plant),
        pystray.MenuItem('Play ladder', play_ladder),
        pystray.MenuItem('Exit', exit_app)
    )
    icon = pystray.Icon("잔디봇", image, "잔디봇", menu)
    icon.run()

if __name__ == '__main__':    
    main()