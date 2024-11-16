from selenium.webdriver.common.by import By

class LoginError:
    def __init__(self,driver):
        self.driver=driver
    
    def passworderrormsg(self,msg):
        text=self.driver.find_element(By.CSS_SELECTOR , 'div[id="auth-error-message-box"] span[class="a-list-item"]').text
        print(text)
        assert msg==text.lstrip()    
    def passworderrormsg(self,errormsg):
        text=self.driver.find_element(By.CSS_SELECTOR , 'div[id="auth-error-message-box"] span[class="a-list-item"]').text
        print(text)
        assert errormsg==text.lstrip()    