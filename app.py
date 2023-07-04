#!/usr/bin/python3
from telegram.ext import Updater, MessageHandler, Filters
import tkinter as tk

# Prompt the user for interface preference
print("Choose interface option:")
print("1. Graphical interface")
print("2. Terminal interface")
print("3. Both graphical and terminal interfaces")

option = input("Enter your choice (1/2/3): ")

graphical_interface = False
terminal_interface = False

if option == "1" or option == "3":
    graphical_interface = True

if option == "2" or option == "3":
    terminal_interface = True

if graphical_interface:
    window = tk.Tk()
    window.title("Telegram Bot")
    message_listbox = tk.Listbox(window, width=50)
    message_listbox.pack()

def handle_message(update, context):
    message = update.effective_message
    if message:
        text = message.text
        chat_id = message.chat_id
        if terminal_interface:
            print(f"Received message from {chat_id}: {text}")

        with open("messages.txt", "a") as file:
            file.write(f"From: {chat_id}\n")
            file.write(f"Message: {text}\n\n")

        if graphical_interface:
            message_listbox.insert(tk.END, f"From: {chat_id}\nMessage: {text}\n")

updater = Updater('Token', use_context=True)  # Replace 'YOUR_BOT_TOKEN' with your actual bot token

dispatcher = updater.dispatcher

message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
dispatcher.add_handler(message_handler)

updater.start_polling()

if graphical_interface:
    window.mainloop()
