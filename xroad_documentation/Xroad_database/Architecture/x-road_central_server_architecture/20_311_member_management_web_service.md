### 3.1.1 Member Management Web Service

Member management web service is called by Security Servers to perform management tasks such as registering a Security Server client or deleting an authentication certificate.

The member management web service interface is a synchronous RPC-style interface provided by the member management web service component. It validates the requests and forwards them to the Central Server management REST API. The service is called by Security Servers.

The interface is described in more detail in \[[ARC-G](#Ref_ARC-G)\], \[[PR-MSERV](#Ref_PR-MSERV)\].