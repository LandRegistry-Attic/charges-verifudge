Feature: Test Hello World Service

Scenario: Check Hello World Page is Displayed (assert_selector Function)
    Given I visit the Hello World page
    Then the page contains Hello World! (assert_selector)

Scenario: Check Hello World Page is Displayed (assert_match Function)
    Given I visit the Hello World page
    Then the page contains Hello World! (assert_match)

Scenario: Check Goodbye World is Not Displayed
    Given I visit the Hello World page
    Then the page does not contain Goodbye World!
