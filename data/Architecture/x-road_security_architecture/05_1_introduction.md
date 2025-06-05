## 1 Introduction

X-Road is an open source data exchange layer solution that enables organizations to exchange information over the Internet. X-Road is a centrally managed distributed data exchange layer between information systems that provides a standardized and secure way to produce and consume services. For a more in-depth introduction to X-Road, refer to the X-Road Architecture \[[ARC-G](../Architecture/arc-g_x-road_arhitecture.md)\].

This document describes the X-Road security architecture and how it fulfills security and privacy principles and best practices. Technical descriptions and guides for X-Road components and protocols are found in separate documents. 

Figure 1 X-Road Security Architecture depicts the X-Road environment and its actors and the data exchanges between them. 

<a id="_X_Road_security_architecture" class="anchor"></a>
![](img/arc-sec_x-road_security_architecture_diagram.svg)

Figure 1. X-Road security architecture.

The identity of each organization (X-Road Service Provider or Service Consumer) and technical entry point (Security Server) is verified using certificates that are issued by a trusted Certification Authority (CA) when an organization joins an X-Road ecosystem. The identities are maintained centrally, but all the data is exchanged directly between a consumer and provider. Message routing is based on organization and service level identifiers that are mapped to physical network locations of the services by X-Road. All the evidence regarding data exchange is stored locally by the data exchange parties, and no third parties have access to the data. Time-stamping and digital signature together guarantee non-repudiation of the data sent via X-Road.