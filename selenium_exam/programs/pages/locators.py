from selenium.webdriver.common.by import By

class MainPageLocators():
     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators(): 
    #login_url = (By.XPATH, "//*[@id='login_link']")
    login_form = (By.XPATH, "//*[@id='login_form']/button")
    register_form = (By.XPATH, "//*[@id='register_form']/button")