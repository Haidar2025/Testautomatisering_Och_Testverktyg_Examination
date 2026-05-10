# Läslistan – Examensuppgift

Testprojekt för kursen **Testautomatisering och testverktyg 25 YHP**.

Applikationen som testas: **https://tap-ht25-testverktyg.github.io/exam/**

---

## Vad har testats

### Backend – TDD med pytest (27 tester)

Affärslogiken implementerades med Test-Driven Development.

| Modul                       | Tester | Beskrivning                                          |
|-----------------------------|--------|------------------------------------------------------|
| `backend/book_store.py`     | 13     | `add_book()`, `toggle_favorite()`, `get_favorites()` |
| `backend/favorite_books.py` | 8      | `add()`, `remove()`, dublettkontroll |
| `tests/test_integration.py` | 6      | BookStore + FavoriteBooks i kombination |

Kör enhetstesterna:
```bash
pytest tests/ -v
```

### Frontend – BDD med behave + Playwright (20 scenarion)

Hela användarflödet testas med Gherkin-scenarion och Playwright.

| Feature       | Scenarion | Vad som testas                               |
|---------------|-----------|----------------------------------------------|
| Navigation    | 4         | Navknappar, aktiv vy inaktiverad             |
| Katalog       | 4         | Bokvisning, hjärtmarkering, Scenario Outline |
| Lägg till bok | 3         | Formulärvalidering, ny bok i katalog         |
| Mina böcker   | 3         | Favoritlesta, lägg till/ta bort              |
| Statistik     | 4         | Räknare uppdateras dynamiskt                 |

Kör BDD-testerna:
```bash
behave
```

---

## Tekniker och mönster

- **Page Object Pattern** – varje sida har en dedikerad klass (`pages/`)
- **Scenario Outline** – parametriserad navigeringstest
- **TDD (Red–Green–Refactor)** – backend skrevs test-first
- **BDD (Given–When–Then)** – feature-filer på svenska

---

## Hur man startar projektet

### Krav

- Python 3.10+
- Node.js (för att köra React-appen lokalt, valfritt)

### 1. Klona repot

```bash
git clone https://github.com/Haidar2025/Testautomatisering_Och_Testverktyg_Examination.git
cd Testautomatisering_Och_Testverktyg_Examination
```

### 2. Skapa virtuell miljö och installera beroenden

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
playwright install chromium
```

### 3. Kör backend-tester (pytest)

```bash
pytest tests/ -v
```

Förväntat resultat: **27 passed**

### 4. Kör BDD-tester (behave)

```bash
behave
```

Förväntat resultat: **20 scenarios passed**

---

## Projektstruktur

```
examination_project/
├── backend/
│   ├── book_store.py        # Bokhantering (TDD)
│   └── favorite_books.py    # Favorithantering (TDD)
├── tests/
│   ├── test_book_store.py   # 13 enhetstester
│   ├── test_favorite_books.py # 8 enhetstester
│   └── test_integration.py  # 6 integrationstester
├── pages/
│   ├── base_page.py         # Navigation (Page Object)
│   ├── catalog_page.py      # Katalog (Page Object)
│   ├── add_book_page.py     # Lägg till bok (Page Object)
│   ├── favorites_page.py    # Mina böcker (Page Object)
│   └── statistics_page.py   # Statistik (Page Object)
├── features/
│   ├── navigation.feature
│   ├── catalog.feature
│   ├── add_book.feature
│   ├── favorites.feature
│   ├── statistics.feature
│   ├── environment.py
│   └── steps/
│       ├── navigation_steps.py
│       ├── catalog_steps.py
│       ├── add_book_steps.py
│       ├── favorites_steps.py
│       └── statistics_steps.py
├── ANSWERS.md               # Teorisvar
├── STORIES.md               # Användarberättelser
├── requirements.txt
├── behave.ini
└── pytest.ini
```
