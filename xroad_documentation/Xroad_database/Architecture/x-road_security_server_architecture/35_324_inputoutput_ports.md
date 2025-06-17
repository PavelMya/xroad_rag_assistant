#### 3.2.4 Input/output ports

Xroad-signer has two input ports for interfaces B and S. The ports are internal and not documented elsewhere than the source code.

Xroad-signer has output port for accessing OCSP responder. The port number is configured in Central Server and xroad-signer reads it from the global configuration.

#### 3.2.5 Persistent data

Xroad-signer persists the configuration in /etc/xroad/signer/keyconf.xml.

Xroad-signer persists the secret keys in keystore that can be a file in the disk or then it can be stored inside a hardware security module (HSM).

### 3.3 xroad-confclient

#### 3.3.1 Role and responsibilities

Xroad-confclient is responsible for fetching global configuration from a configuration source. Configuration source can be Central Server or Configuration Proxy.

#### 3.3.2 Encapsulated data

Xroad-confclient downloads the global configuration and stores it to local disk. Other processes xroad-proxy, xroad-proxy-ui-api and xroad-signer access the files on the disk directly.