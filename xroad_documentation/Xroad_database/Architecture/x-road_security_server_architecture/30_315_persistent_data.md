#### 3.1.5 Persistent data

Xroad-proxy-ui-api reads and writes some data from filesystem. This includes configuration anchor, configuration backups, and internal TLS certificate.

Xroad-proxy-ui-api reads and modifies Security Server configuration using postgresql database serverconf. 
The database model is specified in \[[DM-SS](#Ref_DM-SS)\].

Xroad-proxy-ui-api reads global configuration from filesystem.

Data related to token keys, certificates and CSRs is accessed through xroad-signer.

### 3.2 xroad-signer

#### 3.2.1 Role and responsibilities

Xroad-signer is responsible for managing tokens, keys and certificates.

#### 3.2.2 Encapsulated data

Xroad-signer encapsulates keystore, where the Security Server's secret keys are stored.

Xroad-signer encapsulates keyconf, which tracks the configuration related to tokens, keys and certificates.