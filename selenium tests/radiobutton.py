
# radio button, checkbox code
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(service = Service (ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in")

email_txt = driver.find_element(By.ID, "email")
email_txt.send_keys("testuser123@email.com")
driver.find_element(By.ID, "enterimg").click()

#radio select
radio_button = driver.find_element(By.XPATH, "//input[@value='Male']")
radio_button.click()

#chckbox code
check_box = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for ele in check_box:
    val = ele.get_attribute("value")
    print(val)

    if val == "Movies":
     ele.click()