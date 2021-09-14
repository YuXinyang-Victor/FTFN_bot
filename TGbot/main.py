from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
import constants
import telegram.ext as tg
import responses as resp
import commands_response as cr

print("Bot started. ")              #signal that bot started in python commandline

def start_command_handler(update, context):
    update.message.reply_text(cr.start_response)                       #Do change this later into other text


def help_command_handler(update, context):
    update.message.reply_text(cr.help_response)                       #Do change this later into other text

def msg_handle_interface(update, context):
    received_text = str(update.message.text).lower()
    response_text = resp.respond(received_text)

    update.message.reply_text(response_text)

def error(update, context):
    print(f"update {update} caused error {context.error}")

def main(): 
    updater = tg.Updater(constants.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command_handler))
    dp.add_handler(CommandHandler("help", help_command_handler))

    dp.add_handler(MessageHandler(tg.Filters.text, msg_handle_interface))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()