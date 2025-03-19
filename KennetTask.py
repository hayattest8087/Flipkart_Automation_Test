from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Setting up Webdriver 
options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options =options, service = service)

#expand the browser to maximum
driver.maximize_window()

# Launching the browser with email and Password 
driver.get(" https://gor-pathology.web.app/")
email = driver.find_element(By.NAME,"email")
email.send_keys("test@kennect.io")
password = driver.find_element(By.NAME, "password")
password.send_keys("Qwerty@1234")
login = driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
login.click()


#Wait for Dashboard or navbar to load fully 
WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, "//a[normalize-space()='Patients']")))


# Adding a  Patients 
patients_button = driver.find_element(By.XPATH, "//a[normalize-space()='Patients']")
patients_button.click() 

#Wait for Patient button to load completely
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button/span[normalize-space()='Add Patient']")))

Add_patients = driver.find_element(By.XPATH, "//button/span[normalize-space()='Add Patient']")
Add_patients.click()

# Entering Patient Details 
#1st Page 
Patient_name = driver.find_element(By.NAME,"name")
Patient_name.send_keys("QA")
Patient_email = driver.find_element(By.NAME,"email")
Patient_email.send_keys("qa@yopmail.com")
Patient_phone = driver.find_element(By.NAME,"phone")
Patient_phone.send_keys("7543209876")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
General_details = driver.find_element(By.XPATH,"//button/span[normalize-space()='General Details']")
General_details.click()

#2nd Page 
Patient_height = driver.find_element(By.NAME,"height")
Patient_height.send_keys("177")
Patient_weight = driver.find_element(By.NAME,"weight")
Patient_weight.send_keys("90")

dropdown =WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'MuiSelect-root')]")))
dropdown.click()

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//ul[contains(@class,'MuiList-root')]")))

time.sleep(2)
option_male = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//li[normalize-space()='Male']")))
option_male.click()

Patient_age = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME,"age")))
Patient_age.send_keys("22")
#Patient BloodPressure
Patient_Systolic = driver.find_element(By.NAME,"systolic")
Patient_Systolic.send_keys("122")
Patient_Diastolic = driver.find_element(By.NAME,"diastolic")
Patient_Diastolic.send_keys("90") 
Add_Tests = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[span[contains(text(),'Add Tests')]]")))
driver.execute_script("arguments[0].click();", Add_Tests)

#3rd Page 


dropdown__Add_Tests = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"patient-test")))
dropdown__Add_Tests.click()
for _ in range(4):
    dropdown__Add_Tests.send_keys(Keys.ARROW_DOWN)
dropdown__Add_Tests.send_keys(Keys.RETURN)


dropdown_Add_discounts = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.MuiSelect-root")))
dropdown_Add_discounts.click()

dropdown_select_discounts = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), '10%')]"))
)
dropdown_select_discounts.click()

scroller = "window.scrollTo(0,document.body.scrollHeight * 0.5);"
driver.execute_script(scroller)
time.sleep(3)

plus_icon = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "material-icons")))
plus_icon.click()


dropdown_Equipment_name = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Eqipment Name']"))
)

time.sleep(2)
dropdown_Equipment_name.click()

option_select = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//li[contains(text(),'injection')]")))
option_select.click()

tick_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'MuiIconButton-root')]/span[@class='MuiIconButton-label']/span[text()='check']"))
)
tick_button.click()

input("wait")