from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem


# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )




def main():
    mybot = Updater("", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", greet_planet))

    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def greet_planet(bot, update):
    user_planet = update.message.text.split(' ')[1]
    
    if user_planet == 'Mercury':
        constell = ephem.constellation(ephem.Mercury('2018/12/01'))
    elif user_planet == 'Venus':
        constell = ephem.constellation(ephem.Venus('2018/12/01'))
    elif user_planet == 'Mars':
        constell = ephem.constellation(ephem.Mars('2018/12/01'))
    elif user_planet == 'Jupiter':
        constell = ephem.constellation(ephem.Jupiter('2018/12/01'))

    print(constell)

    update.message.reply_text(constell)

# Вызываем функцию - эта строчка собственно запускает бота
main()