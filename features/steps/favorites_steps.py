"""Steps: Mina böcker"""
from behave import given, when, then


@given("jag är på sidan Mina böcker")
def step_go_to_favorites(context):
    context.base.goto()
    context.base.go_to_favorites()


@when("jag navigerar till Mina böcker")
def step_navigate_to_favorites(context):
    context.base.go_to_favorites()


@when("jag navigerar till katalogen")
def step_navigate_to_catalog(context):
    context.base.go_to_catalog()


@then("ser jag meddelandet om inga favoriter")
def step_see_empty_message(context):
    assert context.favorites.is_empty_message_visible(), \
        "Förväntade att se meddelandet om inga favoriter"


@then('syns "{titel}" i min lista')
def step_book_in_favorites(context, titel):
    assert context.favorites.is_book_in_favorites(titel), \
        f"Förväntade att '{titel}' syns i Mina böcker"


@then('syns inte "{titel}" i min lista')
def step_book_not_in_favorites(context, titel):
    assert not context.favorites.is_book_in_favorites(titel), \
        f"Förväntade att '{titel}' INTE syns i Mina böcker"
