from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import getpass

class log_in():
    def __init__(self,username, password):
        self.username = username
        self.password = password

    def chrome_login(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://twitter.com/login")
        login_field = driver.find_element_by_class_name("js-username-field")
        login_field.clear()
        login_field.send_keys(self.username)
        time.sleep(1)
        password_field = driver.find_element_by_class_name("js-password-field")
        password_field.clear()
        password_field.send_keys(self.password)
        time.sleep(1)
        password_field.submit()

if __name__ == "__main__":
    l = log_in(input("Enter username,email or password\n"),getpass.getpass("Enter your Password\n"))
    l.chrome_login()