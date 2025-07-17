from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service (ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

#access frame
s_frame = driver.find_elements(By.XPATH, "//div[@id='Single']/iframe")

driver.switch_to.frame(s_frame[0])

#perform action inside the frame

txt = driver.find_element(By.TAG_NAME, "input")
txt.send_keys("this is a test")

#switch back to main page

driver.switch_to.default_content()
driver.quit()