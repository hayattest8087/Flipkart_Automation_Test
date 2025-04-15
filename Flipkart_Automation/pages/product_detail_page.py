from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductDetailPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    PRODUCT_TITLE = (By.XPATH, "//span[contains(@class, 'VU-ZEz')]")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'CxhGGd')]")

    def get_product_title(self):
       return self.wait.until(EC.presence_of_element_located(self.PRODUCT_TITLE)).text

    def get_product_price(self):
       return self.wait.until(EC.presence_of_element_located(self.PRODUCT_PRICE)).text
