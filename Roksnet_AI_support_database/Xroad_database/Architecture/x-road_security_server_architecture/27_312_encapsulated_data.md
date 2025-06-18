#### 3.1.2 Encapsulated data

Xroad-proxy-ui-api reads and writes some data from filesystem. This includes configuration anchor, configuration backups, and internal TLS certificate.

Xroad-proxy-ui-api reads and modifies Security Server configuration using postgresql database serverconf. 
The database model is specified in \[[DM-SS](#Ref_DM-SS)\].

Xroad-proxy-ui-api reads global configuration from filesystem.

Data related to token keys, certificates and CSRs is accessed through xroad-signer.