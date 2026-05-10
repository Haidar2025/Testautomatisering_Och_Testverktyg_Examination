"""Page Object: StatisticsPage"""
from .base_page import BasePage


class StatisticsPage(BasePage):
    def book_count_text(self):
        return self.page.get_by_test_id("book-count").inner_text().strip()

    def stars_count_text(self):
        return self.page.get_by_test_id("stars-count").inner_text().strip()

    def total_books(self):
        text = self.book_count_text()
        for word in text.split():
            if word.isdigit():
                return int(word)
        return 0

    def favorited_books(self):
        text = self.stars_count_text()
        for word in text.split():
            if word.isdigit():
                return int(word)
        return 0
