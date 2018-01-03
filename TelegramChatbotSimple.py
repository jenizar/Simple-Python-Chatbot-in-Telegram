import json
import requests
import time
import urllib

#import config


#https://api.telegram.org/bot<token>/METHOD_NAME
TOKEN = "533804285:AAEe2rPVteUWZ9wLeCqCb3CH3ilUY_fLae0"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        if text == 'ask':     
           letter1 = 'Python Book Store. We sell Python books :'
           letter2 = '1. Basic Python :  IDR 100.000'
           letter3 = '2. Intermediate Python : IDR 200.000'
           letter4 = '3. Advance Python : IDR 300.000.'
           letter5 = ' Please type : 1, 2, 3'
           text = letter1 + letter2 + letter3 + letter4 + letter5
        elif text == '1':  
           text = 'You choose 1 : Price IDR 100.000.'
        elif text == '2':  
           text = 'You choose 2 : Price IDR 200.000'
        elif text == '3':  
           text = 'You choose 3 : Price IDR 300.000'        
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]  
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    letter1 = 'Python Book Store. We sell Python books :'
    letter2 = '1. Basic Python :  IDR 100.000'
    letter3 = '2. Intermediate Python : IDR 200.000'
    letter4 = '3. Advance Python : IDR 300.000.'
    letter5 = ' Please type : 1, 2, 3' 
    text = letter1 + letter2 + letter3 + letter4 + letter5
    chat = '453469622'    
    send_message(text, chat)
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
      main()