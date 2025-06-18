## 6 Authentication

For compliance with the security principle of authentication, the objective is to ensure that the provenance (identity) of the X-Road asset or X-Road actor is known and verified. This is accomplished in a standardised manner using authentication keys and certificates. With assurance of integrity, the threat being mitigated is unauthorised access to X-Road infrastructure and assets therein.

X-Road enforces organisation-level authentication (and authorization) mechanisms and for X-Road Administrator web application frontend-to-backend connections and direct calls to the backend for configuration and maintenance automation purposes.

An X-Road organisation’s client information system Security Server acts as the entry point to all the X-Road services. The client information system is responsible for implementing an end user authentication and access control mechanism that complies with the requirements of the particular X-Road instance. The identity of the end user may be made available to the service provider by including it in the service request. 

In case a Security Server becomes compromised, it can be blocked from the X-Road instance by revoking its authentication certificate or removing it from the Central Server's configuration. Similarly, a selected member organisation or subsystem can be blocked out centrally without affecting other Security Servers, members or subsystems.

For details on X-Road Administrator web application user management-related authentication, refer to \[[UG-SS](#Ref_UG-SS)\] section 2.

For details on configuring a Security Server’s authentication key and certificate, refer to \[[UG-SS](#Ref_UG-SS)\] section 3.2.

For details on registering a Security Server’s authentication key and certificate in the Central Server, refer to \[[UG-CS](#Ref_UG-SS)\] section 8.3.

## 7 Access Control
 
For compliance with the security principle of least privilege, the objective is to ensure that X-Road actors, processes and controls must be able to access only the X-Road information and resources that are limited to and necessary for the legitimate and intended purpose.