#### 3.4.3 Messaging

Xroad-proxy accepts messages from local trusted network through interface C in \[[Figure 2](#Ref_Security_Server_process_diagram)\].

Xroad-proxy accepts messages from untrusted network through interface S. Related to this interface there is another interface O that allows downloading of OCSP responses from Security Server.

Additionally xroad-proxy offers interface P for admin commands and queries. It is used by xroad-proxy-ui-api diagnostics to query timestamping status and can be used to set Security Server in maintenance mode during cluster rolling upgrade.