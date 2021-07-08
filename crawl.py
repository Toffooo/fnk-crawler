import time

import requests
from bs4 import BeautifulSoup


bot_token = '1625019619:AAEEZMVL6VS2nsfxZFH_34g4g_KIxovAIbU'
telegram_bot_api_base = 'https://api.telegram.org/bot'
telegram_bot_send_message = '{}{}/sendMessage?chat_id={}&text={}'


def get_value():
    resp = requests.get(
        'https://www.coingecko.com/ru/%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B/fnkcom',
        headers={
            'accept': "*/*",
            'user-agent': (
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
            )
        }
    )
    soup = BeautifulSoup(resp.content, "lxml")
    data = soup.find("span", attrs={"data-coin-id": "13483"})
    return data.text


def send_message():
    price = get_value()

    for chat_id in [557813169, 1149383783]:
        url = telegram_bot_send_message.format(
            telegram_bot_api_base, bot_token, chat_id, price
        )
        requests.post(url)


if __name__ == '__main__':
    while True:
        send_message()
        time.sleep(60)
