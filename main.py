import time
import schedule
import pystray
import sys
from PIL import Image
from check_github import *
from play_ladder import *
import threading

scheduler = schedule.Scheduler()

if __name__ == '__main__':
    image = Image.open("./img/favicon.ico")

    def exit_app(icon, item):
        # 필요하다면 종료 전 데이터 정리
        scheduler.clear()
        icon.stop()
        sys.exit(0)

    def run_schedule():
        while True:
            scheduler.run_pending()
            time.sleep(60)  

    def main():
        scheduler.every().day.at("22:00").do(call_people_to_plant) # from check_github.py

        menu = (
            pystray.MenuItem('Play ladder', play_ladder),
            pystray.MenuItem('Exit', exit_app)
        )
        icon = pystray.Icon("잔디봇", image, "잔디봇", menu)

        schedule_thread = threading.Thread(target=run_schedule)
        schedule_thread.daemon = True
        schedule_thread.start()

        icon.run()

    
    main()
    

