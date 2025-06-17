### 2.2 Message Log

Records all regular messages passing through the security server into the database. The messages are stored together with their signatures and signatures are timestamped. The purpose of the message log is to provide means to prove the reception of a request/response message to a third party.

Archives periodically log records from database as signed documents on the disk and purges archived log records from database. By default, all the signed documents on the disk are grouped together, but grouping them by member or subsystem is also supported.

Both the records in the messagelog database and the message archives can be optionally encrypted (opt-in).

Provides a service that allows the retrieval of signed documents (from database) containing the stored information.

The component is a proxy addon.

### 2.3 Metadata Services

Provides methods that can be used by X-Road participants to discover what services are available from the security server.

The component is a proxy addon.