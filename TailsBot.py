import os
import time
#import random
#import datetime
import telepot
import requests

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    commands = ["*motivate*\nselect a random motivational quoteto raise your morale!","*help*\nDisplay all commands"]
    helpMessage = "";
    for comm in commands:
        helpMessage += str(comm) + '\n\n'


    print 'Got command: %s' % command
#leaving some comments for basic functions here
#    if command == '/roll':
#        bot.sendMessage(chat_id,motivationalThings[random.randint(0,25)])
#    elif command == '/time':
#        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    if command == '/motivate' or command == '/motivate@TailsBot':
    	req = requests.post('http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json')
    	req = req.json()
    	bot.sendMessage(chat_id, str(req['quoteText']) + str('\n') + '_' + str(req['quoteAuthor']) + '_', parse_mode = "Markdown")
    elif command == '/help' or command == '/help@TailsBot':
        bot.sendMessage(chat_id, str(helpMessage), parse_mode = "Markdown")
bot = telepot.Bot(os.environ['TAILS_KEY'])
bot.message_loop(handle)
print 'I am listening ...'

while 1:
	time.sleep(10)