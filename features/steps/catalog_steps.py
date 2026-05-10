"""Steps: Katalog"""
from behave import given, when, then


@given("jag är på katalogsidan")
def step_go_to_catalog(context):
    context.base.goto()
    context.base.go_to_catalog()


@then("ser jag minst 13 böcker i katalogen")
def step_see_at_least_13_books(context):
    count = context.catalog.book_count()
    assert count >= 13, f"Förväntade minst 13 böcker, hittade {count}"


@when('jag klickar på hjärtat för "{titel}"')
def step_click_heart(context, titel):
    context.catalog.click_heart(titel)


@when('jag klickar på hjärtat för "{titel}" två gånger')
def step_click_heart_twice(context, titel):
    context.catalog.click_heart(titel)
    context.catalog.click_heart(titel)


@when('jag klickar på hjärtat för "{titel}" {antal:d} gånger')
def step_click_heart_n_times(context, titel, antal):
    for _ in range(antal):
        context.catalog.click_heart(titel)


@then('är hjärtat markerat för "{titel}"')
def step_heart_is_selected(context, titel):
    assert context.catalog.is_heart_selected(titel), \
        f"Förväntade att hjärtat är markerat för '{titel}'"


@then('är hjärtat inte markerat för "{titel}"')
def step_heart_is_not_selected(context, titel):
    assert not context.catalog.is_heart_selected(titel), \
        f"Förväntade att hjärtat INTE är markerat för '{titel}'"


@then('är hjärtat markerat med status "{status}" för "{titel}"')
def step_heart_status(context, status, titel):
    selected = context.catalog.is_heart_selected(titel)
    if status == "selected":
        assert selected, f"Förväntade selected för '{titel}'"
    else:
        assert not selected, f"Förväntade unselected för '{titel}'"
