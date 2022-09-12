# %%

import configparser
from urllib import request
import telebot
import requests
import decimal

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
url = "https://open.er-api.com/v6/latest/USD"

# Making our request
response = requests.get(url)
data = response.json()
# Your JSON object
print(data["rates"]["ANG"])
greet_messsage = (
    "Здравствуйте!\n"
    "Это бот для проверки курсов валют.\n"
    "Правила использования.\nНеобходимо указать три значения "
    "через пробел: исходная валюта, "
    "валюта перевода, количество"
)

print(greet_messsage)
# %%
print(data["rates"])
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
    # inn, out, amount = message.text.split(' ')
    # amount = decimal.Decimal(amount)
    # url = f'https://open.er-api.com/v6/latest/{MONEY_KEYS[inn]}'
    # resp = requests.get(url)
    # data = resp.json(parse_float=decimal.Decimal)['rates'][MONEY_KEYS[out]]
    # data = data * amount

    # result = (f'{amount} {inn} будут стоить {data} {out}')
    try:
        result = APIclass.get_price(message.text, MONEY_KEYS)
    except APIExeption as e:
        print(e)
        bot.reply_to(message, str(e))
    else:
        bot.reply_to(message, result)


bot.polling(none_stop=True, skip_pending=True)
# %%
