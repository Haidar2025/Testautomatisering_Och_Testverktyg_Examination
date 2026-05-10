"""
Page Object: BasePage

Grundklass med gemensamma metoder som alla sidor delar.
"""

BASE_URL = "https://tap-ht25-testverktyg.github.io/exam/"


class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(BASE_URL, timeout=10000)
        self.page.wait_for_timeout(1500)

    def go_to_catalog(self):
        # Katalog är standardvyn – klicka bara om knappen inte redan är disabled
        btn = self.page.get_by_test_id("catalog")
        if not btn.is_disabled():
            btn.click()
            self.page.wait_for_timeout(400)

    def go_to_add_book(self):
        self.page.get_by_test_id("add-book").click()
        self.page.wait_for_timeout(400)

    def go_to_favorites(self):
        self.page.get_by_test_id("favorites").click()
        self.page.wait_for_timeout(400)

    def go_to_statistics(self):
        self.page.get_by_test_id("statistics").click()
        self.page.wait_for_timeout(400)

    def nav_button(self, testid):
        return self.page.get_by_test_id(testid)

    def is_nav_button_disabled(self, testid):
        return self.nav_button(testid).is_disabled()
