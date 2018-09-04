
import os
import sys
from bothandler import BotHandler
import datetime
import requests

# set the token using
# heroku config:set TELEGRAM_TOKEN='xxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

if not 'TELEGRAM_TOKEN' in os.environ:
    print('Token nao setado em TELEGRAM_TOKEN', file=sys.stderr)
    sys.exit(2)
token=os.environ['TELEGRAM_TOKEN']
greet_bot = BotHandler(token)  
greetings = ('hello', 'hi', 'greetings', 'sup')  
now = datetime.datetime.now()

def main():  
    print('In main',file=sys.stderr)
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        print("In loop...",file=sys.stderr)
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Good Morning  {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
            today += 1

        new_offset = last_update_id + 1

print('Init...',file=sys.stderr)
if __name__ == '__main__':  
    print('Calling main...',file=sys.stderr)
    try:
        main()
    except KeyboardInterrupt:
        exit()
