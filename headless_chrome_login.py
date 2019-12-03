from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import getpass

# taking username,phone or email as input
username = input("Enter username,email or password\n")
password = getpass.getpass("Enter your Password\n")

# headless chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# a new chrome session
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.implicitly_wait(2)
# driver.maximize_window()

# navigatoe to the application home page
driver.get("https://twitter.com/login")

# get the username textbox
login_field = driver.find_element_by_class_name("js-username-field")
login_field.clear()

# enter username
login_field.send_keys(username)
time.sleep(1)

# get the password text box and clear it
password_field = driver.find_element_by_class_name("js-password-field")
password_field.clear()

# enter password
password_field.send_keys(password)
time.sleep(1)
password_field.submit()
