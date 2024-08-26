from selenium import webdriver
from pages.login import LoginPage
import pytest
from random import randint


@pytest.fixture()
def browser():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(url='https://www.saucedemo.com')


    page = LoginPage(chrome_driver)
    page.login('standard_user', 'secret_sauce')

    yield chrome_driver

    chrome_driver.quit()


