#### 2.5.1 UC MEMBER\_54: Parse User Input

**System**: Security server, Central server

**Level**: Subfunction

**Component:** Security server, Central server

**Actors**: -

**Brief Description**: System removes the leading and trailing whitespaces from the user input and verifies that the required fields are not empty.

**Preconditions**: -

**Postconditions**: -

**Triggers**:

-   Step 3 of [2.3.7](#237-uc-member_10-add-an-x-road-member).

-   Step 3 of [2.3.8](#238-uc-member_11-edit-the-name-of-an-x-road-member).

-   Step 7 of [2.3.9](#239-uc-member_12-add-an-owned-security-server-to-an-x-road-member).

-   Step 3 of [2.3.11](#2311-uc-member_56-add-a-subsystem-to-an-x-road-member).

-   Step 4 of [2.3.13](#2313-uc-member_15-create-a-security-server-client-registration-request).

-   Step 3 of [2.3.20](#2320-uc-member_22-edit-the-address-of-a-security-server).

-   Step 3 of [2.3.40](#2340-uc-member_41-add-a-member-class).

-   Step 3 of [2.3.41](#2341-uc-member_42-edit-the-description-of-a-member-class).

-   Step 3 of [2.4.4](#244-uc-member_47-add-a-client-to-the-security-server).

**Main Success Scenario**:

1.  System removes leading and trailing whitespaces.

2.  System verifies that the mandatory fields are filled.

3.  System verifies that the user input does not exceed 255 characters.

**Extensions**:

2a. One or more mandatory fields are not filled.

  - 2a.1. Use case terminates with the error message “Missing parameter: 'X'”, where “X” is the name of the missing parameter.

3a. The user input exceeds 255 symbols.

  - 3a.1. Use case terminates with the error message “Parameter X input exceeds 255 characters”, where “X” is the name of the parameter that had more than 255 characters inserted.

**Related information**: -