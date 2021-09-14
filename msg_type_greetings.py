from enum import Enum
class msg_type_greetings_enum(Enum):
    good_morning = 1
    hello = 2
    good_night = 3

handle_dictionary = {"good_morning":"おはよう。",
                     "hello":"身の安全には気を配って、ドクター",
                     "good_night":"寝てるの？おやすみ。水に追われることがない、いい夢を。"
                    }