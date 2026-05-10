# Användarberättelser – Läslistan

Dessa användarberättelser (user stories) beskriver de funktioner som testats i examensuppgiften.
Format: *Som en [roll] vill jag [mål] så att [nytta].*

---

## Navigation

**US-1: Navigera mellan vyer**
> Som en användare vill jag kunna klicka på navknappar (Katalog, Lägg till, Mina böcker, Statistik)
> så att jag snabbt kan byta mellan applikationens olika vyer.

*Acceptanskriterier:*
- När jag klickar på en navknapp laddas rätt vy.
- Navknappen för den aktiva vyn är inaktiverad (kan ej klickas).

---

## Katalog

**US-2: Visa katalog**
> Som en användare vill jag se alla tillgängliga böcker i katalogen
> så att jag kan få en översikt och välja vad jag vill läsa.

*Acceptanskriterier:*
- Katalogen visar minst 13 böcker vid sidstart.
- Varje bok visas med titel och hjärtknapp.

**US-3: Hjärtmarkera en bok**
> Som en användare vill jag kunna klicka på hjärtat bredvid en bok
> så att jag markerar den som favorit.

*Acceptanskriterier:*
- Första klicket → hjärtat markeras ("selected").
- Andra klicket → hjärtat avmarkeras ("unselected").
- Tredje klicket → hjärtat markeras igen.

---

## Lägg till bok

**US-4: Lägga till en ny bok**
> Som en användare vill jag kunna fylla i titel och författare och trycka Skicka
> så att katalogen växer med böcker jag väljer.

*Acceptanskriterier:*
- Skicka-knappen är inaktiverad om titel eller författare saknas.
- Skicka-knappen aktiveras när båda fälten är ifyllda.
- Den tillagda boken syns i katalogen efter att formuläret skickats.

---

## Mina böcker

**US-5: Se mina favoriter**
> Som en användare vill jag se en samlad lista med mina hjärtmarkerade böcker
> så att jag lätt hittar dem igen.

*Acceptanskriterier:*
- Om inga böcker är markerade visas ett informationsmeddelande.
- Hjärtmarkerade böcker syns i listan.
- Avmarkerade böcker försvinner från listan.

---

## Statistik

**US-6: Se statistik om katalogen**
> Som en användare vill jag se antalet böcker och antalet favoriter i en statistikvy
> så att jag får en snabb överblick.

*Acceptanskriterier:*
- Statistiken visar totalt antal böcker (initialt 13).
- Statistiken visar antal hjärtmarkerade böcker (initialt 0).
- Antalen uppdateras dynamiskt när böcker markeras eller avmarkeras.
