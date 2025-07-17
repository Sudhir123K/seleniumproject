from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select  import Select

from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(service = Service (ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in")

driver.maximize_window()

email_txt = driver.find_element(By.ID, "email")
email_txt.send_keys("testuser123@email.com")
driver.find_element(By.ID, "enterimg").click()



#dropdown code
dropdown = driver.find_element(By.XPATH, "//select[@ng-model='Skill']")
drop = Select(dropdown)

#we can use select method by visible_text
drop.select_by_visible_text('Configuration')

#select by index value
drop.select_by_index(4)

#select by value
drop.select_by_value('Certifications')
print(driver.current_url)

#navigate different URL
driver.get("https://google.com")
print(driver.current_url)

#back to previous url
driver.back()

#referesh the page
driver.refresh()

#back to again chrome url
driver.forward()
