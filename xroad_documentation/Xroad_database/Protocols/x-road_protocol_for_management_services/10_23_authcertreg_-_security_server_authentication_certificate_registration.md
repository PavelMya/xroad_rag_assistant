### 2.3 *authCertReg* - Security Server Authentication Certificate Registration

The *authCertReg* service is invoked by the Security Server when a new authentication certificate is added to the server.

The body of the authentication certificate registration message (request or response) contains the following fields:

* **server** – identifier of the Security Server where the authentication certificate is added;

* **address** – DNS address of the Security Server;

* **authCert** – contents (in DER encoding \[[DER](#Ref_DER)\]) of the authentication certificate that will be added to the Security Server;

* **requestId** – for responses only, unique identifier of the request that is stored in the Central Server database \[[DM-CS](#Ref_DM-CS)\].

The XML Schema fragment of the authentication certificate registration request body is shown below. For clarity, documentation in the schema fragment is omitted.

```xml

    
        
        
        
        
    

```

Unlike the other requests, the authentication certificate registration request cannot be sent as a regular X-Road request. This is caused by a bootstrapping problem – sending an X‑Road message requires that the authentication certificate of the Security Server is registered at the Central Server. However, the certificate is registered only as a result of invoking this service. Therefore, another mechanism is needed.

The authentication certificate registration request is sent to the Central Server directly via HTTPS. When making the HTTPS connection the client MUST verify that the server uses the TLS certificate that is given in the global configuration.

If the Central Server encounters an error, it responds with a SOAP fault message.

The request is sent using HTTP POST method. The content type of the request MUST be *multipart/related* and the request must contain the following MIME parts.

1. X-Road SOAP request message. The message MUST contain the regular X-Road headers and the three data fields (*server*, *address*, *authCert*). The content type of this part MUST be *text/xml*.

2. Proof of possession of the authentication key. The MIME part must contain signature of the SOAP request message (the body of the first MIME part). The signature MUST be given using the private key corresponding to the **authentication certificate** that is being registered (*authCert* field of the SOAP message). The content type of this part must be *application/octet-stream*. Additionally, the part MUST include header field *signature-algorithm-ID* that identifies the signature algorithm. Currently supported signature algorithms are *SHA256withRSA*, *SHA384withRSA*, and *SHA512withRSA*.

3. Signature of the Security Server's owner. The MIME part must contain signature of the SOAP request message, created with the private key corresponding to a **signing certificate** of the Security Server's owner. The content type of this part must be *application/octet-stream*. Additionally, the part MUST include header field *signature-algorithm-ID* that identifies the signature algorithm. Currently supported signature algorithms are *SHA256withRSA*, *SHA384withRSA*, *SHA512withRSA*, *SHA256withRSAandMGF1*, *SHA384withRSAandMGF1*, and *SHA512withRSAandMGF1*.

4. Authentication certificate that is being registered (*authCert* field of the SOAP message). The content type of this part MUST be *application/octet-stream*.

5. Signing certificate of the Security Server's owner that was used to create the third MIME part. The content type of this part MUST be *application/octet-stream*.

6. OCSP response certifying that the signing certificate was valid at the time of creation of the request. The content type of this part MUST be *application/octet-stream*.

The Central Server sends responds with X-Road response message (content type MUST be *text/xml*). The response echoes back the three fields of the SOAP request and adds the field *requestId*.

An example of the authentication certificate registration request and response is given in [Annex A.3](#a3-authcertreg).