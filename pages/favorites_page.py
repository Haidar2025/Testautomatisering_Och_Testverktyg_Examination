"""Page Object: FavoritesPage"""
from .base_page import BasePage


class FavoritesPage(BasePage):
    def is_empty_message_visible(self):
        return self.page.get_by_text("När du valt, kommer dina favoritböcker att visas här.").is_visible()

    def favorite_titles(self):
        items = self.page.locator("[data-testid^='fav-']")
        return [items.nth(i).inner_text().strip() for i in range(items.count())]

    def favorite_count(self):
        return self.page.locator("[data-testid^='fav-']").count()

    def is_book_in_favorites(self, title):
        return self.page.get_by_test_id(f"fav-{title}").is_visible()
