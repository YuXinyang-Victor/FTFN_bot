import schedule
import time
import fileIO as IO

schedule.every().day.at("00:00").do(IO.reset_everyday)

while True:
    schedule.run_pending()
    time.sleep(0.01)