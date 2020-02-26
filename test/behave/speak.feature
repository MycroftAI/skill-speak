Feature: mycroft-speak

  Scenario: 
    Given an english speaking user
     When the user says "speak hello jason"
     Then "mycroft-speak" should reply with exactly "hello jason"

  Scenario: 
    Given an english speaking user
     When the user says "say what's up"
     Then "mycroft-speak" should reply with exactly "what's up"
