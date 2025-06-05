### 3.20 UC TRUST\_19: Parse User Input

**System**: Central server

**Level**: Subfunction

**Component:** Central server

**Actors**: -

**Brief Description**: System removes the leading and trailing
whitespaces from the user input and verifies that the required fields
are not empty.

**Preconditions**: -

**Postconditions**: -

**Triggers**:

-   Step 6 of 3.9.

-   Step 3 of 3.10.

-   Step 5 of 3.11.

-   Step 5 of 3.17.

-   Step 3 of 3.18.

**Main Success Scenario**:

1.  System removes leading and trailing whitespaces.

2.  System verifies that the mandatory fields are filled.

3.  System verifies that the user input does not exceed 255 characters.

**Extensions**:

- 2a. One or more mandatory fields are not filled.
    - 2a.1. Use case terminates with the error message “Missing parameter: 'X'”, where “X” is the name of the missing parameter.

- 3a. The user input exceeds 255 symbols.
    - 3a.1. Use case terminates with the error message “Parameter X input exceeds 255 characters”, where “X” is the name of the parameter that had more than 255 characters inserted.

**Related information**: -