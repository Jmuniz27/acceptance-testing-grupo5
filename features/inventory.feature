# language: en
Feature: Inventory management
  As a store manager
  I want to add, list, update, remove and search products in my inventory
  So that I can keep my stock information accurate and up to date

  Scenario: Add a product to the inventory
    Given the inventory is empty
    When the user adds a product "Coffee"
    Then the inventory should contain "Coffee"

  Scenario: List all products in the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user lists all products
    Then the output should contain:
      """
      Products:
      - Coffee
      - Sugar
      """

  Scenario: Update the quantity of a product
    Given the inventory contains products:
      | Product | Quantity |
      | Coffee  | 10       |
    When the user updates product "Coffee" to quantity "25"
    Then the inventory should show product "Coffee" with quantity "25"

  Scenario: Remove a product from the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user removes the product "Coffee"
    Then the inventory should not contain "Coffee"

  Scenario: Search products by category
    Given the inventory contains products:
      | Product | Category  |
      | Coffee  | Beverages |
      | Tea     | Beverages |
      | Sugar   | Grocery   |
    When the user searches for products in category "Beverages"
    Then the output should contain:
      """
      Products:
      - Coffee
      - Tea
      """
