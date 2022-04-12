import keyring
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Credentials
USERNAME = 'USERNAME'
PASSWORD = keyring.get_password('chase_password', USERNAME)

options = Options()
options.headless = True

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), 
                           options=options)

driver.get('https://secure03a.chase.com/web/auth/dashboard')

username_field = driver.find_element(By.ID, 'userId-text-input-field')
username_field.send_keys(USERNAME)

password_field = driver.find_element(By.ID, 'password-text-input-field')
password_field.send_keys(PASSWORD)

session = driver.get_cookie('SMSESSION')
print(session)

driver.quit()
