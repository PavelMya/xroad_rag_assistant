### 6.6 Logging and security

**Audit log** – log, where the user actions (through user interface), when the user changes the system state or configuration, are logged regardless of whether the outcome was a success or failure.

**Batch signature** – e-stamp provided to a set of documents, enabling to separate a single document from the set and verify its signature.

**Message log** – a log, where exchanged X-Road messages are logged and provided with batch signature. Records all regular messages passing through the security server into the database. The messages are stored together with their signatures and signatures are timestamped. The purpose of the message log is to provide means to prove the reception of a request/response message to a third party.

**System service log** – a log which is made from a running system service of a security server, for example from xroad-confclient, -proxy, signer services.