#### 3.1.13 UC SERVICE\_11: Parse User Input

**System**: Security server, central server

**Level**: Subfunction

**Component**: Security server, central server

**Actors**: -

**Brief** **Description**: System parses the user input and verifies
that the input is well formatted.

**Preconditions**: -

**Postconditions**: -

**Trigger**:

-   Step 3 of 3.1.9.

-   Step 3 of 3.1.10.

-   Step 4 of 3.1.15.

-   Step 3 of 3.1.21.

-   Step 3 of 3.1.23.

-   Step 3 of 3.1.27.

-   Step 3 of 3.1.30.

-   Step 3 of 3.2.4.

-   Step 3 of 3.2.7.

-   Step 3 of 3.2.13.

-   Step 3 of 3.2.14.

**Main** **Success** **Scenario**:

1.  System removes leading and trailing whitespaces.

2.  System verifies that mandatory fields are filled.

3.  System verifies that the user input does not exceed 255 characters.

**Extensions**:

- 2a. One or more mandatory fields are not filled.
    - 2a.1. Use case terminates with the error message “Missing parameter: 'X'” (where “X” is the name of the missing parameter).

- 3a. The user input exceeds 255 characters.
    - 3a.1. Use case terminates with the error message "Parameter 'X' input exceeds 255 characters" (where “X” is the name of the parameter).

**Related** **information**: -