### 2.1 General

Configuration clients download configuration using HTTP protocol (HTTP GET). Configuration source signs the configuration to protect it against modification. The configuration clients receive (via out of band means) configuration anchor containing information needed to successfully download and verify the configuration.

The configuration consists of a signed directory that references individual configuration parts. The signature has expiry date and thus the signed directory must be continuously refreshed by the configuration client. The clients can use the hash values contained in the directory to download the referenced configuration parts only when they are changed.