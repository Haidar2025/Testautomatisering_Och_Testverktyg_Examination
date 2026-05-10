# Teorifrågor – Testautomatisering och testverktyg

## 1. Skillnad mellan enhetstest, integrationstest, regressionstest och prestandatest

| Testtyp | Vad testas | Exempel |
|---|---|---|
| **Enhetstest** | En enstaka funktion eller klass i isolation | `test_add_book_returns_dict()` |
| **Integrationstest** | Samspelet mellan två eller fler moduler | `BookStore` + `FavoriteBooks` i kombination |
| **Regressionstest** | Att tidigare fungerade funktioner fortfarande fungerar efter en ändring | Kör hela testsviten efter en buggfix |
| **Prestandatest** | Hur snabbt och stabilt systemet beter sig under belastning | Mäta svarstid vid 1 000 samtidiga användare |

**Enhetstest** är snabba och isolerade – de mockar bort beroenden. De hittar buggar tidigt och exakt.

**Integrationstest** testar att komponenter fungerar *ihop*, t.ex. att databasen och affärslogiken pratar rätt med varandra.

**Regressionstest** är inte en separat testtyp utan en *strategi* – man kör befintliga tester efter ändringar för att säkerställa att inget gick sönder.

**Prestandatest** mäter icke-funktionella krav: svarstider, genomströmning och stabilitet. Verktyg: Locust, JMeter.

---

## 2. Hur TDD (Test-Driven Development) fungerar

TDD följer en kort, upprepad cykel kallad **Red–Green–Refactor**:

1. **Red** – Skriv ett test som *misslyckas* (det finns ingen kod än).
2. **Green** – Skriv den *minimala* mängd kod som får testet att gå igenom.
3. **Refactor** – Städa upp koden utan att bryta testet.

Sedan börjar cykeln om med nästa krav.

**Fördelar:**
- Designen styrs av testbara enheter → bättre kodstruktur.
- 100 % testtäckning från start.
- Buggar hittas direkt, inte veckor senare.
- Testerna fungerar som levande dokumentation.

I detta projekt skrevs `test_book_store.py` och `test_favorite_books.py` **innan** `book_store.py` och `favorite_books.py` implementerades.

---

## 3. Hur BDD skiljer sig från TDD

| Aspekt | TDD | BDD |
|---|---|---|
| **Fokus** | Implementation (hur koden fungerar) | Beteende (vad systemet ska göra för användaren) |
| **Språk** | Python / kod | Gherkin (Given–When–Then på naturligt språk) |
| **Målgrupp** | Utvecklare | Utvecklare *och* icke-tekniska intressenter |
| **Verktyg** | pytest, unittest | behave, Cucumber, SpecFlow |
| **Vad testas** | Enstaka funktioner | Hela användarflöden (E2E) |

BDD är ett *samarbetsdriven* testmetod. Feature-filer som `katalog.feature` skrivs så att produktägare, testare och utvecklare kan läsa och förstå dem. Stegen binds sedan till Python-kod med dekoratorer.

BDD bygger på TDD-principerna men lyfter blicken till *affärsvärde* och *användarbeteende*.

---

## 4. Vilka tester passar för en Läslistan-webbsida

För Läslistan-applikationen (`https://tap-ht25-testverktyg.github.io/exam/`) rekommenderas följande testtyper:

### Enhetstester (pytest)
Passar för affärslogik utan UI:
- `BookStore.add_book()` – returnerar korrekt bokobjekt
- `BookStore.toggle_favorite()` – kastar `ValueError` för okänt ID
- `FavoriteBooks.add()` – ignorerar dubletter
- `FavoriteBooks.remove()` – tyst om boken saknas

### Integrationstester (pytest)
Passar för samspelet mellan `BookStore` och `FavoriteBooks`:
- Att markera en bok i store synkroniserar med favorites-listan
- Att avmarkera tar bort boken från favorites

### BDD/E2E-tester (behave + Playwright)
Passar för att verifiera hela användarflöden i webbläsaren:
- Navigering mellan vyer via navknappar
- Lägga till en bok via formuläret och se den i katalogen
- Hjärtmarkera en bok och se den i "Mina böcker"
- Statistiksidan uppdateras när favoriter ändras

### Motivering
Enhetstester ger snabb feedback och täcker kantfall. BDD-tester ger förtroende att *hela flödet* fungerar ur ett användarperspektiv. Integrationstester säkerställer att datalagren pratar rätt med varandra. Prestandatest är *inte* prioriterat här eftersom det är en statisk frontend-app utan serverlast.
