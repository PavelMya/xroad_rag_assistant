### 3.42 UC SS\_41: Parse User Input

**System**: Security server

**Level**: Subfunction

**Component:** Security server

**Actors**: -

**Brief Description**: System removes the leading and trailing
whitespaces from the user input and verifies that the required fields
are not empty.

**Preconditions**: -

**Postconditions**: -

**Trigger**:

-   Step 2 of 3.23.

-   Step 2 of 3.24.

-   Step 3 of 3.25.

-   Step 3 of 3.26.

-   Step 4 of 3.29.

-   Step 5 of 3.30.

-   Step 2 of 3.35.

**Main Success Scenario**:

1.  System removes leading and trailing whitespaces.

2.  System verifies that mandatory fields are filled.

3.  System verifies that the user input does not exceed 255 characters.

**Extensions**:

- 2a. One or more mandatory fields are not filled.
    - 2a.1. Use case terminates with the error message “Missing parameter: 'X'” (where “X” is the name of the missing parameter).

- 3a. The user input exceeds 255 characters.
    - 3a.1. Use case terminates with the error message “Parameter 'X' input exceeds 255 characters” (where “X” is the name of the parameter).

**Related information:** -