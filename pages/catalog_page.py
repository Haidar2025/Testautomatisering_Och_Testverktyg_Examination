"""Page Object: CatalogPage"""
from .base_page import BasePage


class CatalogPage(BasePage):
    def book_count(self):
        return self.page.locator(".book").count()

    def click_heart(self, title):
        self.page.get_by_test_id(f"star-{title}").click()
        self.page.wait_for_timeout(200)

    def is_heart_selected(self, title):
        star = self.page.get_by_test_id(f"star-{title}")
        return "selected" in (star.get_attribute("class") or "")

    def book_titles(self):
        return [b.inner_text() for b in self.page.locator(".book").all()]
