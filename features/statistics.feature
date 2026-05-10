Feature: Statistik
  Som en användare vill jag se statistik om katalogen
  för att få en snabb överblick.

  Scenario: Statistiken visar totalt antal böcker
    Given jag är på statistiksidan
    Then visar statistiken 13 böcker totalt

  Scenario: Statistiken visar noll favoriter från start
    Given jag är på statistiksidan
    Then visar statistiken 0 hjärtmarkerade böcker

  Scenario: Statistiken uppdateras när en bok markeras
    Given jag är på katalogsidan
    When jag klickar på hjärtat för "The Bugs are Coming"
    And jag navigerar till statistiksidan
    Then visar statistiken 1 hjärtmarkerade böcker

  Scenario: Statistiken minskar när favorit tas bort
    Given jag är på katalogsidan
    When jag klickar på hjärtat för "The Bugs are Coming"
    And jag klickar på hjärtat för "The Bugs are Coming"
    And jag navigerar till statistiksidan
    Then visar statistiken 0 hjärtmarkerade böcker
