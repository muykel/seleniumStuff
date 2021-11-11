#

from selenium import webdriver
import pyautogui as pyg
import time

def checkOneName(name):
    pyg.press("tab")
    # usernameField.send_keys(name)
    # nextButton.click()

with open("usernames.txt") as f:
    arr = []
    for line in f:
        arr += line.split(' ')

    arr = list(map(lambda x: x.strip("\n"), arr))

    passwordInput = "8kfNTRfbrFDf88cM$" # password used

    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get("https://account.protonmail.com/signup?language=en")
    time.sleep(8)

    # defining the fields on the website
    usernameField = driver.find_element_by_xpath('//*[@id="username"]')
    passwordField = driver.find_element_by_xpath('//*[@id="password"]')
    passwordFieldRepeat = driver.find_element_by_xpath('//*[@id="repeat-password"]')
    nextButton = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/main/div[2]/form/button')

    # the password field doesn't get reset after a failed attempt
    passwordField.send_keys(passwordInput)
    passwordFieldRepeat.send_keys(passwordInput)

    for val in arr:
        checkOneName(val)
        print(val)
        time.sleep(0.5)