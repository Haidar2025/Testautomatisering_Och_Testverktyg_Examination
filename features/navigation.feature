Feature: Navigation
  Som en användare vill jag kunna navigera mellan sidans vyer
  så att jag kan använda alla delar av Läslistan.

  Scenario: Statistik-knappen är inaktiverad på statistiksidan
    Given jag öppnar Läslistan
    When jag klickar på navknappen "statistics"
    Then är navknappen "statistics" inaktiverad

  Scenario Outline: Navigera till en vy via navknappen
    Given jag öppnar Läslistan
    When jag klickar på navknappen "statistics"
    When jag klickar på navknappen "<testid>"
    Then är navknappen "<testid>" inaktiverad

    Examples:
      | testid     |
      | catalog    |
      | add-book   |
      | favorites  |
