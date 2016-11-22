import os
import time
import telepot
import requests
import time
#import random
#import datetime

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].split(" ",1)[0]
    sender = msg['from']['username']
    sendHour = msg['date']
    if(len(msg['text'].split(" ",1)) > 1):
        argument = msg['text'].split(" ",1)[1].strip(" ")
    else:
        argument =""

    commands = ["*motivate*\nSelect a random motivational quote to raise your morale!","*help*\nDisplay all commands","*suggest*\nSuggest a new feature!"]
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
    elif command == '/suggest' or command == '/suggest@TailsBot':
        f = open("suggestions.txt","a")
        if argument != "":
            f.write("User:\t" + str(sender) + "\nDate:\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(sendHour)) + "\ncontent:\t" + argument + "\n\n");
            bot.sendMessage(chat_id, "Suggestion\n\n__" + argument + "__\n\nSuccessfully added to the list", parse_mode = "Markdown")
        else:
            bot.sendMessage(chat_id, "Please, add your suggestion after the command!\nEs:\n/suggest this is my hint!")
bot = telepot.Bot(os.environ['TAILS_KEY'])
bot.message_loop(handle)
print 'I am listening ...'

while 1:
	time.sleep(10)