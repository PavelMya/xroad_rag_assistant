### 3.2 Protocol for Downloading Configuration

Configuration clients download the generated global configuration files from the central server.

The configuration download protocol is a synchronous protocol that is offered by the central server. It is used by configuration clients such as security servers and configuration proxies.

The protocol is based on HTTP and MIME multipart messaging (see \[[PR-GCONF](#Ref_PR-GCONF)\] for details). The configuration is signed by the central server to protect it against modification. Usually the configuration consists of several parts. The protocol allows configuration clients to check whether the configuration has changed and only download the modified parts.

X-Road security servers (and operational monitoring daemons) maintain a local copy of the global configuration, which they periodically update from their respective configuration source. This cached global configuration has a validity period, which, in general, is longer than the period at which configuration clients are configured to update their local copy. Security servers continue to be fully operational while the cached global configuration remains valid. However, an out-of-date copy of the global configuration severely restricts the management capabilities of security server administrators and forbids security servers from processing incoming requests. As such, a short downtime of the interface is permissible within the limits of the configured configuration validity period.