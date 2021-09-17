from random import randint
import fileIO as IO
from random import randint

import other_response as other
import trust_messages as tim
import new_unlocked_message_alert as numa

trust1 = 400
trust2 = 1000
trust3 = 1500
trust4 = 2000

def should_i_respond(user_id):
    condition_talk = IO.get_talk_cnt(user_id)
    condition_touch = IO.get_touch(user_id)
    condition_others = True                     #currently hard-coded as true. This is placeholder that indicates that future addition of conditions can be done here. 


    if((condition_talk < 20) & (condition_touch != 2) & condition_others):
        return True
    else:
        return False

def will_trust_incrs():
    value = randint(1, 10)
    return (value // 10)

def other_response():
    value = randint(0, len(other.other_response)-1)
    response = other.other_response[value]
    return response

def rnd_trust_incrs():
    value = randint(1, 10)
    return value

def rnd_trust_incrs_by_touch():
    value = randint(5, 20)
    return value

def rnd_trust_decrs_by_touch():
    value = randint(5, 20)
    return value

def should_i_alert_new_unlocked_msg(curr_trust1, curr_trust2):
    trust_list = [trust1, trust2, trust3, trust4]

    for i in trust_list:
        if ((curr_trust1 < i) &(curr_trust2 >= i)):
            return True

    return False

def trust_increase_msg():                           #need to write
    value = randint(0, len(tim.trust_increase_message)-1)
    response = tim.trust_increase_message[value]
    return response

def trust_decrease_msg():
    value = randint(0, len(tim.trust_decrease_message)-1)
    response = tim.trust_decrease_message[value]
    return response

def new_unlocked_msg_alert():                   #need to write
    value = randint(0, len(numa.new_unlocked_message_alert)-1)
    response = numa.new_unlocked_message_alert[value]
    return response

def trust_increase_by_touch_msg():
    value = randint(0, len(tim.trust_increase_by_touch_message)-1)
    response = tim.trust_increase_by_touch_message[value]
    return response

def touch_failed_msg():
    value = randint(0, len(tim.touch_failed_message)-1)
    response = tim.touch_failed_message[value]
    return response