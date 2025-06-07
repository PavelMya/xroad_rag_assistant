#### 3.1.10 UC SERVICE\_09: Edit the Address of a WSDL or REST

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator changes the URL of a WSDL or REST.

**Preconditions**: -

**Postconditions**: -

**Trigger**: SS administrator wants to change the URL of a WSDL or REST.

**Main** **Success** **Scenario**:

1.  SS administrator selects to edit the URL of a WSDL or REST.

2.  SS administrator inserts the new URL of the WSDL or REST.

3.  System parses the user input: 3.1.13.

4.  System verifies that the inserted URL does not already exist in the
    list of WSDL or REST URLs saved in the system configuration for this client.

5.  System refreshes the WSDL or REST: steps 2-6 of 3.1.16.

6.  System logs the event “Edit service description” to the audit log.

**Extensions**:

- 3a. The process of parsing the user input terminated with an error message.
    - 3a.1. System displays the error message “X” (where “X” is the termination message from the parsing process).
    - 3a.2. System logs the event “Edit service description failed” to the audit log.
    - 3a.3. SS administrator selects to reinsert the URL of the WSDL or REST. Use case continues from step 3.
    - 3a.3a. SS administrator selects to terminate the use case.

- 4a. The inserted URL already exists.
    - 4a.1. System displays the error message “Failed to edit WSDL (or REST): WSDL (or REST) address already exists.”.
    - 4a.2. System logs the event “Edit service description failed” to the audit log.
    - 4a.3. SS administrator selects to reinsert the URL of the WSDL or REST. Use case continues from step 3.
        - 4a.3a. SS administrator selects to terminate the use case.

- 5a. The process of refreshing the WSDL or REST file terminated with an error message.
    - 5a.1. System displays the error message “Failed to edit WSDL (or REST): 'X'” (where “X” is the termination message from the refreshing process).
    - 5a.2. System logs the event “Edit service description failed” to the audit log.
    - 5a.3. SS administrator selects to reinsert the URL of the WSDL or REST. Use case continues from step 3.
        - 5a.3a. SS administrator selects to terminate the use case.

**Related** **information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].