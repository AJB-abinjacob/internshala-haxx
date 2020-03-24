#!/bin/python3
from telethon import TelegramClient, events, sync

api_id = '894187'
api_hash = 'b6bfa22e694d119dc13294062f63e6fd'

# Initialising the Telegram Client
client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage)
async def response_handler(event):
    # new fake mail
    global fake_mail
    if new_mail_string in event.raw_text:
        words = str(event.raw_text).split(" ")
        for word in words:
            if fake_mail_domain in word:
                fake_mail = word


# Constants for telegram side
generate_count = 0
id_fakemailbot = 'fakemailbot'
new_mail_string = 'Your new fake mail id'
fake_mail = ''
fake_mail_domain = '@hi2.in'

def generate_email():
    client.send_message(id_fakemailbot, "/generate")

client.start()
generate_email()
client.run_until_disconnected()