import configparser

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


def get_config():
    config = configparser.ConfigParser()
    config.read('Configurations/config.ini')
    return config


@pytest.fixture(scope="function")
def setup(request):
    config = get_config()
    base_url = config['DEFAULT']['BASE_URL']

    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-cache")
    options.add_argument("--disable-application-cache")

    #create driver with custom options
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(base_url)

    #clear session and local storage
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")

    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver,10)
    yield
    driver.quit()
