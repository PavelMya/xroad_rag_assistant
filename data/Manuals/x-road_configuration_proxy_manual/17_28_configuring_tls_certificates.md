### 2.8 Configuring TLS Certificates

The installation process creates a self-signed TLS certificate for serving configurations over HTTPS. However, self-signed certificates are not recommended for production use, and should be substituted with certificate issued by a trusted Certificate Authority (CA).

To configure the Configuration Proxy to use a certificate issued by a trusted CA, replace the existing certificate files (`confproxy.crt`) and its associated private key (`confproxy.key`), located in the `/etc/xroad/ssl/` directory.

Reload the nginx service for the certificate change to take effect.

```bash
systemctl reload nginx
```