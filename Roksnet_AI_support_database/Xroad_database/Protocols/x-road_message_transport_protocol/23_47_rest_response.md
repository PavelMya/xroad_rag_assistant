### 4.7 REST Response

```http
Content-Type: multipart/mixed; charset=UTF-8; boundary=xtoptrgBinKkBvoijBRQYWabkZvkECcuIH

--xtoptrgBinKkBvoijBRQYWabkZvkECcuIH
content-type: application/x-road-rest-response

...REST response header...
--xtoptrgBinKkBvoijBRQYWabkZvkECcuIH
content-type: application/x-road-rest-body

...REST response body...
--xtoptrgBinKkBvoijBRQYWabkZvkECcuIH
content-type: application/hash-chain-result

...hash chain result XML...
--xtoptrgBinKkBvoijBRQYWabkZvkECcuIH
content-type: application/hash-chain

...hash chain XML...
--xtoptrgBinKkBvoijBRQYWabkZvkECcuIH
content-type: signature/bdoc-1.0/ts

...signature XML...
--xtoptrgBinKkBvoijBRQYWabkZvkECcuIH--
```