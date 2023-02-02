from selenium.webdriver.common.by import By

class MainPageLocators():
     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators(): 
    #login_url = (By.XPATH, "//*[@id='login_link']")
    login_form = (By.XPATH, "//*[@id='login_form']/button")
    register_form = (By.XPATH, "//*[@id='register_form']/button")

class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    # Сравнить это 
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    #
    # c этим 
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    #
    ############
    #
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    #
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
 
 #222222222222222222222222222222222222222222222222222222
    
class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link") 
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    WRITING_EMPTY_BASKET=(By.XPATH, "//p[text()='Ваша корзина пуста']")
    # Нажать кнопку перехода в карзину 
    BUTTON_VIEW_TO_BASKET = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
   