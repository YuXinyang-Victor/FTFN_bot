import telebot
import constants as cons
import responses as resp
import commands_response as cr
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.
logging.basicConfig(filename = "log_for_sept_21.log")

bot = telebot.TeleBot(cons.API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, cr.start_response)

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id, cr.help_response)

@bot.message_handler(commands=['touch'])
def reply_touch(message):
	user_id = message.from_user.id
	touch_response = cr.touch_response(user_id)
	bot.send_message(message.chat.id, touch_response)

@bot.message_handler(commands=['talk'])
def reply_talk(message):
	user_id = message.from_user.id
	talk_response = cr.talk_response(user_id)
	bot.send_message(message.chat.id, talk_response)

@bot.message_handler(commands=['check_trust'])
def reply_check_trust(message):
	user_id = message.from_user.id
	check_trust_response = cr.check_trust_response(user_id)
	bot.send_message(message.chat.id, check_trust_response)

@bot.message_handler(commands=['assist_me'])
def reply_assist(message):
	#Assist you in checking
	assist_response = cr.assist_me_in_JP_VISA_2()
	bot.send_message(message.chat.id, assist_response)
	alert = cr.assist_infinite_polling_2()
	bot.send_message(message.chat.id, alert)
	
	


@bot.message_handler(func=lambda message: True)
def reply_text_msg(message):
	received_text = str(message.text).lower()
	response_text = resp.respond(received_text)
	bot.send_message(message.chat.id, response_text)

print("bot started...")

bot.infinity_polling()