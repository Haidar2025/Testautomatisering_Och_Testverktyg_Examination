"""Steps: Navigation"""
from behave import given, when, then


@given("jag öppnar Läslistan")
def step_open_site(context):
    context.base.goto()


@when('jag klickar på navknappen "{testid}"')
def step_click_nav_button(context, testid):
    context.base.nav_button(testid).click()
    context.page.wait_for_timeout(300)


@then('är navknappen "{testid}" inaktiverad')
def step_nav_button_disabled(context, testid):
    assert context.base.is_nav_button_disabled(testid), \
        f"Förväntade att navknappen '{testid}' är inaktiverad"


@then("ser jag böcker i katalogen")
def step_see_books(context):
    count = context.catalog.book_count()
    assert count > 0, "Förväntade att se böcker i katalogen"
