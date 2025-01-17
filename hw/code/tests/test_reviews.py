import pytest
from ui.paths import paths
from ui.components.reviews_page import ReviewsElement
from ui.base_case.base_case import BaseCase


class TestMenuPage(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = ReviewsElement(driver, url_config)

    REVIEW_TEXT, REVIEW_STARS = "Очень хорошо!", 5

    def test_check_reviews(self):
        self.page.open_path(paths.GUAVA_DISHES)
        assert self.page.is_visible(self.page.locators.REVIEW_INFO_BLOCK)
        self.page.go_to_review()
        assert self.page.is_url_matches(paths.GUAVA_REVIEWS_PAGE)
        assert self.page.is_visible(self.page.locators.REVIEWS)

    @pytest.mark.skip(
        reason="стабильно не проходит, так как webdriver не видит необходимый элемент. описание проблемы пункт 2 https://github.com/VK-BMSTU-QA/homework-selenium/pull/7#issue-1468677953"
    )
    def test_send_review(self, authorize, order_go_to_review):
        self.page.input_review(self.REVIEW_TEXT, self.REVIEW_STARS)
        self.page.send_review()
        assert self.page.is_url_matches(paths.GUAVA_REVIEWS_PAGE)
        assert self.page.get_first_review_text() == self.REVIEW_TEXT
        assert self.page.get_first_review_stars() == str(self.REVIEW_STARS)
