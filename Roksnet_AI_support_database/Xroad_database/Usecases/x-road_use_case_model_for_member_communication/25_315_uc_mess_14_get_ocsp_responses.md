### 3.15 UC MESS\_14: Get OCSP Responses

**System**: Security server

**Level**: Subfunction

**Component**: Security server

**Actors**: -

**Brief Description**: System gets and caches OCSP responses for usable certificates using OCSP responders defined in the global configuration.

**Preconditions**: -

**Postconditions**: -

**Trigger**: Timer. The system calculates the timer interval by dividing the central server system parameter *ocspFreshnessSeconds* value by 10.

The value of *ocspFreshnessSeconds* determines the validity period of the cached OCSP responses. To buffer against temporary OCSP responder service malfunctions or system failures, the refresh interval of the responses is set to 10 times less than the validity period.

**Main Success Scenario**:

1.  System verifies that the system configuration contains valid global configuration.

2.  System finds certificates from the system configuration that are in *Registered* state and not disabled or expired.

3.  System gets an OCSP response for each found certificate: [3.16](#316-uc-mess_15-get-and-verify-ocsp-response).

4.  System caches the received OCSP responses.

**Extensions**:

1a. Global configuration is expired.

  - 1a.1. System creates an exception message: “Global configuration is expired”. The use case terminates.

2a. System cannot find any certificates that are not disabled or expired.

  - 2a.1. The use case terminates.

**Related information**: -