### 4.6 REST Request

```http
Content-Type: multipart/mixed; charset=UTF-8; boundary=xtopVuvPTiuLRQanuYKzamfNZBOlxZclEe

--xtopVuvPTiuLRQanuYKzamfNZBOlxZclEe
content-type: application/ocsp-response

...ocsp response...
--xtopVuvPTiuLRQanuYKzamfNZBOlxZclEe
content-type: application/x-road-rest-request

...REST request header...
--xtopVuvPTiuLRQanuYKzamfNZBOlxZclEe
content-type: application/x-road-rest-body

...REST request body...
--xtopVuvPTiuLRQanuYKzamfNZBOlxZclEe
content-type: application/hash-chain-result

...hash chain result XML...
--xtopVuvPTiuLRQanuYKzamfNZBOlxZclEe
content-type: application/hash-chain

...hash chain XML...
--xtopVuvPTiuLRQanuYKzamfNZBOlxZclEe
content-type: signature/bdoc-1.0/ts

...signature XML...
--xtopVuvPTiuLRQanuYKzamfNZBOlxZclEe--
```