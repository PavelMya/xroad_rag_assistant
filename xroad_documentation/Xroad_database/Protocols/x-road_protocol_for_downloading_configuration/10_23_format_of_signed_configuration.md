### 2.3 Format of Signed Configuration

Configuration client can download the configuration by making HTTP GET request to the configuration source. The content type of the response is *multipart/related* [MPREL]. The response is a MIME multipart that MUST consist of two parts:

1. Directory of configuration files. The directory is a nested MIME multipart. The format of this directory is specified in [2.4](#2-4-format-of-directory)
2. Signature of the directory, created using private key of the configuration source. The signature is calculated over the body of the first MIME part.

The signature part MUST have the following MIME headers:

- *Content-type* – the value MUST be “*application/octet-stream*”.
- *Content-transfer-encoding* – the value MUST be “*base64*”.
- *Signature-algorithm-id* – the value MUST identify the signature algorithm used to create the signature. This specification supports algorithm identifiers listed in XML Signature specification [XMLDSIG], Section 6.4.
- *Verification-certificate-hash* – the hash of the certificate that was used to sign this configuration. The value of the header MUST also include parameter *hash-algorithm-id* whose value is the hash algorithm identifier used to calculate the verification certificate hash.

The body of the signature part MUST be the value of the signature calculated using the signature algorithm identified in the *Signature-algorithm-id* header.