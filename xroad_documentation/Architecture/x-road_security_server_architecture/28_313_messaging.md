#### 3.1.3 Messaging

Xroad-proxy-ui-api accepts https traffic to interface A in \[[Figure 2](#Ref_Security_Server_process_diagram)\].
Interface A handles both requests to serve content for the UI and requests for REST API calls.
Interface A is directly exposed to outside world.

Xroad-proxy-ui-api accepts http traffic to interface E in \[[Figure 2](#Ref_Security_Server_process_diagram)\].
Interface E handles incoming ACME challenge requests from the Certificate Authority's ACME server (see \[[ACME](#Ref_ACME)\]).
Interface E is directly exposed to outside world.

Xroad-proxy-ui-api communicates with certificate authority's ACME interface R (see \[[ACME](#Ref_ACME)\]).

Xroad-proxy-ui-api communicates with a mail server interface Q when sending notifications about ACME automatic certificate renewal process. The connection can use either STARTTLS or SSL/TLS protocol for added security.

Xroad-proxy-ui-api communicates with Central Server's management services interface M (see \[[PR-MSERV](#Ref_PR-MSERV)\]).

Global configuration is downloaded from Central Server (or Configuration Proxy in some cases) utilizing xroad-confclient and stored on disk.

Xroad-proxy-ui-api communicates with xroad-confclient in three different scenarios:
- When configuration anchor is uploaded to Security Server, it launches fetching of global conf using admin port interface C of xroad-confclient.
- To get the status of global configuration fetching for diagnostics, it accesses xroad-confclient admin port interface C.
- Xroad-proxy-ui-api also reads the global configuration files on disk directly.

Xroad-proxy-ui-api communicates with xroad-signer interface S to manage token, key, and certificate information.
Currently the signer protocol is strictly internal and there is no documentation about it.

Finally Xroad-proxy-ui-api reads/writes data to postgresql interface D.