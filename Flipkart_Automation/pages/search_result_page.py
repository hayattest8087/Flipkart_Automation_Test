# pages/search_results_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):

    FIRST_PRODUCT_NAME = (By.XPATH, "(//div[contains(@class,'KzDlHZ')])[1]")
    FIRST_PRODUCT_PRICE = (By.XPATH, "(//div[contains(@class,'Nx9bqj')])[1]")

    def get_first_product_name(self):
        return self.get_text(self.FIRST_PRODUCT_NAME)

    def get_first_product_price(self):
        return self.get_text(self.FIRST_PRODUCT_PRICE)

    def click_first_product(self):
        self.click(self.FIRST_PRODUCT_NAME)
