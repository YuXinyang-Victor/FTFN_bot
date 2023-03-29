import fileIO as IO
import time
from random import randint
import talk as tk
import threading
import constants as cons
import assist_functions as af

start_response = "私はスカジ、バウンティハンターよ。あなた、本気で私を雇うつもり？私がいれば、厄災を招くかもしれないのよ。"
help_response = "質問がある？私に関して、よくある質問がこちらです。<link_to_description> \n 私がおかしくなった？ケルシーがいないね。じゃ、Dr.North (@FromTheFarNorth)とDr.Carainy (@Carainy)を呼んでください。"

def talk_response(user_id):
    #IO.check_and_create_user_profile(user_id)
    thread_check_create = threading.Thread(target = IO.check_and_create_user_profile, args=(user_id,))                #All changes to the csv file are critical and should follow the multithreading procedure
    thread_check_create.start()
    thread_check_create.join()

    hanndann = tk.should_i_respond(user_id)

    if(hanndann):
        IO.update_talk(user_id)

        trust_incrs = tk.will_trust_incrs(user_id)


        if (trust_incrs):
            IO.update_talk_incrs(user_id)
            response = tk.trust_increase_msg()
            add_trust = tk.rnd_trust_incrs()
            curr_trust1 = IO.get_trust(user_id)

            #IO.update_trust(add_trust, user_id)
            thread_update_trust = threading.Thread(target = IO.update_trust, args = (add_trust,user_id,))
            thread_update_trust.start()
            thread_update_trust.join()

            curr_trust2 = IO.get_trust(user_id)

            alert = tk.should_i_alert_new_unlocked_msg(curr_trust1, curr_trust2)

            if(alert):
                response = tk.new_unlocked_msg_alert()



        else:
            curr_trust = IO.get_trust(user_id)
            response = tk.get_an_unlocked_response(curr_trust)
            


    else:
        response = tk.other_response()

    return response

def touch_response(user_id):
    #IO.check_and_create_user_profile(user_id)
    thread_check_create = threading.Thread(target = IO.check_and_create_user_profile, args=(user_id,))                #All changes to the csv file are critical and should follow the multithreading procedure
    thread_check_create.start()
    thread_check_create.join()

    curr_touch = IO.get_touch(user_id)
    if (curr_touch != -1):
        response = tk.other_response()
        return response

    else: 
        curr_trust = IO.get_trust(user_id)

        prob_trust_increase = cons.probability_of_trust_increase(curr_trust)
        prob_trust_decrease = cons.probability_of_trust_decrease(prob_trust_increase)
        prob_trust_unchanged = cons.probability_of_trust_unchanged()

        value = randint(0,10) / 10

        if (value <= prob_trust_increase):

            IO.update_touch(user_id, 1)

            response = tk.trust_increase_by_touch_msg()
            add_trust = tk.rnd_trust_incrs_by_touch()
            curr_trust1 = IO.get_trust(user_id)

            #IO.update_trust(add_trust, user_id)
            thread_update_trust = threading.Thread(target = IO.update_trust, args = (add_trust,user_id,))
            thread_update_trust.start()
            thread_update_trust.join()

            curr_trust2 = IO.get_trust(user_id)

            alert = tk.should_i_alert_new_unlocked_msg(curr_trust1, curr_trust2)

            if(alert):
                response = tk.new_unlocked_msg_alert()

        elif (value <= (prob_trust_decrease + prob_trust_increase)):

            IO.update_touch(user_id, 2)

            response = tk.trust_decrease_msg()
            decrease_trust = tk.rnd_trust_decrs_by_touch()
            decrease_trust = - decrease_trust

            thread_update_trust = threading.Thread(target = IO.update_trust, args = (decrease_trust,user_id,))
            thread_update_trust.start()
            thread_update_trust.join()

        else:

            IO.update_touch(user_id, 0)

            response = tk.touch_failed_msg()
        
        return response

def check_trust_response(user_id):
    #IO.check_and_create_user_profile(user_id)
    thread_check_create = threading.Thread(target = IO.check_and_create_user_profile, args=(user_id,))                #All changes to the csv file are critical and should follow the multithreading procedure
    thread_check_create.start()
    thread_check_create.join()

    curr_trust = IO.get_trust(user_id)

    response = "my current trust for you is " + str(curr_trust)

    return response

def assist_me_in_JP_VISA():
    #She helps me check Japan VISA application appointment system
    count = af.check_number_accepting()
    if(count!=8):
        response = "ドクター、今ACCEPTINGの数は"+str(count)+"です。変更したから、確認してみようか: https://coubic.com/Embassy-of-Japan/booking_pages#pageContent"
    else:
        response = "ドクター、今ACCEPTINGの数は"+str(count)+"です。確認したいなら: https://coubic.com/Embassy-of-Japan/booking_pages#pageContent"
    return response

def assist_me_in_JP_VISA_2():
    ##Update checking function after Feb 2 update
    changed = af.check_accepting_script()
    if(changed):
        response = "ドクター、予約状況が変更したから、確認してみようか: https://coubic.com/Embassy-of-Japan/booking_pages#pageContent"
    else:
        response = "ドクター、今は満席です。確認したいなら: https://coubic.com/Embassy-of-Japan/booking_pages#pageContent"
    return response

def assist_infinite_polling():
    i = 0
    while (i == 0):
        print("assist polling ...")
        count = af.check_number_accepting()
        if (count != 8):
            response = "ドクター、今ACCEPTINGの数は"+str(count)+"です。変更を気付いたから、確認してみようか: https://coubic.com/Embassy-of-Japan/booking_pages#pageContent"
            return response
        time.sleep(60)

def assist_infinite_polling_2():
    #Update checking function after Feb 2 update
    i = 0
    while (i == 0):
        print("assist polling ...")
        changed = af.check_accepting_script()
        if (changed):
            response = "ドクター、予約状況の変更を気付いたから、確認してみようか: https://coubic.com/Embassy-of-Japan/booking_pages#pageContent"
            return response
        time.sleep(15)


