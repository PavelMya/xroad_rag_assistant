## 5. Publish global configuration over HTTPS

Starting from X-Road version 7.4, it is possible to publish global configuration over HTTPS using a TLS certificate issued by a trusted CA. The CA must be trusted by the Security Server's Java installation. See the Central Server User Guide [UG-CS](#Ref_UG-CS) for details.

### 5.1 Central Server TLS configuration

To configure the Central Server to use a certificate issued by a trusted CA for serving global configurations over HTTPS follow "Central Server Installation Guide" [IG-CS](#Ref_IG-CS) section "Configuring TLS Certificates".

### 5.2 Configuration Proxy TLS configuration

To configure the Configuration Proxy to use a certificate issued by a trusted CA follow "Configuration Proxy Manual" [UG-CP](#Ref_UG-CP) section "Configuring TLS Certificates".