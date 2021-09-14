def get_trust(user_id):                                         #need to write
#我们希望有一个csv文件存储以下信息，每个row包含user_id，trust, talk_cnt, harass
#user_id是用户的telegram识别id，我会用其他的函数去get，你先假设已经得到了这个值
#trust是当前信任值，精确到小数点后一位。不过python里面可以无视数据类型
#talk_cnt是今日已经进行交谈（就是基建里面的戳）的行为，每日上限暂定20次，不过这些可以再改
#harass是一个很怪的设定，代表你每天可以对她做一次大胆的事情，可能会导致涨好感或者掉好感。如果当日触发掉好感，当天就不能进行交谈了。harass我暂时想用数字来代表今日的情况，比如0代表还没有这么干过，1代表好感涨了，2代表好感掉了
    trust = 0
    return trust # trust 作为一个数字被返回

def get_an_unlocked_response(user_id, curr_trust):              #need to write
    unlocked_response = "x"
    return unlocked_response #return strings, do the randint() HERE!

def update_trust(add_trust):                                    #need to write
    i = 0

def get_harass(user_id):                                        #need to write
    return 0

def get_talk_cnt(user_id):                                      #need to write
    return 0