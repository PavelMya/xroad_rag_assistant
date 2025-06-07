## 16 Certificates and Keys Management

Only certificates issued by approved certification authorities can be used in X-Road. Approved certification authorities are defined on the Central Server and the configuration is environment specific. It is possible to have multiple approved certification authorities within an X-Road instance. 

Security Server authentication key and certificate are stored on a software token. Central Server and Security Server signing keys and certificates can be stored on a software token or an HSM device.

Security Server authentication and sign certificate management can be partly automated using the \[[ACME](#Ref_ACME)\] protocol. However, the ACME protocol can be used only if the Certificate Authority issuing the certificates supports it and the X-Road operator has enabled the use of the protocol on the Central Server.

The signer component is responsible for managing signing keys and certificates. The signer is called by other components when creating or verifying signatures. The user interface also calls the signer when generating authentication and signing keys or certificate requests.

By default, X-Road utilises 2048 bit RSA keys as authentication and signing keys/certificates. The key length may be configured using the Security Server system parameters. Longer keys may be utilised in X-Road without compatibility issues; 2k, 3k and 4k keys may be simultaneously utilised.

## 17 Monitoring

X-Road monitoring is conceptually split into environmental and operational monitoring.