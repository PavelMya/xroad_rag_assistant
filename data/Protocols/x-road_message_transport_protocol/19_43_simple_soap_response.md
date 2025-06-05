### 4.3 Simple SOAP Response

```http
Content-Type: multipart/mixed; charset=UTF-8; boundary=xatt569125687hcu8vfma

--xatt569125687hcu8vfma
Content-Type: text/xml ; charset=UTF-8

...response SOAP...
--xatt569125687hcu8vfma
Content-Type: signature/bdoc-1.0/ts 

...signature XML...
--xatt569125687hcu8vfma--
```