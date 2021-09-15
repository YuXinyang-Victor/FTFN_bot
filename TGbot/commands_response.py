import fileIO as IO
from random import randint
import talk as tk
import threading

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

        trust_incrs = tk.will_trust_incrs()


        if (trust_incrs):
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
            response = IO.get_an_unlocked_response(user_id, curr_trust)
            


    else:
        response = tk.other_response()

    return response
