import sys
from markov import markov
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

message, cmd_length = None, None
try:
    cmd_length = sys.argv[1]
    if cmd_length.isdigit():
        print(f'Sentence length is {cmd_length}.')
        cmd_length = int(cmd_length) - 1
    else:
        print("Invalid length given.")
except IndexError:
    print("No length given.")

"""
cmd_length = None
try:
    cmd_length = sys.argv[1]

    if cmd_length.isdigit():
        print(markov(int(cmd_length) - 1))
    else:
        print(markov())
except IndexError:
    print(markov())
"""

with open('login.json', 'r') as file:
    json_object = json.load(file)

username = json_object['username']
password = json_object['password']

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')
sleep(3)

#!! is deprecated
#!! browser.find_element_by_css_selector("input[name='username']").send_keys(username)
browser.find_element(By.CSS_SELECTOR, "[name='username']").send_keys(username)

#!! browser.find_element_by_css_selector("input[name='password']").send_keys(password)
browser.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(password)

#!! browser.find_element_by_xpath("//button[@type='submit']").click()
browser.find_element(By.XPATH, "//button[@type='submit']").click()

sleep(3)

browser.get('https://www.instagram.com/direct/inbox/')
sleep(3)

browser.find_element(By.CSS_SELECTOR, "button.aOOlW:nth-child(2)").click()

# browser.find_element(By.XPATH, "/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a").click()
sleep(3)

browser.find_element(By.XPATH, "/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[5]/a").click()

sleep(3)

while true:
    try:
        cmd_length = sys.argv[1]
        if cmd_length.isdigit():
            message = markov(int(cmd_length) - 1)
        else:
            message = markov()
    except IndexError:
        message = markov()


    browser.find_element(By.CSS_SELECTOR, "[placeholder='Message...']").send_keys(
        message + Keys.ENTER)

    sleep(10)

browser.close()