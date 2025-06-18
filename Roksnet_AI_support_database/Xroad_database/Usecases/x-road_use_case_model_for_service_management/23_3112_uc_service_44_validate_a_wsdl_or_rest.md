#### 3.1.12 UC SERVICE\_44: Validate a WSDL or REST

**System**: Security server

**Level**: Subfunction

**Component**: Security server

**Actors**: -

**Brief** **Description**: The system uses a WSDL or REST validation program to
validate a WSDL or REST file. The location of the validation program is
described by the system parameter *wsdl-validator-command* *rest-validator-command*.

**Preconditions**: -

**Postconditions**: -

**Trigger**:

-   Step 6 of 3.1.9.

-   Step 3 of 3.1.16.

**Main** **Success** **Scenario**:

1.  System runs the validation program and verifies that the validation
    did not return any errors or warnings.

**Extensions**:

- 1a. Validation errors were detected by WSDL or REST validation program while validating the WSDL file.
    - 1a.1. Use case terminates with an error message “WSDL (or REST)('X') validation failed” and displays the WSDL or REST  validator output „Y” (where 'X' is the URL of the WSDL and 'Y' is the reason of the failure).

- 1b. Warnings were detected by WSDL or REST validation program while validating the WSDL or REST file.
    - 1b.1. Use case terminates with a warning message “'X'” (where 'X' is the warning message).

- 1c. The validation program crashed while validating the WSDL or REST file.
    - 1c.1. Use case terminates with an error message “WSDL (or REST) ('X') validation failed” and displays the WSDL or REST validator output „Y” (where 'X' is the URL of the WSDL or REST and 'Y' is the reason of the failure).

**Related** **information**: -