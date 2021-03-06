import sys
import json
from config import username, password, recent, interval
from markov import markov
from time import sleep
from numpy.random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

message, cmd_length = None, None
try:
    cmd_length = sys.argv[1]
    if cmd_length.isdigit():
        print(f'Sentence length is {cmd_length}...')
        cmd_length = int(cmd_length) - 1
    else:
        print("Invalid length given...")
except IndexError:
    print("No length given...")

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')
print("browser started...")
sleep(5)

browser.find_element(By.CSS_SELECTOR, "[name='username']").send_keys(username)
browser.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(password)
browser.find_element(By.XPATH, "//button[@type='submit']").click()
print("logged in as " + username + "...")
sleep(5)

browser.get('https://www.instagram.com/direct/inbox/')
sleep(5)

browser.find_element(By.CSS_SELECTOR, "button.aOOlW:nth-child(2)").click()
sleep(5)

print("started messaging...")
while True:
    # * chat = 1 + randint(recent)
    # * randomly messages one of the recent nth chats

    browser.find_element(
        By.XPATH, f"/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{chat}]").click()
    # ? targets most recent nth chat

    # * browser.find_element(By.XPATH, "//*[contains(text(), 'CHAT NAME HERE')]").click()
    # * targets a specific chat

    sleep(5)

    try:
        cmd_length = sys.argv[1]
        if cmd_length.isdigit():
            message = markov(int(cmd_length) - 1)
        else:
            message = markov(randint(30))
    except IndexError:
        message = markov(randint(30))

    sleep(5)
    print(message + "\n")
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Message...']").send_keys(
        message + Keys.ENTER)

    sleep(interval)

browser.close()
