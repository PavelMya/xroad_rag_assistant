## 24 Configuring ACME

Automated Certificate Management Environment \[[ACME](#Ref_ACME)\] protocol enables automated certificate management of the authentication and sign certificates on the Security Server. The Security Server supports automating the certificate request process, but the process has to be initiated manually when applying for a certificate for the first time. Also, activating the received certificates is a manual task.

The ACME protocol can be used only if the Certificate Authority (CA) issuing the certificates supports it and the X-Road operator has enabled the use of the protocol on the Central Server. Therefore, also the communication between the CA's ACME server and the Security Server is disabled by default. In addition, some member-specific configuration is required on the Security Server.

**Automatic certificate renewal**

Authentication and sign certificates issued by a CA that supports ACME can be automatically renewed. Automatic renewal is enabled by default, but the Security Server administrator can turn it off.

The Security Server runs an automatic renewal job periodically and tries to renew certificates ready for renewal. If the server supports the ACME ARI extension (\[[ACME-ARI](#Ref_ACME-ARI)\]), the time when a certificate is ready for renewal is determined by the ACME server. Otherwise, the time is defined by the `proxy-ui-api.acme-renewal-time-before-expiration-date` system property. The default value of the property is 14 days, which means that the Security Server starts trying to renew a certificate 14 days before it expires. The renewal job configuration can be managed by the `proxy-ui-api.acme-renewal-*` configuration properties.

The renewal status of ACME supported certificates can be seen on the Keys and certificates page:
* **"N/A"** - certificate is not `REGISTERED` or not issued by ACME supported CA and therefore, it is ignored by the automatic certificate renewal job.
* **"Renewal in progress"** - Renewal has started, but is not yet finished. Once the new certificate is registered and enabled, this certificate can be removed.
* **"Renewal error:"** followed by an error message - indicates that the last renewal attempt has failed, also showing the reason for the failure.
* **"Next planned renewal on"** followed by a date - indicates when the next renewal should happen. Note that this date might change in the future when the information is received from the ACME Server.

**Automatic certificate activation**

It is also possible to let the Security Server automatically activate new certificate once it is ordered for signing certificates or once it is registered for authentication certificates. This behaviour can be controlled by respective [system paramaters](ug-syspar_x-road_v6_system_parameters.md#39-management-rest-api-parameters-proxy-ui-api).

**E-mail notifications**

The Security Server supports sending email notifications on ACME-related events. Notifications are sent in case of authentication and sign certificate renewal success and failure, authentication certificate registration success and signing and authentication certificate automatic activation success or failure. The notifications can be turned on and off separately with [system paramaters](ug-syspar_x-road_v6_system_parameters.md#39-management-rest-api-parameters-proxy-ui-api).

The member's e-mail address defined in the `mail.yml` configuration file is used as the recipient. The same email address is also used as a member-specific contact information when a certificate is ordered from the ACME Server.

For the e-mail notifications to work, an external mail server needs to be configured beforehand in the `/etc/xroad/conf.d/mail.yml` configuration file. The configuration include:

* **host** - host name used to connect to the mail server.
* **port** - port number used to connect to the mail server.
* **username** - used for authentication to the mail server.
* **password** - used for authentication to the mail server.
* **use-ssl-tls** - if "true", then full `ssl/tls` protocol is used for connection. If "false" or missing, then `starttls` protocol is used instead.

The **host**, **port**, **username** and **password** properties are mandatory. The mail server configuration status can be viewed in the Diagnostics page. If the Diagnostics page shows that the configuration is incomplete, it means that at least one of required configuration properties is missing. Instead, if all the required configuration are in-place, a test email can be sent from the Diagnostics page.

**Enable connections from the ACME server**

The Security Server has a `[proxy-ui-api]` parameter [acme-challenge-port-enabled](ug-syspar_x-road_v6_system_parameters.md#39-management-rest-api-parameters-proxy-ui-api) that defines whether the Security Server listens to incoming ACME challenge requests on port 80. The default value for this parameter is `false` which means that  the Security Server does not listen on port 80. The parameter can be changed by following the [System Parameters guide](ug-syspar_x-road_v6_system_parameters.md#21-changing-the-system-parameter-values-in-configuration-files).
This parameter can be overriden by an environment variable `XROAD_PROXY_UI_API_ACME_CHALLENGE_PORT_ENABLED` which takes precedence when both are set.

**Member-specific configuration**

Although the main ACME-related configuration is managed on the Central Server and distributed to the Security Servers over the Global Configuration, in order to use the ACME standard, some of the member-specific configurations have to be set on the Security Server side as well. These configurations go in the file `acme.yml`, that is in the configurations folder on the file system (default `/etc/xroad/conf.d`). An example file is added by the installer when installing or upgrading X-Road to version 7.5. The configurations to be added are:

1. Credentials (kid and hmac secret) for external account binding. Some CAs require these for added security. They tie the X-Road member to an external account on the Certificate Authority's side and so need to be acquired externally from the CA.
2. `account-keystore-password` -  a password of the ACME Server account PKCS #12 keystore that is populated automatically by the Security Server, when communicating with the ACME Server.

There are currently two ways to let the ACME server know which type of certificate to return (the chosen CA also needs to support them). The first one, which sends profile ids for authentication and signing certificates in http header, does not require any further configuration on the Security Server side. The second one uses certificate type specific external account credentials. For the authentication certificate add "**auth-**" prefix to the external account binding credentials property names in the `/etc/xroad/conf.d/acme.yml` file. For the signing certificate add the prefix "**sign-**".

Example of the `/etc/xroad/conf.d/acme.yml` file contents (can be found from `/etc/xroad/conf.d/acme.example.yml`):

```yaml

# Example acme.yml file that has properties related to Automatic Certificate Management Environment (ACME)

# that is used to automate acquiring certificates from Certificate Authorities. To use this file

# remove '.example' form the file name and replace with correct values as needed or create a new file named 'acme.yml'.

# ACME external account binding credentials grouped by Certification Authorities(CA-s) and Members,

# where CAs have their name as key and should be surrounded by quotation marks to allow spaces.

# For Members the key is the Member ID in the form :: and

# should also be surrounded by quotation marks to allow for ':'. They have two properties: kid and mac-key, which should be

# acquired externally from the CA. If the CA supports kid-based certificate type selection, then credentials starting

# with the prefix "auth-" can be used to order authentication certificate and credentials starting with "sign-" can

# be used to order signing certificates.