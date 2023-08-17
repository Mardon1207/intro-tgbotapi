import requests
import time

BASE_URL = 'https://api.telegram.org/bot'
TOKEN    = "6190918955:AAH6JhL8iWSkLg77mvBbMUJQ1QqLahJGD_g"


def getMe() -> dict:
    '''getting info about the bot'''
    url = f"{BASE_URL}{TOKEN}/getMe"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return False


def getUpdates() -> dict:
    '''getting info about the bot'''
    url = f"{BASE_URL}{TOKEN}/getUpdates"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return False


def sendMessage(chat_id: str, text: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': text
    }

    response = requests.get(url=url, params=payload)

    return response.status_code


def echo():
    uzunlik=len(getUpdates()['result'])
    while True:
        
        if uzunlik !=len(getUpdates()['result']):

            last_update = getUpdates()['result'][-1]
            
            chat_id = getUpdates()['result'][-1]['message']['chat']['id']
            text = getUpdates()['result'][-1]['message']['text']

            sendMessage(chat_id, text)
            uzunlik=len(getUpdates()['result'])

        time.sleep(0.5)

echo()