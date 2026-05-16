import telebot
from transliterate import to_cyrillic, to_latin
bot = telebot.TeleBot("8970169583:AAFgCtDWp2e29dxM8RLjBILfS75LQKcUuVg", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	text = message.text
	if text.isascii():
		bot.reply_to(message, to_cyrillic(text))
	else:
		bot.reply_to(message, to_latin(text))	
	
bot.infinity_polling()