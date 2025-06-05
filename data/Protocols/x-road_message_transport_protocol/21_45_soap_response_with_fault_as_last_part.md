### 4.5 SOAP Response with Fault as Last Part

```http
Content-Type: multipart/mixed; charset=UTF-8; boundary=xatt569125687hcu8vfma

--xatt569125687hcu8vfma
Content-Type: text/xml; charset=UTF-8

...response SOAP...
--xatt569125687hcu8vfma
Content-Type: text/xml; charset=UTF-8

...SOAP fault...
--xatt569125687hcu8vfma--
```