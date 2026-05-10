"""
Enhetstester för FavoriteBooks (TDD)
"""
import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from backend.favorite_books import FavoriteBooks


@pytest.fixture
def favs():
    return FavoriteBooks()


@pytest.fixture
def sample_book():
    return {"id": 1, "title": "Bok A", "author": "Forfattare A", "fav": True}


@pytest.fixture
def another_book():
    return {"id": 2, "title": "Bok B", "author": "Forfattare B", "fav": True}


# ------------------------------------------------------------------
# Tester för add
# ------------------------------------------------------------------

def test_add_increases_length(favs, sample_book):
    """add ska öka antalet favoriter med ett."""
    assert len(favs) == 0
    favs.add(sample_book)
    assert len(favs) == 1


def test_add_book_is_in_list(favs, sample_book):
    """Boken ska finnas i listan efter add."""
    favs.add(sample_book)
    assert sample_book in favs


def test_add_duplicate_is_ignored(favs, sample_book):
    """Att lägga till samma bok två gånger ska inte ge duplicat."""
    favs.add(sample_book)
    favs.add(sample_book)
    assert len(favs) == 1


def test_add_multiple_books(favs, sample_book, another_book):
    """Flera olika böcker ska kunna läggas till."""
    favs.add(sample_book)
    favs.add(another_book)
    assert len(favs) == 2
    assert sample_book in favs
    assert another_book in favs


# ------------------------------------------------------------------
# Tester för remove
# ------------------------------------------------------------------

def test_remove_decreases_length(favs, sample_book):
    """remove ska minska antalet favoriter med ett."""
    favs.add(sample_book)
    favs.remove(sample_book)
    assert len(favs) == 0


def test_remove_book_not_in_list(favs, sample_book):
    """Ta bort en bok som inte finns ska inte kasta fel."""
    favs.remove(sample_book)  # ska inte krascha
    assert len(favs) == 0


def test_remove_only_removes_target(favs, sample_book, another_book):
    """remove ska bara ta bort den angivna boken."""
    favs.add(sample_book)
    favs.add(another_book)
    favs.remove(sample_book)
    assert sample_book not in favs
    assert another_book in favs


def test_books_property_returns_copy(favs, sample_book):
    """books-property ska returnera en kopia."""
    favs.add(sample_book)
    copy = favs.books
    copy.clear()
    assert len(favs) == 1
