### 2.4 *authCertDeletion* - Security Server Authentication Certificate Deletion

The *authCertDeletion* service is invoked by the Security Server when an authentication certificate is deleted from the server. The body of the authentication certificate deletion message (request or response) contains the following fields:

* **server** – identifier of the Security Server where the authentication certificate is removed;

* **authCert** – contents (in DER encoding) of the authentication certificate that is removed from the Security Server;

* **requestId** – for responses only, unique identifier of the request that is stored in the Central Server database \[[DM-CS](#Ref_DM-CS)\].

The XML Schema fragment of the authentication certificate deletion request body is shown below.

```xml

    
        
        
        
    

```

The response echoes back the client and the server fields of the request and adds the field *requestId*.

An example of the authentication certificate deletion request and response is given in [Annex A.4](#a4-authcertdeletion).