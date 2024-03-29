import pandas as pd
from pandas.io.formats.format import format_percentiles
import constants as cons

import threading
#import sys
#print(sys.path)
lock = threading.Lock()

def get_trust(user_id):                                         #need to write
#我们希望有一个csv文件存储以下信息，每个row包含user_id，trust, talk_cnt, touch
#user_id是用户的telegram识别id，我会用其他的函数去get，你先假设已经得到了这个值
#trust是当前信任值，精确到小数点后一位。不过python里面可以无视数据类型
#talk_cnt是今日已经进行交谈（就是基建里面的戳）的行为，每日上限暂定20次，不过这些可以再改
#touch是一个很怪的设定，代表你每天可以对她做一次大胆的事情，可能会导致涨好感或者掉好感。如果当日触发掉好感，当天就不能进行交谈了。touch我暂时想用数字来代表今日的情况，比如0代表还没有这么干过，1代表好感涨了，2代表好感掉了
    user_profile = pd.read_csv('user_profile.csv', index_col = 0)
    trust = user_profile['trust'][user_id]
    return trust # trust 作为一个数字被返回

def update_trust(add_trust, user_id):                                    #need to write lock
    for i in range(10000):
        lock.acquire()
        user_profile = pd.read_csv('user_profile.csv', index_col = 0)
        user_profile.loc[user_profile.index == user_id, 'trust'] += add_trust
        user_profile.to_csv("user_profile.csv")
        print("user" + str(user_id) + " trust updated")
        lock.release()
        return

def get_touch(user_id):                                        #need to write
    user_profile = pd.read_csv('user_profile.csv', index_col = 0)
    touch = user_profile['touch'][user_id]
    return touch     #debug hard code

def get_talk_cnt(user_id):                                      #need to write
    user_profile = pd.read_csv('user_profile.csv', index_col = 0)

    talk_cnt = user_profile['talk_cnt'][user_id]
    return talk_cnt     #debug hard code

def get_talk_incrs(user_id):
    user_profile = pd.read_csv('user_profile.csv', index_col = 0)

    talk_incrs = user_profile['talk_incrs'][user_id]
    return talk_incrs

def check_and_create_user_profile(user_id):                     #need to write lock
    for i in range(10000):
        lock.acquire()
        user_profile = pd.read_csv('user_profile.csv', index_col=0)

        list_of_existing_users = user_profile.index.to_list()

        if (user_id in list_of_existing_users):
            
            lock.release()
            return
        else:
            new_profile = [cons.trust_init, cons.talk_cnt_init, cons.touch_init, cons.talk_incrs_init]
            new_profile_series = pd.Series(new_profile, index = user_profile.columns)
            new_profile_series.name = user_id
            
            user_profile = user_profile.append(new_profile_series)

                
            user_profile.to_csv("user_profile.csv")
                
        
            print("new user created! " + str(user_id))
            lock.release()
            return

def update_talk(user_id):
    for i in range(10000):
        lock.acquire()
        user_profile = pd.read_csv('user_profile.csv', index_col = 0)
        user_profile.loc[user_profile.index == user_id, 'talk_cnt'] += 1

        user_profile.to_csv("user_profile.csv")
        lock.release()
        return

def update_touch(user_id, touch):
    for i in range(10000):
        lock.acquire()
        user_profile = pd.read_csv('user_profile.csv', index_col = 0)
        user_profile.loc[user_profile.index == user_id, 'touch'] = touch

        user_profile.to_csv("user_profile.csv")
        lock.release()
        return

def update_talk_incrs(user_id):
    for i in range(10000):
        lock.acquire()
        user_profile = pd.read_csv('user_profile.csv', index_col = 0)
        user_profile.loc[user_profile.index == user_id, 'talk_incrs'] = 1

        user_profile.to_csv("user_profile.csv")
        lock.release()
        return

def reset_everyday():
    for i in range(10000):
        lock.acquire()
        user_profile = pd.read_csv('user_profile.csv', index_col = 0)
        user_profile['touch'] = -1
        user_profile['talk_cnt'] = 0
        user_profile['talk_incrs'] = 0

        user_profile.to_csv("user_profile.csv")
        lock.release()
        return