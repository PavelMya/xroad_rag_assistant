#### 2.4.12 import-certificate

**Description:** Imports a certificate from the specified file to a key. The certificate is imported to the key pair whose public key matches that of the certificate.

**Arguments:**
* ***file***: the relative or absolute file name of the certificate in PEM or DER format.
* ***member id***: the identifier of the member constructed from the C, O, CN fields of the certificates DN, entered as: `\"  \"`

**Output:** Identifier of the key to which the certificate was imported.

#### 2.4.13 login-token

**Description:** Log in to the specified token.

**Arguments:**
* ***token id***: the identifier of the token. Use *[list-tokens](#241-list-tokens)* to look up token identifiers.

**Output:** (none)

#### 2.4.14 logout-token

**Description:** Log out of the specified token

**Arguments:**
* ***token id***: the identifier of the token. Use *[list-tokens](#241-list-tokens)* to look up token identifiers.

**Output:** (none)

#### 2.4.15 init-software-token

**Description:** Initialize the software token. A PIN is prompted that is used to log in to this token.

**Arguments:** (none)

**Output:** (none)