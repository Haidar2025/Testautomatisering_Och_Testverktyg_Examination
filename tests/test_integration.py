"""
Integrationstester: BookStore + FavoriteBooks

Testar att de två klasserna fungerar tillsammans
på det sätt sidan förväntar sig.
"""
import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from backend.book_store import BookStore
from backend.favorite_books import FavoriteBooks


@pytest.fixture
def store():
    return BookStore([
        {"id": 1, "title": "Bok A", "author": "Forfattare A"},
        {"id": 2, "title": "Bok B", "author": "Forfattare B"},
        {"id": 3, "title": "Bok C", "author": "Forfattare C"},
    ])


@pytest.fixture
def favs():
    return FavoriteBooks()


# ------------------------------------------------------------------

def test_toggle_and_add_to_favorites(store, favs):
    """
    Hela flödet: toggle på en bok → lägg till i FavoriteBooks.
    """
    book = store.toggle_favorite(1)
    assert book["fav"] is True
    favs.add(book)
    assert len(favs) == 1


def test_toggle_off_and_remove_from_favorites(store, favs):
    """
    Toggle on → lägg till favorit → toggle off → ta bort favorit.
    """
    book = store.toggle_favorite(2)
    favs.add(book)
    assert len(favs) == 1

    store.toggle_favorite(2)
    favs.remove(book)
    assert len(favs) == 0


def test_favorites_reflect_store_state(store, favs):
    """
    Favoritlistan ska stämma överens med böcker som har fav=True i store.
    """
    store.toggle_favorite(1)
    store.toggle_favorite(3)

    for book in store.get_favorites():
        favs.add(book)

    assert len(favs) == 2
    fav_ids = {b["id"] for b in favs.books}
    assert fav_ids == {1, 3}


def test_add_new_book_and_favorite_it(store, favs):
    """
    Lägg till en ny bok via store → markera som favorit → syns i favs.
    """
    new_book = store.add_book("Ny Forfattare", "Ny Bok")
    assert new_book["fav"] is False

    toggled = store.toggle_favorite(new_book["id"])
    favs.add(toggled)

    assert len(favs) == 1
    assert favs.books[0]["title"] == "Ny Bok"


def test_unfavorite_does_not_appear_in_favorites(store, favs):
    """
    Böcker utan fav=True ska inte hamna i FavoriteBooks.
    """
    for book in store.books:
        if book["fav"]:
            favs.add(book)
    assert len(favs) == 0


def test_multiple_toggles_sync_with_favorites(store, favs):
    """
    Tre toggle (= True) → boken är favorit.
    Fyra toggle (= False) → boken ska tas bort från favs.
    """
    book_id = 1
    for _ in range(3):
        book = store.toggle_favorite(book_id)

    favs.add(book)
    assert len(favs) == 1

    book = store.toggle_favorite(book_id)  # 4e toggle → fav=False
    favs.remove(book)
    assert len(favs) == 0
