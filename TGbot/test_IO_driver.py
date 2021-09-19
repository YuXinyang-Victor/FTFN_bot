import fileIO as IO
import threading

thread_update_trust = threading.Thread(target = IO.update_trust, args = (5,707084888,))
thread_update_trust.start()
thread_update_trust.join()

thread_check_create = threading.Thread(target = IO.check_and_create_user_profile, args=(707084888,))                #All changes to the csv file are critical and should follow the multithreading procedure
thread_check_create.start()
thread_check_create.join()

talk_cnt = IO.get_talk_cnt(707084888)
print(talk_cnt)

trust = IO.get_trust(707084888)
print(trust)