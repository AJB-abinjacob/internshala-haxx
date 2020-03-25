from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import names
from passwordgenerator import pwgenerator

# Constants
fakeemail_website = 'https://email-fake.com/'

# Setting up Selenium
driver_fakemail = webdriver.Chrome()

# Starting selenium
print("Starting window for fake email...")
driver_fakemail.get(fakeemail_website)
#time.sleep(5) # waiting for 5 seconds for the website to generate fake email
fake_email_element = driver_fakemail.find_element_by_id("email_ch_text")
fake_email = fake_email_element.text

print("Fake mail generated: ")
print(fake_email)

# Internshala
print("Opening Internshala window...")
internshala_link = 'https://internshala.com/the-grand-summer-internship-fair?utm_source=eap_copylink&utm_medium=3722461'
name_first = names.get_first_name()
name_last = names.get_last_name()
password = pwgenerator.generate()

driver_is = webdriver.Chrome()
driver_is.get(internshala_link)
print("Injecting fake values...")
email_element = driver_is.find_element_by_id("email")
password_element = driver_is.find_element_by_id("password")
name_first_element = driver_is.find_element_by_id("first_name")
name_last_element = driver_is.find_element_by_id("last_name")
button = driver_is.find_element_by_xpath("//button[contains(text(),'Register for the fair')]")
email_element.send_keys(fake_email)
password_element.send_keys(password)
name_first_element.send_keys(name_first)
name_last_element.send_keys(name_last)
#name_last_element.send_keys(Keys.RETURN)
button.click()

print("Values injected successfully.")
time.sleep(1)
print("Waiting for confirmation email...")
while True:
    elements_verif = driver_fakemail.find_elements_by_partial_link_text("Verify")
    print("Checking...")
    if len(elements_verif) == 0:
        time.sleep(2)
    else:
        element_verif = elements_verif[0]
        break

verification_mail = element_verif.get_attribute("href")

print("Opening verification email...")
driver_is.get(verification_mail)
print("!! Done !!")