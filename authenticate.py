from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import *

import variables

name_key = None

if __name__ == "__main__":
    exit()

def name(update, context):
    update.message.reply_text(
            'Please enter the registered username: ',
            reply_markup = ReplyKeyboardRemove()
            )
    return 5

def password(update, context):
    global name_key
    name_key = str(update.message.text)
    if name_key in variables.credentials:
        update.message.reply_text('Please Provide the pass-key')
        return 6
    else: 
        update.message.reply_text('This username is not available in database, Register or get a new name')
        return ConversationHandler.END

def check(update, context):
    pass_key = update.message.text
    if variables.credentials.get(name_key) == str(pass_key):
        update.message.reply_text('You are verified. Press Ok to proceed',
                reply_markup = ReplyKeyboardMarkup([['Ok'],['/cancel']])
                )
        return 7
    else:
        update.message.reply_text('Pass key you sent isn\'t in database. We are ending conversation now.')
        return ConversationHandler.END

def adding(update, context):
    reply_text = [['/add'],['No']]
    update.message.reply_text(
            'Do you want to import the additional Handlers. Press /add to import',
            reply_markup = ReplyKeyboardMarkup(
                reply_text, one_time_keyboard = True
                )
            )
    return 8






