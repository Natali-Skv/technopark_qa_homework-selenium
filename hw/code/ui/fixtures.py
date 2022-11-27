import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.components.login_page import LoginPage
from _pytest.fixtures import FixtureRequest
import os


def get_driver(browser_name):
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=Options())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')

    driver.maximize_window()
    return driver


@pytest.fixture()
def driver(browser_config):
    driver = get_driver(browser_config)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def credentials():
    return str.strip(os.environ["PHONE"]), str.strip(os.environ["CODE"])


@pytest.fixture(scope="session")
def cookies(credentials, url_config, browser_config):
    driver = get_driver(browser_config)
    login_page = LoginPage(driver, url_config)
    login_page.open()
    login_page.login(*credentials)
    cookies = driver.get_cookies()
    driver.quit()
    return cookies