#### 3.1.4 Input/output ports

Xroad-proxy-ui-api has listening ports for incoming https traffic. The Security Server ports are described in \[[IG-SS](#Ref_IG-SS)\] and \[[IG-SS-RHEL](#Ref_IG-SS-RHEL)\].

Xroad-proxy-ui-api accesses xroad-confclient's admin port to command it to download global configuration. The output port is internal and specified in xroad-confclient's source code.

Xroad-proxy-ui-api accesses xroad-signer's admin and signer protocol ports. Both ports are internal and must be looked up in the xroad-signer's source code.

Xroad-proxy-ui-api accesses postgresql using the port specified in /etc/xroad/db.properties.

Xroad-proxy-ui-api accesses certificate authority's ACME interface R (see \[[ACME](#Ref_ACME)\]) to manage authentication and sign certificates. The output port is defined on the Central Server and distributed to the Security Servers using global configuration.

Xroad-proxy-ui-api accesses mail server interface Q when sending notifications about ACME automatic certificate renewal process. The output port is specified in the /etc/xroad/conf.d/mail.yml configuration file.