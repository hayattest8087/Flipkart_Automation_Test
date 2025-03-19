from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://www.demoblaze.com")


driver.maximize_window()
driver.execute_script("window.open('https://google.com')")
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])

#save_path = "C:/Users/ACER/Downloads/webpage_screenshot.png"
#driver.save_screenshot(save_path)
input("Enter any button to close the window")


#driver.quit()