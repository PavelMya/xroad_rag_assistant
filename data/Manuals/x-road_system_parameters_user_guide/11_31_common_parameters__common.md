### 3.1 Common parameters : `[common]`

| **Parameter**                     | **Default value**                               | **Description**                                                      |
|-----------------------------------|-------------------------------------------------|----------------------------------------------------------------------|
| configuration-path                | /etc/xroad/globalconf/                          | Absolute path to the directory where global configuration is stored. |
| temp-files-path                   | /var/tmp/xroad/                                 | Absolute path to the directory where temporary files are stored.     |
| grpc-internal-host                | 127.0.0.1                                       | Bind gRPC servers to a specific host.                                |
| grpc-internal-tls-enabled         | true                                            | Enables mTLS for gRPC services                                       |
| grpc-internal-keystore            | /var/run/xroad/xroad-grpc-internal-keystore.p12 | gRPC keystore for mTLS configuration.                                |
| grpc-internal-keystore-password   | \<generated-value>                               | gRPC keystore password.                                              |
| grpc-internal-truststore          | /var/run/xroad/xroad-grpc-internal-keystore.p12 | gRPC truststore for mTLS configuration.                              |
| grpc-internal-truststore-password | \<generated-value>                               | gRPC truststore password.                                            |