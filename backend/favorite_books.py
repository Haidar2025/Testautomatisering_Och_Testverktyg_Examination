"""
Backend: FavoriteBooks

Håller reda på vilka böcker användaren har markerat som favoriter.

Metoder:
  add(book)     → lägger till en bok i favoritlistan
  remove(book)  → tar bort en bok från favoritlistan
"""


class FavoriteBooks:
    def __init__(self):
        self._favorites = []

    def add(self, book):
        """
        Lägger till boken om den inte redan finns i listan.
        Dubbla tillägg ignoreras.
        """
        if book not in self._favorites:
            self._favorites.append(book)

    def remove(self, book):
        """
        Tar bort boken om den finns.
        Tar bort en bok som inte finns i listan gör ingenting.
        """
        if book in self._favorites:
            self._favorites.remove(book)

    @property
    def books(self):
        """Returnerar en kopia av favoritlistan."""
        return list(self._favorites)

    def __len__(self):
        return len(self._favorites)

    def __contains__(self, book):
        return book in self._favorites
