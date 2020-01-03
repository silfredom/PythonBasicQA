
Feature: Create an account

  @regression @smoke @newaccount @account
  Scenario: Create an account
    Given I navigate to Cornershop
    And I Sign up using this information:
      | Email                 | Name                 | Last name           | Password            |
      | new valid email       | AutomationName       | Automation Lastname | Qwertyisbadpassword |
      Then A message should be present stating: "Thank you for joining Cornershop Automationname. Confirm your email address. One hour grocery delivery is right around the corner."



### Test Cases
#### Create an account
##### Steps
###1. Navigate to the site
###2. Click on “Sign up” button
###3. Complete the sign up form with valid data and submit it
###	* Enter a valid email
###	* Enter a Name
###	* Enter a Last name
###	* Enter a Password
###	* Click on “Sign up” button

##### Expected result
###A message should be present stating “We have sent you an email”. A second message should be present indicating extra instructions for the sign up process to be completed: “Click on the email that we just sent to <email-entered> to activate your account.”
