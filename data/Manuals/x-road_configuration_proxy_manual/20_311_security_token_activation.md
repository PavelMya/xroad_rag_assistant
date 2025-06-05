#### 3.1.1 Security Token Activation

The Configuration Proxy uses a security token for storing the key that is used for signing the distributed configuration. The token can be stored either on hard disk (software token) or in hardware. Before the Configuration Proxy can be used, the security token must be initialized and activated.

Initialization of a software token can be done as follows:

```bash
signer-console init-software-token
```

A PIN is prompted, which will be used to log in to the software token afterwards. Initialization of hardware tokens is vendorspecific and is not in scope of this documentation.

Activation of the security token is done by logging in to the token, using the following command:

```bash
signer-console login-token <TOKEN_ID>
```

where &lt;TOKEN_ID&gt; is the identifier of the security token, which can be found with:

```bash
signer-console list-tokens
```

Note, that the identifier of a software token is always „0”.