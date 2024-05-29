import os
from selenium import webdriver

os.environ['PATH'] += "C:\SeleniumDrivers"
driver = webdriver.Chrome()


driver.get("https://www.finnair.com/fi-fi")