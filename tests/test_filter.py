import pytest
from pages.inventory import InventoryPage
from confest import browser
from utils import highlight

@pytest.mark.parametrize(
    'option', [
        # 'za', 'hilo', 'az',
        'lohi'
    ]
)
def test_filter(browser, option):
    page = InventoryPage(browser)
    assert option == page.filter_value(option)
    highlight(page.filter, browser)
    browser.get_screenshot_as_file(f'screenshots/filter.png')






