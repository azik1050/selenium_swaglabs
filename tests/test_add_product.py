from confest import browser
from pages.inventory import InventoryPage


def test_add_product(browser):
    page = InventoryPage(browser)
    page.add_product()
    assert page.cart_link == '1'
