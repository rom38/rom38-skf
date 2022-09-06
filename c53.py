# %%

import configparser
import telebot


cfg = configparser.ConfigParser()
cfg.read('tg_bot.ini')

TOKEN = cfg['tg_bot']['api_token']

bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, f'привет: {message.chat.username}')

@bot.message_handler(commands=['hello'])
def handle_start_salute(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'Привет: {message.chat.username}!!!')

@bot.message_handler(content_types=['photo'])
def handle_rep_pict(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

bot.polling(none_stop=True)
# %%
