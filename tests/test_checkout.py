from random import randint
from pages.inventory import InventoryPage
from pages.cart import CartPage
from pages.checkout import CheckoutPage
from confest import browser
import pytest


@pytest.mark.parametrize(
    'data', [
        {
            'firstname': '111',
            'lastname': '111',
            'postal': '111'
        }
    ]
)
def test_checkout_fill(data, browser):
    inventory_page = InventoryPage(browser)
    inventory_page.add_product()
    inventory_page.cart_link.click()

    cart_page = CartPage(browser)
    cart_page.checkout_button.click()

    checkout_page = CheckoutPage(browser)
    checkout_page.submit_form(data)
    checkout_page.finnish_button.click()
    assert checkout_page.success_message == 'Thank you for your order!'
    browser.get_screenshot_as_file(f'screenshots/checkout.png')




