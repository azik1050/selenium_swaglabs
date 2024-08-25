import pytest
from confest import browser
from pages.inventory import InventoryPage


@pytest.mark.parametrize(
    'option', ['lohi', 'hilo', 'az', 'za']
)
def test_filter(browser, option):
    page = InventoryPage(browser)
    assert option == page.filter_value(option)





