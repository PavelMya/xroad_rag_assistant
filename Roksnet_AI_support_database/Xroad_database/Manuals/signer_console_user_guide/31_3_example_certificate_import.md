## 3 Example: Certificate Import

The following usage example shows how to initialize a software token and import a certificate to signer.

1.  Initialize the software token
    ```bash
    signer-console init-software-token
    ```
    A PIN is prompted, this will be used to log in to the software token afterwards.

2.  Log in to the software token
    ```bash
    signer-console login-token 0
    ```
    Note, that the identifier of software token is always `0`.

3.  Generate a new key on the software token:
    ```bash
    signer-console generate-key 0
    ```
    Output is key id: 
    `F30D41B745FC072028956A3E9695416247248595`

4.  Create a certificate request:
    ```bash
    signer-console generate-cert-request F30D41B745FC072028956A3E9695416247248595 \"FOO BAR BAZ\" s "C=FOO,O=BAR,CN=BAZ" pem
    ```
    Output:
    `Saved to file F30D41B745FC072028956A3E9695416247248595.csr`

5.  Send the CSR to the Certificate Authority and get the certificate.
6.  Import the new certificate to signer
    ```bash
    signer-console import-certificate  "SAVED" \"FOO BAR BAZ\"
    ```