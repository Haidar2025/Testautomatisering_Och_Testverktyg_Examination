"""Steps: Statistik"""
from behave import given, when, then


@given("jag är på statistiksidan")
def step_go_to_stats(context):
    context.base.goto()
    context.base.go_to_statistics()


@when("jag navigerar till statistiksidan")
def step_navigate_to_stats(context):
    context.base.go_to_statistics()


@then("visar statistiken {antal:d} böcker totalt")
def step_stats_book_count(context, antal):
    total = context.statistics.total_books()
    assert total == antal, \
        f"Förväntade {antal} böcker totalt, fick {total}"


@then("visar statistiken {antal:d} hjärtmarkerade böcker")
def step_stats_favorites_count(context, antal):
    favs = context.statistics.favorited_books()
    assert favs == antal, \
        f"Förväntade {antal} hjärtmarkerade, fick {favs}"
