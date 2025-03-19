import pytest
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ✅ Step 1: Set up Chrome Options
options = Options()
options.add_argument("--disable-notifications")  # Disable Chrome notifications
options.add_experimental_option("excludeSwitches", ["enable-automation"])
prefs = {
    "credentials_enable_service":False,
    "profile.password_managed_enabled":False
}
options.add_experimental_option("prefs",prefs)
#options.add_experimental_option("useAutomationExtension", False)


# ✅ Step 2: Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# ✅ Step 3: Open the website
driver.get("https://new-frontend-qa.timespro.com/")
driver.maximize_window()
# ✅ Step 4: Wait for the page to load
wait = WebDriverWait(driver, 15)

# ✅ Step 5: Handle Popup (if exists)
try:
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="evg-exit-intent-popup-email-capture"]/div[2]/button')))
    close_button.click()
    print("✅ Popup closed successfully.")
except Exception as e:
    print("⚠️ No popup found or unable to close it:", e)

# ✅ Step 6: Find and enter login credentials
wait = WebDriverWait(driver , 15)
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ulj-login']/span/div/div/div/div[1]/button/span[1]/span")))
login_button.click()

email_field = wait.until(EC.presence_of_element_located((By.ID, "username_welcome_page")))
email_field.send_keys("qa_test@yopmail.com")  # Enter Email


email_field.send_keys(Keys.TAB)
email_field.send_keys(Keys.ENTER)

# continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Continue')])[1]")))
# continue_button.click()



password_field = wait.until(EC.presence_of_element_located((By.ID, "password_welcome_login")))
password_field.send_keys("Test@123")  # Replace with the correct password

password_field.send_keys(Keys.RETURN)  # Press Enter to log in
print("Login Successfully")
# ✅ Step 8: Close the browser after testing
input("wait for the login to happen")

