import os
import time
import telepot
import requests
import time
#import random
#import datetime


#TODO: commands should be more complete (including extended syntax)
commands = ["*motivate*\nSelect a random motivational quote to raise your morale!","*help*\nDisplay all commands","*suggest*\nSuggest a new feature!"]
helpMessage = "";
for comm in commands:
    helpMessage += str(comm) + '\n\n'

def handle(msg):
#AREA : command line splitting
    #TODO: IMPROVE SECURITY!!! (parsing, etc...)
    chat_id = msg['chat']['id']
    command = msg['text'].split(" ",1)[0]   #split command and argument
    sender = msg['from']['username']
    sendHour = msg['date']
    if(len(msg['text'].split(" ",1)) > 1):
        argument = msg['text'].split(" ",1)[1].strip(" ")
    else:           # if there's no argument, argument becomes ""
        argument =""
#AREA : command line execution
    print 'Got command: %s' % command       #may be removed or commented in future
    if command == '/motivate' or command == '/motivate@TailsBot':           #TODO: search for other rerpos
    	req = requests.post('http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json')
        try:
            req = req.json()
        except Exception as req:
            f= open("errors.txt","a")
            f.write("User:\t" + str(sender) + "\nDate:\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(sendHour)) + "\ncontent:\t" + req + "\nexception\t" + req + "\n\n");
    	bot.sendMessage(chat_id, str(req['quoteText']) + str('\n') + '_' + str(req['quoteAuthor']) + '_', parse_mode = "Markdown")
    elif command == '/help' or command == '/help@TailsBot':                 #simple help
        bot.sendMessage(chat_id, str(helpMessage), parse_mode = "Markdown")
    elif command == '/suggest' or command == '/suggest@TailsBot':       #TODO: in case /suggest is empty require a text
        f = open("suggestions.txt","a")     #TODO it may be nice to do a binary file for analysis, i guess?
        if argument != "":
            f.write("User:\t" + str(sender) + "\nDate:\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(sendHour)) + "\ncontent:\t" + argument + "\n\n");
            bot.sendMessage(chat_id, "Suggestion\n\n__" + argument + "__\n\nSuccessfully added to the list", parse_mode = "Markdown")
        else:
            bot.sendMessage(chat_id, "Please, add your suggestion after the command!\nEs:\n/suggest this is my hint!")
#AREA : bot execution
bot = telepot.Bot(os.environ['TAILS_KEY'])
bot.message_loop(handle)
print 'I am listening ...'

while 1:
	time.sleep(10)