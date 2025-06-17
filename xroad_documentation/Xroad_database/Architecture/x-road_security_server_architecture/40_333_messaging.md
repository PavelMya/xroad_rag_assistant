#### 3.3.3 Messaging

Xroad-confclient downloads global configuration from a configuration source, namely Central Server or Configuration Proxy, through interface G in \[[Figure 2](#Ref_Security_Server_process_diagram)\]. The protocol used in downloading configuration is specified in \[[PR-GCONF](#Ref_PR-GCONF)\].

Xroad-confclient offers admin interface C for commands and queries. This is used by xroad-proxy-ui-api to fetch diagnostics information.

#### 3.3.4 Input/output ports

Xroad-confclient has single input port for admin commands and queries. The port number is for internal use and specified in the source code only.

#### 3.3.5 Persistent data

Xroad-confclient downloads and persists global configuration on disk.

### 3.4 xroad-proxy