@tags @tag
Feature: Main page

  As a user I want to have access to all elements of the page

  Background:
    Given User navigates to main page

  @smoke @positive
  Scenario: Check 'Compare insurance quotes instantly.' components
    When User chooses "Car insurance" option
    Then User chooses "Home insurance" option
    Then User clicks on "Zip code" field
    Then User clicks "Start" button