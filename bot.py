import requests


BASE_URL = 'https://api.telegram.org/bot'
TOKEN    = "6602447524:AAFuq2qNvn61P7j5ocEdDxoRn0jw8TVAO4Y"


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

    requests.get(url=url, params=payload)

sendMessage('1258594598', 'hi from bot!')
