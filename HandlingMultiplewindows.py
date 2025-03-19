from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get('http://www.google.com')
driver.execute_script("window.open('http://timespro.com')")
time.sleep(10)
driver.switch_to.window(driver.window_handles[1])

time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)

