### 2.11 *maintenanceModeDisable* - Disable Maintenance Mode for the Security Server

The *maintenanceModeDisable* service is used to disable maintenance mode for the Security Server. When the maintenance mode is disabled, the Security Server receives requests from other Security Servers.

The body of the maintenance enable message (request or response) contains following fields:

* **server** – identifier of the Security Server where the client is registered;
* **requestId** – for responses only, unique identifier of the request that is stored in the Central Server database \[[DM-CS](#Ref_DM-CS)\].

The XML Schema fragment of the client rename request body shown below.

```xml

    
        
        
        
    

```

The request is sent using HTTP POST method. The content type of the request MUST be *multipart/related* and the request must contain the following MIME parts.

1. X-Road SOAP request message. The message MUST contain the regular X-Road headers and the two data fields (*server*, *client*). The content type of this part MUST be *text/xml*.

2. Signature of owner member of the Security Server. The MIME part must contain signature of the SOAP request message, created with the private key corresponding to a **signing certificate** of the owner member. The content type of this part must be *application/octet-stream*. Additionally, the part MUST include header field *signature-algorithm-ID* that identifies the signature algorithm. Currently supported signature algorithms are *SHA256withRSA*, *SHA384withRSA*, *SHA512withRSA*, *SHA256withRSAandMGF1*, *SHA384withRSAandMGF1*, and *SHA512withRSAandMGF1*.

3. Signing certificate of the owner member that was used to create the second MIME part. The content type of this part MUST be application/octet-stream.

4. OCSP response certifying that the owner member's signing certificate was valid at the time of creation of the request. The content type of this part MUST be application/octet-stream.

The response echoes back the client and the server fields of the request and adds the field *requestId*.

An example of the maintenance mode disable request and response is given in [Annex A.11](#a11-maintenanceModeDisable).

## Annex A. Example messages