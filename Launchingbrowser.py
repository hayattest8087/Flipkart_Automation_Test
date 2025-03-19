from selenium import webdriver
import time

# Attach to the existing Chrome session
options = webdriver.ChromeOptions()
options.debugger_address = "localhost:9222"  # Match the port set in step 1

# No need for Service or ChromeDriverManager when attaching
driver = webdriver.Chrome(options=options)

# Open Facebook in the already running Chrome instance
driver.get("http://www.facebook.com")

time.sleep(10)
driver.quit()
