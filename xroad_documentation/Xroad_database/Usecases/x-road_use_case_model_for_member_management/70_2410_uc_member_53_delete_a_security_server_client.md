#### 2.4.10 UC MEMBER\_53: Delete a Security Server Client

**System**: Security server

**Level**: User task

**Component**: Security server

**Actor**: SS administrator

**Brief description**: SS administrator deletes the information about a security server client.

**Preconditions**:

-   The state of the security server client is *saved*, *global error* or *deletion in progress*.

-   The security server client is not the owner of the security server.

**Postcondition**: -

**Trigger**: -

**Main success scenario**:

1.  SS administrator selects to delete a security server client.

2.  System prompts for confirmation.

3.  SS administrator confirms.

4.  System verifies that the signature certificates associated with the client have no other users and asks for confirmation to delete the client's signature certificates.

5.  SS administrator confirms by clicking DELETE button.

6.  System deletes the signature certificates associated with the client from the system configuration.

7.  System deletes the information about the client from the system configuration.

8.  System logs the event “Delete client” to the audit log.

**Extensions**:

3a. SS administrator selects not to delete the client and terminates the use case.

4a. The signature certificates associated with the client have other users. Use case continues form step 7.

5a. SS administrator selects not to delete the signature certificates associated with the client. Use case continues form step 7.

**Related information**:

-   The audit log is located at `/var/log/xroad/audit.log`. The data set of audit log records is described in the document “X-Road: Audit Log Events” \[[SPEC-AL](#Ref_SPEC-AL)\].

-   The security server client state machine model is described in the document “Security Server User Guide” \[[UG-SS](#Ref_UG-SS)\].

### 2.5 Common Use Cases