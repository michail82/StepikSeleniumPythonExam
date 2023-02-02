from .pages.base_page import BasePage
from .pages.login_page import LoginPage
#from .pages.product_page import BasePage
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_should_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    
def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    
def test_guest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    
# Комманда запуска теста  
# pytest -v --tb=line --language=en test_main_page.py

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
    
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
     page = BasePage(browser, link)
     page.open()
     page.go_to_basket
     time.sleep(10)
     
# Гость открывает главную страницу 
# Переходит в корзину по кнопке в шапке сайта
# Ожидаем, что в корзине нет товаров
# Ожидаем, что есть текст о том что корзина пуста 