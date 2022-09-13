import decimal
import json
import requests


class APIExeption(Exception):
    pass


class APIclass():
    @staticmethod
    def get_price(message: str, m_keys):
        if len(message.split(" ")) != 3:
            raise APIExeption(
                "Количество значений должно "
                "быть равно трем!")
        src, dst, amount = message.split(" ")
        if src == dst:
            raise APIExeption(
                "Валюты обмена совпадают, "
                "обменять невозможно!")
        try:
            float(amount)
        except ValueError as e:
            raise APIExeption(
                f"Не удалось обработать количество \"{amount}\".\n"
                "Количество валюты должно быть "
                "указано в виде целого числа, либо "
                "числа с плавающей точкой!") from e

        try:
            src_ticker = m_keys[src]
        except KeyError as e:
            raise APIExeption(
                f"Валюта \"{src}\""
                " не поддерживается!") from e
        try:
            dst_ticker = m_keys[dst]
        except KeyError as e:
            raise APIExeption(
                f"Валюта \"{dst}\""
                " не поддерживается!") from e

        # в денежных расчетах удобнее пользоваться decimal вместо float,
        # особенно когда апи самостоятельно не умножает на количество
        amount = decimal.Decimal(amount)
        url = f"https://open.er-api.com/v6/latest/{src_ticker}"
        resp = requests.get(url)
        # мне так больше нравится, не нужно импортировать json,
        # но по условию задачи json необходим
        data = resp.json(parse_float=decimal.Decimal)["rates"][dst_ticker]
        data = data * amount

        result = f"{amount} {src} будут стоить {data} {dst}"
        return result
