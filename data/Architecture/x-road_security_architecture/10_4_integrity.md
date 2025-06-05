## 4 Integrity

For compliance with the security principle of integrity, the objective is to ensure that X-Road assets are not modified and do not become corrupted. With assurance of integrity, the threat being mitigated is unauthorised access to and unauthorised actions upon X-Road assets. 

X-Road incorporates a public key infrastructure (PKI) whereby a certification authority (CA) issues authentication certificates to Security Servers and signing certificates to X-Road member organisations. The CA processes certificate signing requests conforming to \[[PKCS10](#Ref_PKCS10)\].

All X-Road messages are signed by the signing key of the organisations that send the messages and all messages are logged. Message logging is enabled by default. This means that both message headers and message bodies are logged. Logging of message bodies may be disabled on Security Server level or for selected subsystems. By default, the logs are stored as plaintext on the Security Server, but encryption can be enabled by the Security Server administrator. It's also possible to install a Security Server with the message log add-on fully disabled.