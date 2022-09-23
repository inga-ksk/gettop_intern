# Created by Inga at 22.09.2022
Feature: Sorting by Average Rating is showing correct items with available ratings

  Scenario: User can sort products by average rating
    Given Open product catalog page
    When Click on sorting dropdown list
    And Select Sort by average rating
    Then 1st product has rating starts displayed after sorting

  Scenario: User can click through product pages after sorting is done (1, 2, > buttons under product catalog)
    Given Open product catalog page
    When Click on sorting dropdown list
    And Select Sort by average rating
    And Click on > in page list
    Then Second catalog page is open

  Scenario: Url https://gettop.us/shop/?orderby=rating opens page with results sorted by Rating
    Given Open url https://gettop.us/shop/?orderby=rating
    Then 1st product has rating starts displayed after sorting

