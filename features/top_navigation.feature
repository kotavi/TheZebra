@tags @tag
Feature: Top navigation header

  As a user I want to be able to use the header section of the page

  Background:
    Given User navigates to main page
    And Top navigation items are present

  @smoke @positive
  Scenario Outline: User can open <Test name> top navigation link
    When User opens "Compare" menu
        And User clicks on "<Link Name>" link
      Then "<Link Name>" page with correct title will be opened

    Examples:
    | Test name         | Link Name          |
    | Auto Insurance    |  Auto Insurance    |
    | Home Insurance    |  Home Insurance    |

  @smoke @positive
  Scenario: Check 'Get Quotes' button
    When User scrolls down the page
    Then "Get Quotes" button appears
