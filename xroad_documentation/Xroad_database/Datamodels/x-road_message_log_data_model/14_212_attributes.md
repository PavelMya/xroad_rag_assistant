#### 2.1.2 Attributes

| Name                 | Type                   | Modifiers  | Description |
| -------------------- |:----------------------:| ----------:| -----------:|
| id [PK]              | bigint                 | NOT NULL   | Primary key |
| discriminator        | character varying(255) | NOT NULL   | Technical attribute, specifying the Java class to which the log record is mapped. The possible values are “m” (MessageRecord) and “t” (TimestampRecord). The corresponding Java classes are located in the ee.ria.xroad.common.messagelog package. |
| time                 | bigint                 |            | The creation time of the log record (number of milliseconds since January 1, 1970, 00:00:00 GMT). |
| archived             | boolean                |            | A flag indicating whether this log record has been archived. |
| queryid              | character varying(255) |            | The id field of the SOAP message header. Only present for message records. |
| message              | text                   |            | The SOAP message body or REST request data. Only present for message records. Created only when encryption is switched off. |
| signature            | text                   |            | The signature of the message. Only present for message records. |
| hashchain            | text                   |            | If the signature is a batch signature, the base-64 encoded hash chain. Only present for message records. |
| hashchainresult      | text                   |            | If the signature is a batch signature, the base-64 encoded hash chain result. Only present for message records. |
| signaturehash        | text                   |            | Hash of the signature of the message. Only present for message records. |
| timestamprecord [FK] | bigint                 |            | Identifies the timestamp record that timestamps this message record. References id attribute of LOGRECORD entity. Only present for message records. |
| timestamphashchain   | text                   |            | If the message record is time-stamped, the base-64 encoded hash chain of the timestamp. Only present for message records. |
| response             | boolean                |            | A flag indicating whether the message in this log record is a response message (as opposed to a request message). Only present for message | timestamp            | text                   |            | Base64-encoded contents of the time stamp.  Only present for timestamp records |
| memberclass          | character varying(255) |            | Member class of the client who sent this message. Only present for message records. |
| membercode           | character varying(255) |            | Member code of the client who sent this message. Only present for message records. |
| subsystemcode        | character varying(255) |            | Subsystem code of the client who sent this message. Only present for message records. |
| attachment           | oid                    |            | The REST message body (a large binary object) |
| xrequestid           | character varying(255) |            | An optional id which is shared between a request and a response. |
| keyid                | character varying(255) |            | ID of the key used to encrypt/decrypt the message. |
| ciphermessage        | bytea                  |            | The SOAP message body or REST request data in encrypted form. Only present for message records. Created only when encryption is switched on. |