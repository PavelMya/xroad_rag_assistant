### 4.4 SOAP Request with Attachments

```http
Content-Type: multipart/mixed; charset=UTF-8; boundary=xtop1357783211hcn1yiro
 
--xtop1357783211hcn1yiro 
Content-Type: application/ocsp-response 

...ocsp response...
--xtop1357783211hcn1yiro
Content-Type: text/xml; charset=UTF-8

...request SOAP...
--xtop1357783211hcn1yiro 
Content-Type: multipart/mixed; charset=UTF-8; boundary=xtop569125687h3h10du0 

--xtop569125687h3h10du0
Content-Type: text/plain; charset=UTF-8
Content-Location: attachment.txt
 
...attachment data...
--xtop569125687h3h10du0 
Content-Type: application/octet-stream
Content-Transfer-Encoding: base64
Content-Id: 

...attachment data...
--xtop569125687h3h10du0 --

--xtop1357783211hcn1yiro 
Content-Type: application/hash-chain-result

...hash chain result XML...
--xtop1357783211hcn1yiro 
Content-Type: application/hash-chain

...hash chain XML...
--xtop1357783211hcn1yiro 
Content-Type: signature/bdoc-1.0/ts 

...signature XML...
--xtop1357783211hcn1yiro--
```