Feature: Amazon Login
    Background: base
        Given User initialize the browser
        When  User launch the application
        Then user can see the title of page as "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"

    Scenario: Login to Amazon with valid credentials
        Given User clicks on the signin
        When User fills phone number "********"
        And user click continue 
        And User enter password "*******"
        And User should see forgot password "Forgot password?"
        And user click signin
        Then user can see their name "Raksha" at right top


    Scenario: Login to Amazon with invalid password credentials
        Given User clicks on the signin
        When User fills phone number "*******"
        And user click continue 
        And User enter password "*******"
        And User should see forgot password "Forgot password?"
        And user click signin
        Then user should see "Your password is incorrect"

    Scenario: Login to Amazon with invalid phone number
        Given User clicks on the signin
        When User fills phone number "*******"
        And user click continue 
        And User should see phonenumber eror "We cannot find an account with that mobile number"
    
    Scenario: Login to Amazon with forgot password
        Given User clicks on the signin
        When User fills phone number "*******"
        And user click continue 
        And User should see forgot password "Forgot password?"
        And user click forgot password
       