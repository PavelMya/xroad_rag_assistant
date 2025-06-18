### 5.3 Security Server TLS configuration

The TLS certificate used by the global configuration endpoint must be signed by a trusted CA (one trusted by the JAVA installation).

If the certificate isn't trusted by the Security Server's JAVA installation by default, it can be manually added to the system truststore by following the steps below:

**Example on Ubuntu 20.04 / 22.04**

Copy the `.crt` file (PEM) into the `/usr/local/share/ca-certificates` folder.

Run `sudo update-ca-certificates`.

**Example on RHEL 7 / 8 / 9**

Copy the `.crt` file (PEM or DER) into the `/etc/pki/ca-trust/source/anchors` folder.

Run `sudo update-ca-trust extract`.

It is possible to disable the verification of the global configuration endpoint’s TLS certificate via system properties. The verification may be disabled in test and development environments. Instead, the verification must always be enabled in production environments. System parameters are specified in the [UG-SYSPAR](#Ref_UG-SYSPAR) section "Configuration Client parameters: [configuration-client]".