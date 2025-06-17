### 2.2 Downloading OCSP Responses from Service Provider

Each X-Road security server only interacts with the CA that issued the certificates used by it. For this reason, the OCSP responses for certificates are always transferred together with the certificates themselves. The security servers cache the OCSP responses for their certificates and periodically update this cache.

The service client's security server sends the OCSP responses for authentication certificate as part of the request message. However, before sending the request the client's security server must verify service provider's security server's authentication certificate. Because the OCSP stapling specification is not widely implemented yet, the client's security server downloads the OCSP responses from the service provider's security server using a separate channel (HTTP).

Service provider's security server must respond to HTTP GET requests to port 5577 (default configuration). In the HTTP GET request the client's security server indicates the certificates whose OCSP responses are requested. For this, the client includes cert query parameters whose content is hexadecimally encoded SHA-1 hashes of the certificates. For example, the following URL is used to retrieve OCSP responses for two certificates: 

`http://SECURITYSERVER:5577/?cert=a1b2c3d4e5&cert=f6g7h8i9j0`

where SECURITYSERVER is the address of the service provider's security server.

As a response to this request the service responds with a MIME multipart message (`multipart/related`). Each part of this message must contain a requested OCSP responses with content-type `application/ocsp-response`. See Annex [4.1](#41-response-to-ocsp-downloading-request) for an example response.