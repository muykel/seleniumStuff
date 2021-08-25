from selenium import webdriver
from selenium import certifi
# driver initialization
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# launch URL
driver.get("https://www.tutorialspoint.com/index.htm")
