# %%
# имя бота @sk_c52_bot

import configparser
import telebot

from c56_extensions import APIExeption
from c56_extensions import APIclass

cfg = configparser.ConfigParser()
cfg.read("c56_bot.ini")

TOKEN = cfg["tg_bot"]["api_token"]
MONEY_KEYS = {
    "доллар": "USD",
    "евро": "EUR",
    "рубль": "RUB",
    "тенге": "KZT",
    "юань": "CNY",
}

bot = telebot.TeleBot(TOKEN)

# %%

# Where USD is the base currency you want to use
# url = "https://open.er-api.com/v6/latest/USD"

greet_messsage = (
    "Здравствуйте!\n"
    "Это бот для проверки курсов валют.\n"
    "Правила использования.\nНеобходимо указать три значения "
    "через пробел: исходная валюта, "
    "валюта перевода, количество.\n"
    " Для получения списка доступных валют"
    " наберите /values"
)

# %%


@bot.message_handler(commands=["start", "help"])
def handle_start_help(message):
    bot.reply_to(message, greet_messsage)


@bot.message_handler(commands=["values"])
def handle_values(message):
    values = [key for key in MONEY_KEYS]
    values = ', '.join(values)
    bot.reply_to(message, f'Доступные валюты : {values}')


@bot.message_handler(content_types=['text'])
def handle_convert(message: telebot.types.Message):
    try:
        result = APIclass.get_price(message.text, MONEY_KEYS)
    except APIExeption as e:
        print(e)
        bot.reply_to(message, f"Ошибка пользователя!\n{e}")
    except Exception as e:
        print(e)
        bot.reply_to(message, f"Не могу обработать команду!\n{e}")
    else:
        bot.reply_to(message, result)


bot.infinity_polling(skip_pending=True)
# %%
