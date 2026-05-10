Feature: Lägg till bok
  Som en användare vill jag kunna lägga till en ny bok
  så att katalogen växer med böcker jag väljer.

  Scenario: Skicka-knappen är inaktiv när fälten är tomma
    Given jag är på sidan för att lägga till bok
    Then är skicka-knappen inaktiverad

  Scenario: Skicka-knappen aktiveras när båda fälten är ifyllda
    Given jag är på sidan för att lägga till bok
    When jag fyller i titeln "Min favoritbok" och författaren "Min favoritförfattare"
    Then är skicka-knappen aktiv

  Scenario: Lägga till en ny bok dyker upp i katalogen
    Given jag är på sidan för att lägga till bok
    When jag fyller i titeln "En bok om testning" och författaren "Haidar"
    And jag klickar på skicka
    And jag navigerar till katalogen efter tillägg
    Then katalogen innehåller boken "En bok om testning"
