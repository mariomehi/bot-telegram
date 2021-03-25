import telebot
API_TOKEN = '1686869327:AAGuBtD0m7ApdkbgxFuLEHxEDy65IIuuEG0'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, """\
Ciao io sono un bot.
Sono stato appena creato e sono decisamente stupido.\
""")
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text=='Ciao':
        bot.reply_to(message, 'Ciao, io sono un bot, come stai?')
    elif message.text=='Bene':
        bot.reply_to(message, 'Bene, mi fa piacere. Anche io!')
    else:
        bot.reply_to(message, 'Sono un pò studido. Non ho capito.')

bot.polling()

https://api.telegram.org/bot1686869327:AAGuBtD0m7ApdkbgxFuLEHxEDy65IIuuEG0/sendMessage?chat_id=-1001416637552&text=123
