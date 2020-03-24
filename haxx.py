#!/bin/python3
from telethon import TelegramClient, events, sync

api_id = '894187'
api_hash = 'b6bfa22e694d119dc13294062f63e6fd'

# Initialising the Telegram Client
client = TelegramClient("session", api_id, api_hash)
client.start()