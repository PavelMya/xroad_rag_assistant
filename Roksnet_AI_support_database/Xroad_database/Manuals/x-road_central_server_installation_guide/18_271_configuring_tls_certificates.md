#### 2.7.1 Configuring TLS Certificates

The installation process creates a self-signed TLS certificates. However, self-signed certificates are not recommended for production use, and should be substituted with certificate issued by a trusted Certificate Authority (CA).

To configure the Central Server to use a certificate issued by a trusted CA for serving global configurations over HTTPS, replace the existing certificate files (`global-conf.crt`) and its associated private key (`global-conf.key`), located in the `/etc/xroad/ssl/` directory.

Reload the nginx service for the certificate change to take effect.

```bash
systemctl reload nginx
```