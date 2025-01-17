import pytest
from ui.paths import paths
from ui.components.order_history_page import OrderHistoryPage
from ui.base_case.base_case import BaseCase


class TestOrderHistory(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = OrderHistoryPage(driver, url_config)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, set_page):
        self.page.open_path(paths.MAIN)

    def test_order_details(self, authorize, order):
        assert self.page.is_invisible(self.page.locators.ORDER_DETAILS)
        self.page.expand_order_details()
        assert self.page.is_visible(self.page.locators.ORDER_DETAILS)

    def test_close_order_details(self, authorize, order):
        self.page.expand_order_details()
        assert self.page.is_visible(self.page.locators.ORDER_DETAILS)

        self.page.hide_order_details()
        assert self.page.is_invisible(self.page.locators.ORDER_DETAILS)

    def test_go_to_all_restaurants(self, authorize, order):
        self.page.click(self.page.locators.GO_TO_ALL_RESTAURANTS)
        assert self.page.is_url_matches(paths.MAIN)
        assert self.page.is_visible(self.page.locators.RESTAURANTS_HEADER)
