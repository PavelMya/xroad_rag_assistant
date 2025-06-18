## 2 Overview

X-Road services are used by X-Road members communicating directly with each other via security servers, using synchronous request-response messaging pattern.

Security servers periodically download global configuration from the central server (see \[[UC-GCONF](#Ref_UC-GCONF)\]). The global configuration is used to check validity of various data items, such as certificates, OCSP responses and timestamps. In addition, the global configuration is used to verify that communicating parties are registered on the X-Road.

Security servers ensure the integrity and confidentiality of the exchanged messages by signing the messages with the X-Road member's signing key and using mutually authenticated Transport Layer Security (TLS) channel for transport. The long-term evidential value of the signed messages is ensured by logging the exchanged messages and periodically timestamping the message logs.

The security servers interact with trust services to acquire certificate validity information and to timestamp signed messages. The trust service calls are asynchronous with respect to the message exchange.

Security servers store operational monitoring data in operational monitoring buffer and forward the data to operational monitoring daemon (see \[[UC-OPMON](#Ref_UC-OPMON)\]).

The communication process between an X-Road service client and an X-Road service provider is described in detail as use cases in [Chapter 3](#3-use-case-model).

The general steps of the communication process, excluding actions that are asynchronous to the message exchange process, are depicted as a sequence diagram in [Annex A](#annex-a-sequence-diagram-for-messaging).

## 3 Use Case Model