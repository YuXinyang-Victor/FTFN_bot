from random import randint
import fileIO as IO
from random import randint
import other_response as other

trust1 = 40
trust2 = 100
trust3 = 150
trust4 = 200

def should_i_respond(user_id):
    condition_talk = IO.get_talk_cnt(user_id)
    condition_harass = IO.get_harass(user_id)
    condition_others = True                     #currently hard-coded as true. This is placeholder that indicates that future addition of conditions can be done here. 

    if(condition_talk & (condition_harass != 2) & condition_others):
        return True
    else:
        return False

def will_trust_incrs():
    value = randint(1, 20)
    return (value/20)

def other_response():
    value = randint(0, len(other.other_response)-1)
    response = other.other_response[value]
    return response

def rnd_trust_incrs():
    value = randint(1, 10)
    return (value/10)

def should_i_alert_new_unlocked_msg(curr_trust1, curr_trust2):
    trust_list = [trust1, trust2, trust3, trust4]

    for i in trust_list:
        if ((curr_trust1 < i) &(curr_trust2 >= i)):
            return True

    return False

def trust_increase():                           #need to write
    return "place_holder_for_trust_increase"

def new_unlocked_msg_alert():                   #need to write
    return "new unlocked message alert placeholder"
