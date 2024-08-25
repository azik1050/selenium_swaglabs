from pages.inventory import InventoryPage
from pages.cart import CartPage
from confest import browser


def test_add_product(browser):
    inventory_page = InventoryPage(browser)
    inventory_page.add_product()
    assert inventory_page.cart_link.text == '1'
    inventory_page.cart_link.click()

    cart_page = CartPage(browser)
    assert type(cart_page.product_header.text) is str
    browser.get_screenshot_as_file(f'screenshots/add_product.png')
