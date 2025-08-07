import configparser
import os

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

    driver = webdriver.Chrome(options=options)
    driver.get(base_url)

    # Optional: Wait for element instead of readyState
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "makeFlex"))  # Example class on MMT
    )

    driver.delete_all_cookies()
    # Commenting out storage clear to prevent access error
    # driver.execute_script("window.localStorage.clear();")
    # driver.execute_script("window.sessionStorage.clear();")

    request.cls.driver = driver
    request.cls.wait = WebDriverWait(driver, 10)
    yield
    driver.quit()

# @pytest.fixture(scope="function")
# def setup(request):
#     config = get_config()
#     base_url = config['DEFAULT']['BASE_URL']
#
#     options = Options()
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_argument("--incognito")
#     options.add_argument("--start-maximized")
#     options.add_argument("--disable-cache")
#     options.add_argument("--disable-application-cache")
#     if os.getenv("CI"):
#         options.add_argument("--headless")
#         options.add_argument("--disable-gpu")
#         options.add_argument("--no-sandbox")
#         options.add_argument("--disable-dev-shm-usage")
#
#     #create driver with custom options
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()
#     driver.get(base_url)
#
#     WebDriverWait(driver, 10).until(
#         lambda d: d.execute_script("return document.readyState") == "complete"
#     )
#
#     driver.delete_all_cookies()
#     try:
#         driver.execute_script("window.localStorage.clear();")
#         driver.execute_script("window.sessionStorage.clear();")
#     except Exception as e:
#         print("Warning: Could not clear local/session storage:", e)
#
#     #clear session and local storage
#     # driver.delete_all_cookies()
#     # driver.execute_script("window.localStorage.clear();")
#     # driver.execute_script("window.sessionStorage.clear();")
#
#     request.cls.driver = driver
#     request.cls.wait = WebDriverWait(driver,10)
#     yield
#     driver.quit()
