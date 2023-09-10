import time
import schedule
from check_github import *

# chat_command = ['사다리', '잔디']


def main():
    schedule.every().day.at("22:00").do(check_github_message) # from check_github.py
    while True:
        schedule.run_pending()
        time.sleep(60)
    # check_github_message()


if __name__ == '__main__':
    main()

