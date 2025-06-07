## 11 Message Log

The purpose of the message log is to provide means to prove the reception of a regular request or response message to a third party. The Security Server supports three options for configuring message log:

- Full logging
  - The whole message including both message body and metadata is logged. The log records can be verified afterwards and they can be used as evidence.
- Metadata logging
  - Only metadata is logged while message body is not logged. Verifying the log records afterwards is not possible and they cannot be used as evidence.
- No message logging
  - Message logging is fully disabled, neither message body nor metadata is logged. No log records are generated.

Full logging and metadata logging can be configured on Security Server and subsystem level. When the Security Server level configuration is used, the same configuration is applied to all the subsystems. Instead, when the subsystem level configuration is used, the configuration is applied to specific subsystems only. In addition, combining the Security Server and subsystem level configurations is also possible, e.g., set metadata logging on the Security Server level and enable full logging for specific subsystems only. Instead, message logging is fully disabled on a Security Server level. Therefore, a subsystem that requires full or metadata logging should not be registered on the same Security Server with a subsystem that requires fully disabling message logging.

Regardless of how logging is configured, messages exchanged between Security Servers are always signed and encrypted. Also, when full logging or metadata logging is enabled, the Security Server produces a signed and timestamped document (Associated Signature Container [ASiC]) for regular requests and responses.

Message log data is stored to the database of the Security Server during message exchange. When storing messages to the database, the message body can be optionally encrypted, but by default the encryption is switched off. According to the configuration ([11.1.4 Timestamping Parameters](#1114-timestamping-parameters)), the timestamping of the signatures of the exchanged messages is either synchronous to the message exchange process or is done asynchronously using the time period set by the X-Road governing agency. In case message logging is fully disabled, timestamping doesn't occur at all.

In case of synchronous timestamping, the timestamping is an integral part of the message exchange process (one timestamp is taken for the request and another for the response). If the timestamping fails, the message exchange fails as well and the Security Server responds with an error message.

In case of asynchronous timestamping, all the messages (maximum limit is determined in the configuration, see [11.1.4 Timestamping Parameters](#1114-timestamping-parameters)) stored in the message log since the last periodical timestamping event are timestamped with a single (batch) timestamp. By default, the Security Server uses asynchronous timestamping for better performance and availability.

The Security Server periodically composes signed (and timestamped) documents from the (optionally encrypted) message log data and archives them in the local file system. Archive files are ZIP containers containing one or more signed documents and a special linking information file for additional integrity verification purpose. Message log archive encryption and grouping can be enabled and configured separately. By default, both are disabled. Message grouping can be configured by member or subsystem. By default, all archive files go to the same default group. Grouping and encryption are enabled/disabled on a Security Server level - they are either enabled or disabled for all the members and subsystems. It's not possible to enable/disable neither of them for selected members or subsystems only.