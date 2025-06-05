### 3.10 UC MESS\_09: Log Message and Signature to Message Log

**System**: Security server

**Level**: Subfunction

**Component**: Security server

**Actors**: -

**Brief Description**: The system verifies that logging is allowed (if the time of last successful timestamping is older than specified by the security policy, then no more messages are accepted by the message log) and creates a log record containing the message and the signature. If the system is configured for synchronous timestamping, then the logging process includes timestamping of the created log record.

**Preconditions**: -

**Postconditions**: -

**Triggers**:

-   Steps 13 and 21 of [3.3](#33-uc-mess_02-process-x-road-soap-request).

-   Steps 11 and 19 of [3.4](#34-uc-mess_03-process-x-road-request-message).

**Main Success Scenario**:

1.  System verifies that at least one timestamping service exists in the system configuration.

2.  System verifies that timestamping has not been failing for longer than the period set by the security server system parameter *acceptable-timestamp-failure-period*.

3.  System creates a log record consisting of the SOAP message (attachments are not logged) and the signature and saves the record to message log.

4.  System verifies that the log record should be timestamped synchronously to the messaging process (security server system parameter *timestamp-immediately* value is set to *true*).

5.  System timestamps the message log record: [3.11](#311-uc-mess_10-timestamp-message-log-records) from step 2.

**Extensions**:

1a. No timestamping services are found in the system configuration.

  - 1a.1. System creates an exception message: “Cannot time-stamp messages: no time-stamping services configured“. The use case terminates.

2a. Timestamping has been failing for longer than the allowed period.

  - 2a.1. System creates an exception message: “Cannot time-stamp messages“. The use case terminates.

3a. Creating or saving the log record encounters an error.

  - 3a.1. System creates an exception message containing the details of the encountered error. The use case terminates.

4a. The security server system parameter *timestamp-immediately* value is set to *false*.

  - 4a.1. System timestamps the log record asynchronously, at the next time timestamping is triggered by the timer defined by central server system parameter *timeStampingIntervalSeconds*. The use case terminates.

5a. Timestamping terminates with an exception message.

  - 5a.1. The use case terminates with the exception message.

**Related information**: -