
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
greetings = ('hello', 'hi', 'greetings', 'sup', 'oi','olá','alo','ola','alô')
now = datetime.datetime.now()

def main():  
    print('In main',file=sys.stderr)
    new_offset = None
    today = now.day

    while True:
        hour = now.hour
        print("In loop...",file=sys.stderr)
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        print("Last_update len: %s" % len(last_update))
        for msg in last_update:

            last_update_id = msg['update_id']
            last_chat_id = msg['message']['chat']['id']

            print("Last_update_id %s" % msg['update_id'])
            print("Processando <<%s>>\n" % msg)
            if  'new_chat_member' in msg['message']:
                last_chat_name = msg['message']['new_chat_member']['first_name']
                greet_bot.send_message(last_chat_id, "Olá %s!\n Bem vid@ ao grupo!", last_chat_name)

            if 'left_chat_participant' in msg['message']:
                last_chat_name = msg['message']['left_chat_participant']['first_name']
                greet_bot.send_message(last_chat_id,"Tchau %s!", last_chat_name)

            if  'text' in msg['message']:
                print("message....")
                last_chat_name = msg['message']['chat']['first_name']
                last_chat_text = msg['message']['text']

                print("hour %s" % hour)
                print("today %s" % today)
                print("now.day %s" % now.day)
                if last_chat_text.lower() in greetings and today == now.day and 0 <= hour < 12:
                    greet_bot.send_message(last_chat_id, 'Bom dia  {}'.format(last_chat_name))
                    print("Bom dia")
                    today += 1

                elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
                    greet_bot.send_message(last_chat_id, 'Boa tarde {}'.format(last_chat_name))
                    print("Boa tarde")
                    today += 1

                elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
                    greet_bot.send_message(last_chat_id, 'Boa noite  {}'.format(last_chat_name))
                    print("Boa noite")
                    today += 1

                #elif last_chat_text.lower() = 'trendings':


            new_offset = last_update_id + 1

print('Init...',file=sys.stderr)
if __name__ == '__main__':  
    print('Calling main...',file=sys.stderr)
    try:
        main()
    except KeyboardInterrupt:
        exit()
