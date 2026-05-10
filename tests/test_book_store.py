"""
Enhetstester för BookStore (TDD)

Varje metod testas isolerat.
"""
import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from backend.book_store import BookStore


# ------------------------------------------------------------------
# Fixtures
# ------------------------------------------------------------------

@pytest.fixture
def empty_store():
    return BookStore()


@pytest.fixture
def store_with_books():
    return BookStore([
        {"id": 1, "title": "Bok A", "author": "Forfattare A"},
        {"id": 2, "title": "Bok B", "author": "Forfattare B"},
    ])


# ------------------------------------------------------------------
# Tester för add_book
# ------------------------------------------------------------------

def test_add_book_returns_book(empty_store):
    """add_book ska returnera den nyss skapade boken."""
    book = empty_store.add_book("Forfattare X", "Titel X")
    assert book["title"] == "Titel X"
    assert book["author"] == "Forfattare X"


def test_add_book_has_unique_id(empty_store):
    """Varje bok ska få ett unikt id."""
    book1 = empty_store.add_book("A", "Bok 1")
    book2 = empty_store.add_book("B", "Bok 2")
    assert book1["id"] != book2["id"]


def test_add_book_starts_with_fav_false(empty_store):
    """En ny bok ska inte vara favorit från start."""
    book = empty_store.add_book("C", "Bok C")
    assert book["fav"] is False


def test_add_book_increases_length(empty_store):
    """Antal böcker ska öka med ett per tillägg."""
    assert len(empty_store) == 0
    empty_store.add_book("D", "Bok D")
    assert len(empty_store) == 1
    empty_store.add_book("E", "Bok E")
    assert len(empty_store) == 2


def test_add_multiple_books_keeps_all(empty_store):
    """Alla tillagda böcker ska finnas kvar i listan."""
    empty_store.add_book("F", "Bok F")
    empty_store.add_book("G", "Bok G")
    titles = [b["title"] for b in empty_store.books]
    assert "Bok F" in titles
    assert "Bok G" in titles


# ------------------------------------------------------------------
# Tester för toggle_favorite
# ------------------------------------------------------------------

def test_toggle_favorite_sets_fav_true(store_with_books):
    """Första toggle ska markera boken som favorit."""
    store_with_books.toggle_favorite(1)
    book = next(b for b in store_with_books.books if b["id"] == 1)
    assert book["fav"] is True


def test_toggle_favorite_twice_resets(store_with_books):
    """Två toggle på samma bok ska återställa fav till False."""
    store_with_books.toggle_favorite(1)
    store_with_books.toggle_favorite(1)
    book = next(b for b in store_with_books.books if b["id"] == 1)
    assert book["fav"] is False


def test_toggle_favorite_three_times_is_true(store_with_books):
    """Tre toggle ger fav=True (udda antal = True)."""
    store_with_books.toggle_favorite(1)
    store_with_books.toggle_favorite(1)
    store_with_books.toggle_favorite(1)
    book = next(b for b in store_with_books.books if b["id"] == 1)
    assert book["fav"] is True


def test_toggle_favorite_only_affects_target_book(store_with_books):
    """Toggle på bok 1 ska inte påverka bok 2."""
    store_with_books.toggle_favorite(1)
    book2 = next(b for b in store_with_books.books if b["id"] == 2)
    assert book2["fav"] is False


def test_toggle_favorite_unknown_id_raises(store_with_books):
    """Toggle med ett okänt id ska kasta ValueError."""
    with pytest.raises(ValueError):
        store_with_books.toggle_favorite(9999)


# ------------------------------------------------------------------
# Tester för get_favorites
# ------------------------------------------------------------------

def test_get_favorites_empty_initially(store_with_books):
    """Inga favoriter från start."""
    assert store_with_books.get_favorites() == []


def test_get_favorites_returns_marked_books(store_with_books):
    """get_favorites ska returnera böcker med fav=True."""
    store_with_books.toggle_favorite(2)
    favs = store_with_books.get_favorites()
    assert len(favs) == 1
    assert favs[0]["id"] == 2


def test_books_property_returns_copy(store_with_books):
    """books-property ska returnera en kopia, inte en referens."""
    copy = store_with_books.books
    copy.append({"id": 99, "title": "Fake", "author": "Fake", "fav": False})
    assert len(store_with_books) == 2
