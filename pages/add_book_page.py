"""Page Object: AddBookPage"""
from .base_page import BasePage


class AddBookPage(BasePage):
    def fill_title(self, title):
        self.page.get_by_test_id("add-input-title").fill(title)

    def fill_author(self, author):
        self.page.get_by_test_id("add-input-author").fill(author)

    def submit(self):
        self.page.get_by_test_id("add-submit").click()
        self.page.wait_for_timeout(400)

    def is_submit_disabled(self):
        return self.page.get_by_test_id("add-submit").is_disabled()
