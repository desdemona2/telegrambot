import os

if __name__ == "__main__":
    exit()

def IP(update, context):
    os.system('curl -s ifconfig.co > ip')
    with open('ip','r') as file:
        value = file.readline()
    update.message.reply_text(value)
    os.system('rm ip')

def help(update, context):
    update.message.reply_text(f'''
    As you are verified user. You can use commands to handle bot
For a list of commands you can use /list,
or to end the session you can use /cancel
            '''
    )

def listcmd(update, context):
    update.message.reply_text('''
    List of commands that you can use to handler your bot
/start  : to start the session
/ip_check   : to check the ip of home server
/help   : to get info about the bot
/list   : to list the commands
/detail : to list your details
    ''')

def detail(update, context):
    user = update.message.from_user
    update.message.reply_text(f'''
    These are your details
id          : {user.id}
firstname   : {user.first_name}
username    : {user.username}
'''
    )





