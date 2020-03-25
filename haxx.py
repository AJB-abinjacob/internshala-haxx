#!/bin/python3
from telethon import TelegramClient, events, sync
import names
from passwordgenerator import pwgenerator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
                login_internshala()


# Constants for telegram side
generate_count = 0
id_fakemailbot = 'fakemailbot'
new_mail_string = 'Your new fake mail id'
fake_mail = ''
fake_mail_domain = '@hi2.in'

def generate_email():
    client.send_message(id_fakemailbot, "/generate")

# internshala
driver = webdriver.Chrome()
link = 'https://internshala.com/the-grand-summer-internship-fair?utm_source=eap_copylink&utm_medium=3722461'
def login_internshala():
    global fake_mail
    name_first = names.get_first_name()
    name_last = names.get_last_name()
    password = pwgenerator.generate()
    driver.get(link)
    email_element = driver.find_element_by_id("email")
    password_element = driver.find_element_by_id("password")
    name_first_element = driver.find_element_by_id("first_name")
    name_last_element = driver.find_element_by_id("last_name")
    email_element.send_keys(fake_mail)
    password_element.send_keys(password)
    name_first_element.send_keys(name_first)
    name_last_element.send_keys(name_last)
    #element.send_keys(Keys.RETURN)
    #element.close()

client.start()
generate_email()
client.run_until_disconnected()