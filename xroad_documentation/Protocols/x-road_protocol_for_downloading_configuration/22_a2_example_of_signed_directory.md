### A.2 Example of Signed Directory

This example directory contains two parts. The first part contains private parameters and the second part contains shared parameters.

```http
Content-Type: multipart/related; charset=UTF-8; boundary=envelopeboundary

--envelopeboundary
Content-Type: multipart/mixed; charset=UTF-8; boundary=innerboundary

--innerboundary
Expire-date: 2014-05-20T17:42:55Z

--innerboundary
Content-type: application/octet-stream
Content-transfer-encoding: base64
Content-identifier: PRIVATE-PARAMETERS; instance="EE"
Content-location: /private-parameters.xml
Hash-algorithm-id: http://www.w3.org/2001/04/xmlenc#sha512

qgD1gNt3i/eDMCy0s6lTig6TD5h4=
--innerboundary
Content-type: application/octet-stream
Content-transfer-encoding: base64
Content-identifier: SHARED-PARAMETERS; instance="EE"
Content-location: /shared-parameters.xml
Hash-algorithm-id: http://www.w3.org/2001/04/xmlenc#sha512

qgD1gNt3i/eDMCy0s6lTig6TD5h4=
--innerboundary--
--envelopeboundary
Content-type: application/octet-stream
Content-transfer-encoding: base64
Signature-algorithm-id: http://www.w3.org/2001/04/xmldsig-more#rsa-sha512
Verification-certificate-hash: trng71M3bScT0fkc1TBWUaG+D28zTo;
    hash-algorithm-id="http://www.w3.org/2001/04/xmlenc#sha512"

D1XfU3UXTFxS8s8iVW9+ePJhcuYTgpN4+Ze4oZgjbt...=
--envelopeboundary--
```

## Annex B. shared-parameters.xsd