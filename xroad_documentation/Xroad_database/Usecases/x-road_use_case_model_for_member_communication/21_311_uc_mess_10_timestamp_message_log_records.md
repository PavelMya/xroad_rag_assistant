### 3.11 UC MESS\_10: Timestamp Message Log Records

**System**: Security server

**Level**: Subfunction

**Component**: Security server

**Actor**: TSS

**Brief Description**: The system finds log records that need to be timestamped, creates a timestamping request and sends it to the TSS. Upon receiving the response from the TSS, the system validates the response and logs it to the message log.

**Preconditions**: -

**Postconditions**: -

**Triggers**:

-   Step 5 of [3.10](#310-uc-mess_09-log-message-and-signature-to-message-log) if the security server system parameter *timestamp-immediately* value is set to *true.*

-   Timer defined by central server system parameter *timeStampingIntervalSeconds* if the security server system parameter *timestamp-immediately* value is set to *false.*

**Main Success Scenario**:

1.  System verifies that message log records that need to be timestamped exist.

2.  System verifies that the system configuration contains valid global configuration.

3.  System looks up timestamping service addresses from the system configuration.

4.  System creates timestamping request, sends the request to the first timestamping service found in the system configuration and receives the response.

5.  System reads the response and verifies that the timestamp was granted (status of the response is either *granted* or *grantedWithMods*).

6.  System verifies that the response corresponds with the request.

7.  System verifies that the timestamp is signed by an approved timestamping authority.

8.  System creates a timestamp record that contains the timestamp and saves the timestamp record to database. System associates the timestamped message records with the timestamp record.

**Extensions**:

1a. No log records that need timestamping are found.

  - 1a.1. The use case terminates.

2a. Global configuration is expired.

  - 2a.1. System creates an exception message: “Global configuration is expired”. The use case terminates.

3a. No timestamping services are found in the system configuration.

  - 3a.1. System creates an exception message: “Cannot time-stamp, no TSP URLs configured“. The use case terminates.

4a. System failed to get a response from the timestamping service.

  - 4a.1. System sends the timestamping request to the next timestamping service found in the system configuration.

    - 4a.1a. System fails to get a response. The use case continues from step 4a.1.

    - 4a.1b. System has tried and failed to get a response from all the timestamping services listed in the system configuration.

      - 4a.1b.1. System creates an exception message: “Failed to get time stamp from any time-stamping providers“. The use case terminates.

5a. System failed to read the response.

  - 5a.1. System creates an exception message: “Could not read time-stamp response“. The use case terminates.

5b. Timestamp was not granted.

  - 5b.1. System creates an exception message containing the response status information. The use case terminates.

6a. The verification resulted in an error (the response does not correspond to the request).

  - 6a.1. System creates an exception message containing the details of the encountered error. The use case terminates.

7a. System does not find the certificate of the timestamp signer from the list of approved timestamping services.

  - 7a.1. System creates an exception message: “Could not find TSP certificate for timestamp“. The use case terminates.

7b. System fails to get timestamp signer information.

  - 7b.1. System creates an exception message: “Could not get signer information for X” (where “X” is the serial number of the certificate used to sign the timestamp.). The use case terminates.

7c. Verification of the signature fails.

  - 7c.1. System creates an exception message: “Failed to verify timestamp“. The use case terminates.

8a. Creating or saving the log record fails or associating the log records with the timestamp record fails.

  - 8a.1. System creates an exception message containing the error information. The use case terminates.

**Related information**:

-   Information about timestamping in X-Road system can be found in documents “Profile for High-Perfomance Digital Signature” \[[HPDS](#Ref_HPDS)\] and “Using Batch Hashing for Signing and Time-Stamping” \[[BATCH](#Ref_BATCH)\].