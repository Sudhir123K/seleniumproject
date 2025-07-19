#in this file we basically keep the data is used over the entire code
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = None
@pytest.fixture(scope="session", autouse=True)
def browser():
    global driver
    if driver is None:
       driver = webdriver.Chrome(service = Service (ChromeDriverManager().install()))
    return driver


