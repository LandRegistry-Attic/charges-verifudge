Feature: Create a new Identity

@delete_identity_afterwards
Scenario: Create an Identity
    Given I am on the identity list
    When I create an identity for John Smith:
      | address_line1 | 123 Fake Street |
      | postcode      | AB12 3CD        |
      | dob           | 12 Oct 1988     |
      | gender        | male            |
    Then John Smith should be listed on the identity list
    And John Smith's address is 123 Fake Street, AB12 3CD
    And John Smith's date of birth is 12 October 1988
    And John Smith's gender is male

