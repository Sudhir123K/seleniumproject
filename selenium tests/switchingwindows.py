from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service = Service (ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

#parent window
par = driver.current_window_handle
print(par)
driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']").click()

#all windows
windows = driver.window_handles

#child window
for win in windows:
    if win != par:
        driver.switch_to.window(win)

driver.find_element(By.XPATH, "//span[contains(text(),'Downloads')]").click()
driver.close()

driver.switch_to.window(par)
driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']").click()

driver.quit()

