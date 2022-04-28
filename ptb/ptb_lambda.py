import json
from telegram.ext import Dispatcher, MessageHandler, Filters
from telegram import Update, Bot

bot = Bot(token="INSERT YOUR TOKEN FROM BOTFATHER HERE")
dispatcher = Dispatcher(bot, None, use_context=True)

def echo(update, context):
    
    chat_id = update.message.chat_id
    chat_user = update.message.from_user
    chat_text = update.message.text
    
    context.bot.send_message(chat_id=chat_id, text= "Message from " + str(chat_user.first_name) + ": \n " + chat_text)

def lambda_handler(event, context):
    
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
   
    try:
        dispatcher.process_update(
            Update.de_json(json.loads(event["body"]), bot)
        )

    except Exception as e:
        print(e)
        return {"statusCode": 500}

    return {"statusCode": 200}

