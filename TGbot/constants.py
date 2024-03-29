import math

API_KEY = '1965742244:AAGNlPICQUErHXqRspSwrmupEITZF5rfnRo'

trust_init = 0
touch_init = -1
talk_cnt_init = 0
talk_incrs_init = 0

prob_trust_change_by_touch = 0.55

def probability_of_trust_increase(curr_trust):
    prob_trust_increase = 0.25 - 0.25 * (math.cos((math.pi) * curr_trust / 1000))
    return prob_trust_increase

def probability_of_trust_decrease(prob_trust_increase):
    prob_trust_decrease = prob_trust_change_by_touch - prob_trust_increase
    return prob_trust_decrease

def probability_of_trust_unchanged():
    prob_trust_unchanged = 1 - prob_trust_change_by_touch
    return prob_trust_unchanged

trust_threshold_for_msg = [0, 100, 400, 800, 1400, 2000]
