#### 2.2.2 Initialization Events

The audit log events related to initialization.

| Event                           | Data fields                                                                                                                                                                                                                                               |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Initialize anchor               | <ul><li>anchorFileHash - the hash of the initialized anchor file</li><li>anchorFileHashAlgorithm - the hash algorithm used to calculate value of the field anchorFileHash</li><li>generatedAt - the UTC time when the anchor file was generated</li></ul> |
| Initialize server configuration | <ul><li>ownerIdentifier - the owner identifier of the initialized security server</li><li>serverCode - the server code of the initialized security server</li></ul>                                                                                       |