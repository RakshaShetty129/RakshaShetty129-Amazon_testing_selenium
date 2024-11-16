from selenium.webdriver.common.by import By

class signin:
    def __init__(self,driver):
        self.driver = driver
    def number(self,num):
        self.driver.find_element(By.ID ,'ap_email').send_keys(num)
    def continueclick(self):
        self.driver.find_element(By.ID , 'continue').click()
    def enterpassword(self, password):
        self.driver.find_element(By.ID , 'ap_password').send_keys(password)
     
    def forgotpassword(self,forgottext):
        passwordtext=self.driver.find_element(By.ID , 'auth-fpp-link-bottom').text
        print(passwordtext)
        assert forgottext==passwordtext.lstrip()    
    def sinclick(self):
        self.driver.find_element(By.ID , 'signInSubmit').click()
    def verifyname(self,name):
        text=self.driver.find_element(By.ID , 'nav-link-accountList-nav-line-1').text
        print(text)
        textarray=text.split(',')
        print(textarray)
        name_text=textarray[1]
        print(name_text)
        assert name==name_text.lstrip()
        
    def forgotpass(self):
        self.driver.find_element(By.ID , "auth-fpp-link-bottom").click()
        
    
    