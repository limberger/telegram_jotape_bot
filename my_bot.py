
import os
import sys
from bothandler import BotHandler
import datetime
import requests
import pylunar
import time
import ephem
from pytz import timezone
import pytz

# set the token using
# heroku config:set TELEGRAM_TOKEN='xxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
NOME_DO_BOT="jotape_bot"

if not 'TELEGRAM_TOKEN' in os.environ:
    print('Token nao setado em TELEGRAM_TOKEN', file=sys.stderr)
    sys.exit(2)
token=os.environ['TELEGRAM_TOKEN']
greet_bot = BotHandler(token)  
greetings = ('hello', 'hi', 'greetings', 'sup', 'oi','olá','alo','ola','alô')
now = datetime.datetime.now()

def ajuda(greet_bot, last_chat_id):
    greet_bot.send_message(last_chat_id, "Comandos\n/ajuda - Lista os comandos disponíveis.\n/lua - Fase da lua em Brasilia.\n/sol - dados do sol\n")


def sol(greet_bot, last_chat_id):
    # Brasilia
    bsb = ephem.Observer()
    bsb.lat, bsb.lon = '-15.6982196', '-48.1082429'
    bsb.date =  datetime.datetime.utcnow()
    nascer = bsb.next_rising(ephem.Sun()).datetime().replace(tzinfo=pytz.utc)
    zenite = bsb.next_transit(ephem.Sun()).datetime().replace(tzinfo=pytz.utc)
    por = bsb.next_setting(ephem.Sun()).datetime().replace(tzinfo=pytz.utc)

    unascer = bsb.previous_rising(ephem.Sun()).datetime().replace(tzinfo=pytz.utc)
    uzenite = bsb.previous_transit(ephem.Sun()).datetime().replace(tzinfo=pytz.utc)
    upor = bsb.previous_setting(ephem.Sun()).datetime().replace(tzinfo=pytz.utc)
    greet_bot.send_message(last_chat_id, "Último\nNascer do Sol: %s\n Zênite: %s\n Pôr-do-sol: %s\n---\nPróximo\nNascer do Sol: %s\n Zênite: %s\n Pôr-do-sol: %s\n" %
                           (
                               unascer.astimezone(pytz.timezone('America/Sao_Paulo')),
                               uzenite.astimezone(pytz.timezone('America/Sao_Paulo')),
                               upor.astimezone(pytz.timezone('America/Sao_Paulo')),
                               nascer.astimezone(pytz.timezone('America/Sao_Paulo')) ,
                            zenite.astimezone(pytz.timezone('America/Sao_Paulo')) ,
                            por.astimezone(pytz.timezone('America/Sao_Paulo')) )
                           )




def lua(greet_bot, last_chat_id):
    # Brasilia
    mi = pylunar.MoonInfo((-15, 47, 38), (-47, 52, 58))
    mi.update(datetime.datetime.utcnow())
    percentual = mi.fractional_phase()
    idade = mi.age()
    x = mi.rise_set_times('America/Sao_Paulo')
    nascimento = datetime.datetime(*x[0][1])
    topo = datetime.datetime(*x[1][1])
    por = datetime.datetime(*x[2][1])
    # New Moon.
    # Waxing Crescent.
    # First Quarter.
    # Waxing Gibbous.
    # Full Moon.
    # Waning Gibbous.
    # Last Quarter.
    # Waning Crescent.
    #

    lua = {
    "NEW_MOON" : "Lua nova",
    "WAXING_CRESCENT": "Lua nova crescente ",
    "FIRST_QUARTER" : "Lua cresente",
    "WAXING_GIBBOUS" : "Lua cresente quase cheia",
    "FULL_MOON" : "Lua cheia",
    "WANING_GIBBOUS" : "Lua cheia minguando",
    "LAST_QUARTER":"Lua minguante",
    "WANING_CRESCENT": "Lua minguante quase nova"
    }
    print(mi.phase_name())
    print(mi.magnitude())
    greet_bot.send_message(last_chat_id, "Lua %s.  %.2f percentual de cheia\nIdade %.2f\n"
                                         "Nascimento %s \nÁplice %s\nPor %s\n" %
                           (lua[mi.phase_name()],
                            percentual * 100,
                            idade ,
                            nascimento.strftime("%d/%m/%Y %H:%M:%S"),
                            topo.strftime("%d/%m/%Y %H:%M:%S"),
                                                        por.strftime("%d/%m/%Y %H:%M:%S") ) )


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
                greet_bot.send_message(last_chat_id, "Olá %s!\n Bem vid@ ao grupo!\nMeu nome é %s\n" %
                                       (last_chat_name, NOME_DO_BOT))
                greet_bot.send_message(last_chat_id, "Primeiramente #LulaLivre! :-)")
                greet_bot.send_message(last_chat_id,
                                       "Eu ainda sou meio bobinho, se vocë mandar para mim uma mensagem ajuda eu te digo quais são minhas capacidades.")
                ajuda(greet_bot,last_chat_id)

            if 'left_chat_participant' in msg['message']:
                last_chat_name = msg['message']['left_chat_participant']['first_name']
                greet_bot.send_message(last_chat_id,"Tchau %s!" % last_chat_name)

            if  'text' in msg['message']:
                print("message....")
                last_chat_name = ''
                if 'first_name' in msg['message']['chat']:
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

                elif last_chat_text.lower() == "/ajuda":
                    ajuda(greet_bot,last_chat_id)

                elif last_chat_text.lower() == "/lua":
                    lua(greet_bot,last_chat_id)

                elif last_chat_text.lower() == "/sol":
                    sol(greet_bot,last_chat_id)

                #elif last_chat_text.lower() = 'trendings':


            new_offset = last_update_id + 1

print('Init...',file=sys.stderr)
if __name__ == '__main__':  
    print('Calling main...',file=sys.stderr)
    try:
        main()
    except KeyboardInterrupt:
        exit()
