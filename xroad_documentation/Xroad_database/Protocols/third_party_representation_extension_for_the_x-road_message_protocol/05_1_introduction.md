## 1 Introduction

This specification describes an extension to the X-Road Message Protocol 4.0 \[[PR-MESS](#Ref_PR-MESS)\].

The purpose of this extension is to allow sending of additional information to the X-Road service providers in case when service client represents third party while issuing a query. The query is initiated by a third party and the results are also forwarded to that third party, but the request itself is signed by service client.

The described scenario can be used by MISP and other portals that offer X-Road services to various types of institutions. These institutions may not be X-Road members and even may not be eligible for becoming ones, but the service agreements between service providers and service clients may allow service clients to forward data received from X-Road services to these institutions.

### 1.1 Terms and abbreviations

See X-Road terms and abbreviations documentation \[[TA-TERMS](#Ref_TERMS)\]

### 1.2 References

| Document ID||
| ------------- |-------------|
| \[PR-MESS\] | [X-Road: Message Protocol v4.0](../pr-mess_x-road_message_protocol.md)
| \[TA-TERMS\] | [X-Road Terms and Abbreviations](../../terms_x-road_docs.md)