import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(service = Service (ChromeDriverManager().install()))
driver.get("https://www.redbus.in")
driver.maximize_window()
driver.implicitly_wait(5)

select_date = "20-7-2025"
dates = select_date.split("-")

driver.find_element(By.ID,"onward_cal").click()
td = driver.find_element(By.
//div[@id='rb-calendar_onward_cal']//td"