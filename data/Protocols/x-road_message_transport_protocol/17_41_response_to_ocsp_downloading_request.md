### 4.1 Response to OCSP Downloading Request

```http
Content-Type: multipart/related; charset=UTF-8; boundary=jetty625909216ic7gfi1u 

--jetty625909216ic7gfi1u 
Content-Type: application/ocsp-response 

...bytes of the ASN.1-encoded OCSP response...
--jetty625909216ic7gfi1u--
```