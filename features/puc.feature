
Feature: #Enter feature name here

  @ui @puc
  Scenario: Verifico el indicador de password strong
    Given I navigate to phpmyadmin
    And I access to users accounts
    Then I fill the passwords inputs with "PUCcurso123"
    And I verify the label is "Strong"

  @ui @puc
  Scenario: Verifico el indicador de password weak
    Given I navigate to phpmyadmin
    And I access to users accounts
    Then I fill the passwords inputs with "PUCcurso"
    And I verify the label is "Weaka"
