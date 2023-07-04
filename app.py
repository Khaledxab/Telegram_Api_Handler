#!/usr/bin/python3
from telegram.ext import Updater, MessageHandler, Filters

def handle_message(update, context):
    message = update.effective_message
    if message:
        text = message.text
        chat_id = message.chat_id
        print(f"Received message from {chat_id}: {text}")

        with open("messages.txt", "a") as file:
            file.write(f"From: {chat_id}\n")
            file.write(f"Message: {text}\n\n")

updater = Updater('token', use_context=True)  # Replace 'YOUR_BOT_TOKEN' with your actual bot token

dispatcher = updater.dispatcher

message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
dispatcher.add_handler(message_handler)

updater.start_polling()
