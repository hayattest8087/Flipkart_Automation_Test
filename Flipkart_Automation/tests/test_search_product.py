from selenium.webdriver.chrome.webdriver import WebDriver
from pages.home_page import HomePage
from pages.search_result_page import SearchResultsPage
from pages.product_detail_page import ProductDetailPage
import pytest
def test_search_for_product(driver: WebDriver):
    home = HomePage(driver)
    home.close_login_popup()
    home.search_product("iPhone 13")

    search = SearchResultsPage(driver)
    first_name = search.get_first_product_name()
    first_price = search.get_first_product_price()

    print("Search Page →", first_name, first_price)

    search.click_first_product()

    # Switch to new tab
    driver.switch_to.window(driver.window_handles[1])
    try:
     product = ProductDetailPage(driver)
     detail_title = product.get_product_title()
     detail_price = product.get_product_price()

     print("Detail Page →", detail_title, detail_price)
    except Exception as e:
      pytest.fail(f" ProductDetailPage actions failed: {str(e)}")
    
    try:
     assert first_name.split()[0] in detail_title  # Partial match
     assert detail_price is not None
    except Exception as e:
      pytest.fail(f" Assertion failed: {str(e)}")