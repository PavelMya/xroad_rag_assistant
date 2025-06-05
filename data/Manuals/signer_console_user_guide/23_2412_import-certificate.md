#### 2.4.12 import-certificate

**Description:** Imports a certificate from the specified file to a key. The certificate is imported to the key pair whose public key matches that of the certificate.

**Arguments:**
* ***file***: the relative or absolute file name of the certificate in PEM or DER format.
* ***member id***: the identifier of the member constructed from the C, O, CN fields of the certificates DN, entered as: `\"<instance> <class> <code>\"`

**Output:** Identifier of the key to which the certificate was imported.