"""
Backend: BookStore

Hanterar en lista med böcker. Varje bok har ett unikt id,
en titel, en författare och ett fav-fält (bool).

Metoder:
  add_book(author, title)       → lägger till en ny bok
  toggle_favorite(book_id)      → växlar fav-status för en bok
"""


class BookStore:
    def __init__(self, initial_books=None):
        self._books = []
        self._next_id = 1

        if initial_books:
            for book in initial_books:
                entry = {
                    "id": book["id"],
                    "title": book["title"],
                    "author": book["author"],
                    "fav": False,
                }
                self._books.append(entry)
                # Se till att nästa ID är unikt
                if book["id"] >= self._next_id:
                    self._next_id = book["id"] + 1

    # ------------------------------------------------------------------
    # Publik API
    # ------------------------------------------------------------------

    def add_book(self, author, title):
        """Lägger till en ny bok och returnerar den."""
        new_book = {
            "id": self._next_id,
            "author": author,
            "title": title,
            "fav": False,
        }
        self._books.append(new_book)
        self._next_id += 1
        return new_book

    def toggle_favorite(self, book_id):
        """
        Växlar fav-statusen för boken med givet id.
        Kastar ValueError om boken inte hittas.
        """
        for book in self._books:
            if book["id"] == book_id:
                book["fav"] = not book["fav"]
                return book
        raise ValueError(f"Ingen bok med id {book_id} hittades")

    # ------------------------------------------------------------------
    # Hjälpmetoder
    # ------------------------------------------------------------------

    @property
    def books(self):
        """Returnerar en kopia av boklistan."""
        return list(self._books)

    def get_favorites(self):
        """Returnerar alla böcker markerade som favoriter."""
        return [b for b in self._books if b["fav"]]

    def __len__(self):
        return len(self._books)
