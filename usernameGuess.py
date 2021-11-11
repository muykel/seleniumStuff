#

from selenium import webdriver
import pyautogui as pyg
import keyboard
import time

def checkOneName(name):
    # pyg.write(name)
    keyboard.write(name) # both keyboard and pyg don't fucking work fuck you
    time.sleep(0.3)
    pyg.press("enter")
    time.sleep(0.3)
    pyg.hotkey('command', 'a')
    time.sleep(0.3)
    pyg.press("backspace")

with open("usernames.txt") as f:
    arr = []
    for line in f:
        arr += line.split(' ')

    arr = list(map(lambda x: x.strip("\n"), arr))

    passwordInput = "$" # password used

    driver = webdriver.Chrome()
    driver.get("https://account.protonmail.com/signup?language=en")
    time.sleep(5)

    # defining the fields on the website
    passwordField = driver.find_element_by_xpath('//*[@id="password"]')
    passwordFieldRepeat = driver.find_element_by_xpath('//*[@id="repeat-password"]')

    # the password field doesn't get reset after a failed attempt
    passwordField.send_keys(passwordInput)
    passwordFieldRepeat.send_keys(passwordInput)

    for i in range(10):
        pyg.press("tab")

    for val in arr:
        checkOneName(val)
        time.sleep(2)