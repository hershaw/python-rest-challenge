# Python challenge

This code challenge will consist of you building a very simple
REST api to keep track of loan applications. There is no frontend to this, its as simple as it sounds.

If there are bugs or conceptual mistakes in the test itself, don't
be shy about bringing them up. You get huge big bonus points for
proactivity and critical thinking in general.

## Concepts to cover

This challenge is meant to cover the following concepts

- REST api implementation
- Have a database backing it
- Provide documentation (via a README is enough)
- Testing
    - use behave
- Git
    - Forks, PRs, code reviews.
- pip

## Dependencies

The dependencies listed below are **suggestions**. If you know
of a library that clearly better than one that we have suggested,
you are free to use it as long as you can justify yourself.

- python 3
  - this one is pretty much required. if you want to use python 2
    you better have a REALLY good reason.
- mongodb
    - You can choose any mongodb python drivers
- [flask](http://flask.pocoo.org/) for your webserver
    - For testing, use [test_client()](http://flask.pocoo.org/docs/0.12/testing/)
- [webargs](https://webargs.readthedocs.io/en/latest/) for validation
- [behave](http://pythonhosted.org/behave/) for testing

## Assignment

You will take the following Gherkin requirements and implement
and test a REST API that satisfies the expressed business needs.

```
Feature: Loan applications API
  REST API for integration with loan application frontends built by
  client IT departments.

  Scenario: Add a new loan application
    Given the webserver is running
    And a valid application is generated
    When the endpoint POST /application is called
    Then the ID of the application is returned
    And the loan exists in the database
    
  Scenario: Attempt to add application with missing field
    Given the webserver is running
    And an application with age missing is generated
    When the endpoint POST /application is called
    Then an error message saying age is missing is returned
    And status 422 is returned
    
  Scenario: Attempt to add application with incorrect type
    Given the webserver is running
    And an application with age as a string is generated
    When the endpoint POST /application is called
    Then an error message saying age has wrong type is returned
    And status 422 is returned

  Scenario: Fetch an application by ID
    Given the webserver is running
    And an application exists in the database with id "1"
    When GET /application is called with the id of "1"
    Then the correct application is returned
    And status 200 is returned
    
  Scenario: Update an application by ID
    Given the webserver is running
    And an application exists in the database
    When PATCH /application is called to update a field
    Then the update is recorded in the database
    And status 200 is returned
    
  Scenario: Delete an application by ID
    Given the webserver is running
    And an application exists in the database
    When DELETE /application is called to delete a known application
    Then the application is no longer in the database
    And status 200 is returned

```

Applications must have the following types and keys. Anything that
does not have the correct types or keys is considered invalid.

```
{
  "age": <int>,
  "income": <float>,
  "employed": <boolean>
}
```

## Implementation
1. Fork this repo, take a branch, and write your code there
1. Add me [hershaw](https://github.com/hershaw) as a collaborator
  and when you are ready to submit, issue a PR to master in your
  own fork and I will review it
      
## Submission

The assignment is considered complete with the following conditions:

1. there is a `pip-requirements.txt` file
1. all tests pass
1. you can start the webserver and make curl requests
1. a comprehensive readme exists

To submit, add me as a contributor to the repo and mention me in a comment so I recieve a notification and our team can review it.
