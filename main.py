import time
from check_github import *
from play_ladder import *
import schedule
# import pystray
# import sys
# from PIL import Image
# import threading

# scheduler = schedule.Scheduler()

# def exit_app(icon, item):
#     # 필요하다면 종료 전 데이터 정리
#     scheduler.clear()
#     icon.stop()
#     sys.exit(0)

# def run_schedule():
#     while True:
#         scheduler.run_pending()
#         time.sleep(60)  

def main():
    # image = Image.open("./img/favicon.ico")
    schedule.every().day.at("22:00").do(call_people_to_plant) # from check_github.py
    # scheduler.every().day.at("22:00").do(call_people_to_plant) # from check_github.py
    # scheduler.every(30).seconds.do(call_people_to_plant) # from check_github.py

    # menu = (
    #     pystray.MenuItem('Play ladder', play_ladder),
    #     pystray.MenuItem('Exit', exit_app)
    # )
    # icon = pystray.Icon("잔디봇", image, "잔디봇", menu)

    # schedule_thread = threading.Thread(target=run_schedule)
    # schedule_thread.daemon = True
    # schedule_thread.start()

    # icon.run()
    while True:
        # scheduler.run_pending()
        schedule.run_pending()
        time.sleep(60) 

if __name__ == '__main__':    
    main()
    

