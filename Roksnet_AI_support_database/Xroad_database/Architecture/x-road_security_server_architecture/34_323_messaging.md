#### 3.2.3 Messaging

Xroad-signer fetches information from certificate authority's OCSP responder using interface U.

Xroad-signer offers interface S in \[[Figure 2](#Ref_Security_Server_process_diagram)\] for signing requests. It is used by xroad-proxy-ui-api and xroad-proxy. Additionally xroad-proxy is accessing directly the keyconf.xml encapsulated by xroad-signer.

Xroad-signer offers interface B which is admin interface for commanding xroad-signer. It is used by xroad-proxy-ui-api and xroad-proxy.