from selenium import webdriver
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    @property
    def product_header(self):
        product = self.browser.find_element(By.XPATH, "//div[@data-test='inventory-item-name']")
        return product

    @property
    def checkout_button(self):
        button = self.browser.find_element(By.XPATH, "//button[@data-test='checkout']")
        return button
