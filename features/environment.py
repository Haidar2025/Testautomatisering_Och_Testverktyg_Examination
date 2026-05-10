"""
Behave environment: sätter upp Playwright inför varje scenario
och stänger ner efter.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from playwright.sync_api import sync_playwright


def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)


def after_all(context):
    context.browser.close()
    context.playwright.stop()


def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    # Importera page objects
    from pages.base_page import BasePage
    from pages.catalog_page import CatalogPage
    from pages.add_book_page import AddBookPage
    from pages.favorites_page import FavoritesPage
    from pages.statistics_page import StatisticsPage

    context.base = BasePage(context.page)
    context.catalog = CatalogPage(context.page)
    context.add_book = AddBookPage(context.page)
    context.favorites = FavoritesPage(context.page)
    context.statistics = StatisticsPage(context.page)


def after_scenario(context, scenario):
    context.page.close()
