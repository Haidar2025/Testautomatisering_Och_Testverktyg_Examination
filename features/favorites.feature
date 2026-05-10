Feature: Mina böcker
  Som en användare vill jag se mina hjärtmarkerade böcker
  på en samlad sida så att jag lätt hittar dem.

  Scenario: Tomt meddelande visas när inga favoriter finns
    Given jag är på sidan Mina böcker
    Then ser jag meddelandet om inga favoriter

  Scenario: Hjärtmarkerad bok visas under Mina böcker
    Given jag är på katalogsidan
    When jag klickar på hjärtat för "Git Blame and Other Ways to Lose Friends"
    And jag navigerar till Mina böcker
    Then syns "Git Blame and Other Ways to Lose Friends" i min lista

  Scenario: Ta bort favorit tar även bort den från Mina böcker
    Given jag är på katalogsidan
    When jag klickar på hjärtat för "My First Regex (And Last)"
    And jag navigerar till Mina böcker
    Then syns "My First Regex (And Last)" i min lista
    When jag navigerar till katalogen
    And jag klickar på hjärtat för "My First Regex (And Last)"
    And jag navigerar till Mina böcker
    Then syns inte "My First Regex (And Last)" i min lista
