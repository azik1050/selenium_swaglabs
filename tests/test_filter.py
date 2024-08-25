import pytest
from pages.inventory import InventoryPage
from confest import browser


@pytest.mark.parametrize(
    'option', ['lohi', 'hilo', 'az', 'za']
)
def test_filter(browser, option):
    page = InventoryPage(browser)
    assert option == page.filter_value(option)
    browser.get_screenshot_as_file(f'screenshots/filter.png')






