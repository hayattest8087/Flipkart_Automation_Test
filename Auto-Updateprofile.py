import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome Driver with Options
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)



# Open Naukri website
driver.get('https://www.naukri.com/')

# ✅ FIX: Use Explicit Wait (WebDriverWait)
wait = WebDriverWait(driver, 10)  # Now 'wait' is correctly defined

try:
    # ✅ FIX: Corrected `until` Syntax (Added Extra Parentheses)
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login_Layer")))
    login_button.click()



    # ✅ FIX: Corrected `until` Syntax for Email Field
    loginemail = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")))
    loginemail.send_keys("khan.hayat66666@gmail.com")

    # ✅ Add Password & Login Click
    
    loginpass = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))
    loginpass.send_keys("mumbaigame")

    loginclick = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Login')]")))
    loginclick.click()

    print("✅ Login Attempted!")
    
except Exception as e:
    print("⚠️ Error Occurred:", e)

finally:
    input("Check the browser and press Enter to close...")
    #driver.quit()

