# Created by Inga at 17.09.2022
Feature: Page number navigation is available and works as expected
  # Enter feature description here

  Scenario: User can click through multiple product pages by clicking 1, 2 for page number
    Given Open product catalog page
    And First product catalog page is open
    When Click on page 2 of product catalog
    Then Second catalog page is open


  Scenario: User can click through multiple product pages by clicking >
    Given Open product catalog page
    And First product catalog page is open
    When Click on > in page list
    Then Second catalog page is open


  Scenario: User can click through multiple product pages by clicking <
    Given Open product catalog page 2
    When Click on < in page list
    Then First product catalog page is open