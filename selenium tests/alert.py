from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service = Service (ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()
#ok or accept alert

driver.find_element (By.ID, "OKTab").click()
time.sleep(2)
driver.switch_to.alert.accept()

#how to dismiss alert
driver.find_element(By.XPATH, "//a[@href='#CancelTab']").click()
driver.find_element(By.ID, "CancelTab").click()
time.sleep(2)
driver.switch_to.alert.dismiss()

#text alert
driver.find_element(By.XPATH, "//a[@href='#Textbox']").click()
driver.find_element(By.ID, "Textbox").click()
time.sleep(2)

tx = driver.switch_to.alert.text
print(tx)
driver.switch_to.alert.send_keys("this is a test alert")
time.sleep(2)
driver.switch_to.alert.accept()
driver.quit()
