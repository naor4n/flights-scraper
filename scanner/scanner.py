import os
from selenium import webdriver


class Scanner():
    def __init__(self, driver_path =  r"C:\SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ['PATH'] +=  self.driver_path
        self.driver = webdriver.Chrome()
        
        super(Scanner, self).__init__()

    def get_first_page(self, url = f"https://www.finnair.com/fi-fi"):
        self.get(url)

    def close(self):
        self.driver.quit()