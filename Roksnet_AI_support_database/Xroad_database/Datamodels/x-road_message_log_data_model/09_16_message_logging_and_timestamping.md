### 1.6 Message Logging and Timestamping

The input to the message log component consists of a message and its corresponding signature (along with hash chain and hash chain result if the signature is a batch signature). Depending on the security policy, timestamping can be asynchronous (one or more signatures are batch timestamped) or synchronous (to guarantee the timestamp).

The process of logging and asynchronous timestamping consists of the following steps:

1. System verifies that the message and signature can be logged – if the time of last successful timestamping is older than specified by the security policy then no more messages are accepted by the system and the situation should be considered as system failure.
2. System saves the message and signature in the message log. The message body is stored in encrypted format if the parameter `messagelog-encryption-enabled` is enabled.
3. System periodically timestamps messages that have no timestamp. Batch timestamp is created if more than one message is timestamped simultaneously. Regular timestamp is created for single messages.

When timestamping synchronously, the logging call will block until the timestamp is received. The process of synchronous timestamping consists of the following steps:

1. The system saves the message and signature in the message log.
2. System timestamps the message synchronously.

### 1.7 Entity-Relationship Diagram

![Entity-Relationship Diagram](img/messagelog-er.svg)

## 2. Description of Entities