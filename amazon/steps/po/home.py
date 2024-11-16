from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.title=""
    def titleverifty(self,title):
        title_captured=self.driver.title
        print(title_captured)
        assert title ==title_captured
    def signin_click(self):
        
        self.driver.find_element(By.ID , 'nav-link-accountList').click()
    
    