from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import *

import authenticate
import variables
import commands

updater = Updater(variables.KEY)
dp = updater.dispatcher

def start(update, context):
    keyboard = [['Ok'],['/cancel']]
    user = update.message.from_user.username
    update.message.reply_text(f'''\n
    Hi {user}, You have to verify yourself before proceeding further
Press Ok to move further
    ''',
    reply_markup = ReplyKeyboardMarkup(keyboard)
    )
    return 0

def concent(update, context):
    reply_keyboard = [['Yes'],['No']]
    update.message.reply_text(
            'Do you want to proceed with verification.',
            reply_markup = ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard = True
                )
            )
    return 1

def concent_check(update, context):
    check = update.message.text

    if str(check) == 'Yes':
        update.message.reply_text(
                'Really glad you complied. Return Ok to move forward',
                reply_markup = ReplyKeyboardMarkup([['Ok','/cancel']]),
                )
        return 2
    elif check == 'No':
        update.message.reply_text(
                'Hope next time you come with credentials',
                reply_markup = ReplyKeyboardRemove(),
                )
        return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text(
                'Thanks for your time',
                reply_markup = ReplyKeyboardRemove(),
                )
    return ConversationHandler.END

def commandAdd(update, context):
    response = update.message.text
    if str(response) == '/add':
        update.message.reply_text('use /help to get the list of commands',
                reply_markup = ReplyKeyboardRemove()
                )
        dp.add_handler(CommandHandler('ip_check', commands.IP))
        dp.add_handler(CommandHandler('help', commands.help))
        dp.add_handler(CommandHandler('list', commands.listcmd))
        dp.add_handler(CommandHandler('detail', commands.detail))
    elif str(response) == 'No':
        update.message.reply_text('Than why did you wasted your time to get to this point')
    
    return ConversationHandler.END

def main():
    conv_handler = ConversationHandler(
            entry_points = [CommandHandler('start', start)],
            states = {
                0 : [MessageHandler(Filters.text & ~Filters.command, concent)],
                1 : [MessageHandler(Filters.text & ~Filters.command, concent_check)],
                2 : [MessageHandler(Filters.text & ~Filters.command, authenticate.name)],
                5 : [MessageHandler(Filters.text & ~Filters.command, authenticate.password)],
                6 : [MessageHandler(Filters.text & ~Filters.command, authenticate.check)],
                7 : [MessageHandler(Filters.text & ~Filters.command, authenticate.adding)],
                8 : [CommandHandler('add', commandAdd)]
                },
            fallbacks = [CommandHandler('cancel', cancel)],
    #            conversation_timeout = 15
            )
    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()






