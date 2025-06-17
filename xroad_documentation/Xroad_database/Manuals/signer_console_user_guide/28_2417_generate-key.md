#### 2.4.17 generate-key

**Description:** Generates a key on the specified token.

**Arguments:**
* ***token id***: the identifier of the token. Use *[list-tokens](#241-list-tokens)* to look up token identifiers.
* ***label***: the label of the key is set for SSCD devices.
* ***algorithm***: the algorithm used by generated key, Possible values: RSA, EC. Prior to version 7.6.0 only RSA is supported.

**Output:** The id of the generated key.