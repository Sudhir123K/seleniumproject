import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="module")
def browser_launch():
 global driver
 driver = webdriver.Chrome(service = Service (ChromeDriverManager().install()))
 yield


def test_printurl(browser_launch):
   driver.get("https://www.programiz.com/python-programming/online-compiler/")

def test_printurl2(browser_launch):
    print(driver.current_url)