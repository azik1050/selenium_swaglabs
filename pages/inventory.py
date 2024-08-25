from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    @property
    def _find_filter(self):
        dropdown = self.browser.find_element(By.XPATH, "//select[@data-test='product-sort-container']")
        _filter = Select(dropdown)
        return _filter

    def filter_value(self, option):
        _filter = self._find_filter
        _filter.select_by_value(option)
        selected_option = self._find_filter.first_selected_option.get_attribute('value')
        return selected_option

    def add_product(self):
        button = self.browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
        button.click()

    @property
    def cart_link(self):
        link = self.browser.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']")
        return link
