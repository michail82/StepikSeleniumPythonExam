import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language ru or other")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
   # time.sleep(3)
    #time.sleep(1000)
    browser.quit()