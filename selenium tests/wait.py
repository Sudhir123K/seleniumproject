from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service = Service (ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='#Multiple']"))).click()


