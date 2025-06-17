### 2.3 Forcing Missing Timestamps To Be Created

If the security server was configured to timestamp messages asynchronously it may be possible that there is no timestamp associated with one or more signatures of the requested documents. In this case the request will fail with an internal error and return an appropriate error message string - "Some message signatures have not been timestamped yet!" (or "Message signature has not been timestamped yet!" if requesting a single document only).

If this behavior is not desired the following parameter can be used:

* `force` – specifies that the timestamping procedure should be executed explicitly in case any of the requested document signatures have no associated timestamps.

Thus, in order to retrieve the signed document for a message with transaction identifier *abc12345* exchanged by the security server *sec1.gov* by the client *EE/ENT/CLIENT1/SUB* and force any missing timestamps to be created, the request URL is

    http://sec1.gov/asic?queryId=abc12345&xRoadInstance=EE&memberClass=ENT&memberCode=CLIENT1&subsystemCode=SUB&force

Should there be no working time-stamping provider available to the security server, the signed document retrieval service will respond with the error message "Failed to get timestamp from any time-stamping providers".