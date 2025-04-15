# pages/home_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    CLOSE_POPUP = (By.XPATH, "//button[contains(text(),'✕')]")
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    def close_login_popup(self):
        if self.is_element_present(self.CLOSE_POPUP):
            self.click(self.CLOSE_POPUP)

    def search_product(self, product_name):
        self.enter_text(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)
