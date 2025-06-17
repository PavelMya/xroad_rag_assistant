### 2.6 *addressChange* - Security Server address change

The service is used to change the Security Server address from Security Server.

The body of the address change message (request or response) contains the following fields:

* **server** – identifier of the Security Server where the owner is changed;
* **address** – new Security Server DNS address;
* **requestId** – for responses only, unique identifier of the request that is stored in the Central Server database \[[DM-CS](#Ref_DM-CS)\].

The XML Schema fragment of the address change request body is shown below. For clarity, documentation in the schema fragment is omitted.

```xml

    
        
        
        
    

```

The request is sent using HTTP POST method. The content type of the request MUST be *multipart/related* and the request must contain the following MIME parts.

1. X-Road SOAP request message. The message MUST contain the regular X-Road headers and the two data fields (*server*, *client*). The content type of this part MUST be *text/xml*.
 
2. Signature of owner member of the Security Server. The MIME part must contain signature of the SOAP request message, created with the private key corresponding to a **signing certificate** of the owner member. The content type of this part must be *application/octet-stream*. Additionally, the part MUST include header field *signature-algorithm-ID* that identifies the signature algorithm. Currently supported signature algorithms are *SHA256withRSA*, *SHA384withRSA*, *SHA512withRSA*, *SHA256withRSAandMGF1*, *SHA384withRSAandMGF1*, and *SHA512withRSAandMGF1*.
 
3. Signing certificate of the owner member that was used to create the second MIME part. The content type of this part MUST be *application/octet-stream*.
 
4. OCSP response certifying that the owner member's signing certificate was valid at the time of creation of the request. The content type of this part MUST be *application/octet-stream*.

The response echoes back the server and the client fields of the request and adds the field *requestId*.

An example of the address change request and response is given in [Annex A.6](#a6-addresschange)).