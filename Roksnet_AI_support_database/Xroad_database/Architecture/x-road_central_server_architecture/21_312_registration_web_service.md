### 3.1.2 Registration Web Service

Registration web service is called by Security Servers to register an authentication certificate.

The registration web service interface is a synchronous RPC-style interface provided by the registration web service component. It validates the requests and forwards them to the Central Server management REST API. The service is called by Security Servers.

The interface is described in more detail in \[[ARC-G](#Ref_ARC-G)\], \[[PR-MSERV](#Ref_PR-MSERV)\].