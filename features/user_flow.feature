@tags @tag
Feature: User Flow

  As a user I want to get Car insurance quotes

  Background:
    Given User navigates to main page

  @positive
  Scenario: Get quotes for auto insurance
    When User chooses "Car insurance" option
    And User types zip code "12345"
    And User clicks "Start" button
      Then User is referred to page1 of questionnaire
      When User selects "No" for having car insurance as of today
      And User selects "I own my home"
      And User selects "I need car insurance now"
      And User clicks Save button
    Then User is referred to page2 of questionnaire
      When User chooses "2020" for a vehicle year
      And User chooses "Cadillac" for a vehicle make
      And User chooses "Xt4" for a vehicle model
      And User chooses "Luxury4drCrossover" for a vehicle trim
      And User clicks Save vehicle button
    Then User is referred to page3 of questionnaire
      When User chooses "Own - paid in full" for a type of ownership
      And User chooses "Personal/Commuting" for primary use
      And User enters "10000" for mileage
      And User selects "per year" for frequency
      And User clicks Save vehicle details button
    Then User is referred to page4 of questionnaire
      When User enters personal information: "John", "Reddik", "04/28/1985", "123 Zebra Dr"
      And User clicks Save driver details button
    Then User is referred to page5 of questionnaire
      When User provides information: "Male", "Single", "Excellent", "No diploma", "No violations", "John.Reddik@gmail.com", "No"
    And User clicks Show my quotes button
    Then User is referred to final page of questionnaire
