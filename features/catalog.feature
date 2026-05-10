Feature: Katalog
  Som en användare vill jag kunna bläddra i katalogen
  och markera böcker som favoriter.

  Scenario: Katalogen innehåller böcker
    Given jag öppnar Läslistan
    Then ser jag minst 13 böcker i katalogen

  Scenario: Hjärtmarkera en bok
    Given jag är på katalogsidan
    When jag klickar på hjärtat för "Agile Is a Feeling"
    Then är hjärtat markerat för "Agile Is a Feeling"

  Scenario: Ta bort hjärtmarkering
    Given jag är på katalogsidan
    When jag klickar på hjärtat för "Stack Overflow: A Love Story" två gånger
    Then är hjärtat inte markerat för "Stack Overflow: A Love Story"

  Scenario Outline: Hjärtmarkering vid flera klick
    Given jag är på katalogsidan
    When jag klickar på hjärtat för "<titel>" <antal> gånger
    Then är hjärtat markerat med status "<status>" för "<titel>"

    Examples:
      | titel                          | antal | status      |
      | Learn Python in 21 Years       | 1     | selected    |
      | Learn Python in 21 Years       | 2     | unselected  |
      | Learn Python in 21 Years       | 3     | selected    |
