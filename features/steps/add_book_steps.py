"""Steps: Lägg till bok"""
from behave import given, when, then


@given("jag är på sidan för att lägga till bok")
def step_go_to_add_book(context):
    context.base.goto()
    context.base.go_to_add_book()


@when('jag fyller i titeln "{titel}" och författaren "{forfatter}"')
def step_fill_form(context, titel, forfatter):
    context.add_book.fill_title(titel)
    context.add_book.fill_author(forfatter)


@when("jag klickar på skicka")
def step_click_submit(context):
    context.add_book.submit()


@when("jag navigerar till katalogen efter tillägg")
def step_go_to_catalog_after_add(context):
    context.base.go_to_catalog()


@then("är skicka-knappen inaktiverad")
def step_submit_disabled(context):
    assert context.add_book.is_submit_disabled(), \
        "Förväntade att skicka-knappen är inaktiverad"


@then("är skicka-knappen aktiv")
def step_submit_enabled(context):
    assert not context.add_book.is_submit_disabled(), \
        "Förväntade att skicka-knappen är aktiv"


@then('katalogen innehåller boken "{titel}"')
def step_catalog_contains_book(context, titel):
    titles_text = " ".join(context.catalog.book_titles())
    assert titel in titles_text, \
        f"Förväntade att katalogen innehåller '{titel}'"
