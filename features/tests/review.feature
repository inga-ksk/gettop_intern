# Created by Inga at 19.09.2022
Feature: Review submission is working and reviews are saved

  Scenario: User can submit a review
    Given Open product page
    When Click on Review Tab
    And Choose rating
    And Review text is typed in
    And Fields Name and Email are filled out
    And Submit button is clicked
    Then Review is saved and added to reviews list