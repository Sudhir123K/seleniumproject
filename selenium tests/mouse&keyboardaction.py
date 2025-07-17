import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(service = Service (ChromeDriverManager().install()))
driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()
driver.implicitly_wait(5)

#mouse actions
action = webdriver.ActionChains(driver)

women = driver.find_element(By.XPATH, "//a[@id='ui-id-4']")
action.move_to_element(women).perform()

top = driver.find_element(By.XPATH, "//a[@id='ui-id-9']")
action.move_to_element(top).perform()


#jacket = driver.find_element(By.XPATH, "//a[@id='ui-id-11']")

#action.move_to_element(jacket).click().perform()

#keyboard actions
kb = driver.find_element(By.ID, "search")
action.click(kb).key_down(Keys.SHIFT).send_keys("Test").key_up(Keys.SHIFT).send_keys(Keys.ENTER).perform()
time.sleep(4)



