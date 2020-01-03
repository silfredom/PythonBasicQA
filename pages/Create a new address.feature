
Feature: Create a new address

  @regression @smoke @newaddress @address
  Scenario: Create a new address
    Given I navigate to Cornershop qa page
    And I log in with a valid account




#### Create a new address
##### Pre-conditions
Have an account of an existing user.
##### Steps
1. Navigate to the site
2. Click on “Log in” button
3. Login with a valid account
	* Enter an existing user email address
	* Enter its password
	* Click on “Log in”

4. Dismiss starter tutorial (this is shown only for new accounts with no address)
5. Complete the “Add address” form and submit it
	* Enter a name for the address
	* Select the address tupe
	* Enter the street address
	* Select a city, locality and country
	* Click on “Continue”
6. Click on “Save” in the “Adjust location” step

##### Expected result
The new address added should be shown at the top left corner next to a blue house icon.

