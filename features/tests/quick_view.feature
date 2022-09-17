# Created by Inga at 17.09.2022
Feature: Quick View function is clickable and enables user to add products

  Scenario: User can open and close Quick View by clicking on closing X
    Given Open product catalog page
    When Hover over product image
    And Click on Quick view link
    Then Quick view overlay window is open
    And Click on closing X
    And Catalog page is back


  Scenario: User can click Quick View and add product to cart
    Given Open product catalog page
    When Hover over product image
    And Click on Quick view link
    Then Quick view overlay window is open
    And Click on Add to cart button
    And Header cart features one item