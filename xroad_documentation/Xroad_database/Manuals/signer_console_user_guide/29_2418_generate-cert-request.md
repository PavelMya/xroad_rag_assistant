#### 2.4.18 generate-cert-request

**Description:** Generates a certificate request under the specified key in Signer and saves it to a CSR file in current directory.

**Arguments:**
* ***key id***: the identifier of the key. Use *[list-keys](#242-list-keys)* to look up key identifiers.
* ***member id***: the identifier of the member that matches the subject name, entered as: `\"  \"`
* ***usage***: key usage – either `s` (sign) or `a` (authentication)
* ***subject name***: the subject distinguished name, entered as: `C=,O=,CN=`
* ***format***: the format of the generated certificate request – either `der` or `pem`

**Output:** Name of the file where the certificate request was saved.

#### 2.4.19 update-software-token-pin

**Description:** Updates the software token's PIN code. First, the current PIN is prompted and after that the new PIN is prompted twice. 

**Arguments:** (none)

**Output:** (none)