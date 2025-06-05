### 4.2 Simple SOAP Request

```http
Content-Type: multipart/mixed; charset=UTF-8; boundary=xtop1357783211hcn1yiro 

--xtop1357783211hcn1yiro 
Content-Type: application/ocsp-response 

...ocsp response...
--xtop1357783211hcn1yiro 
Content-Type: text/xml ; charset=UTF-8

...request SOAP...
--xtop1357783211hcn1yiro 
Content-Type: signature/bdoc-1.0/ts 

...signature XML...
--xtop1357783211hcn1yiro--
```