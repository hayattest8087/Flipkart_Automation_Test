
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(2)
driver.maximize_window()
driver.find_element(By.ID, "justAnInputBox").click()

time.sleep(5)
wait = WebDriverWait(driver, 10)
option = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='choice 6 2 1']")))
option.click()

extracttext = driver.find_element(By.ID,"justAnInputBox").get_attribute("value")
print("Selected Value",extracttext)



