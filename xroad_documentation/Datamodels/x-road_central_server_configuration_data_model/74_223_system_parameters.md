### 2.23 SYSTEM_PARAMETERS

System configuration parameter necessary for proper functioning of Central Server and entire X-Road for that matter. System parameters are stored as key-value pairs. Following is the list of supported system parameters. In an HA setup, the name of the node that initiated a particular insertion, is not significant, except for where stated explicitly.

1. managementServiceProviderClass – Member class part of the identifier pointing to the Security Server client that provides management services. The value can be changed in the user interface.
2. managementServiceProviderCode – Member code part of the identifier pointing to the Security Server client that provides management services. The value can be changed in the user interface.
3. managementServiceProviderSubsystem – Subsystem code part of the identifier pointing to the Security Server client that provides management services. The value can be changed in the user interface.
4. centralServerAddress – the DNS name of this Central Server. The value can be changed in the user interface. In an HA setup, the value is local to each node of the cluster.
5. instanceIdentifier – the instance identifier of this X-Road instance. Must be globally unique. The value is assigned during the initialization of the Central Server in the user interface.
6. authCertRegUrl – URL where Security Servers can send their authentication certificate registration requests. May contain placeholder %{centralServerAddress} which will be replaced with value of the centralServerAddress system parameter.
7. confSignDigestAlgoId  – identifier of the digest algorithm that is used for signing the global configuration. Supported values are 'SHA-512', 'SHA-384' and 'SHA-256'.
8. confHashAlgoUri – URI of the algorithm that is used to hash distributable global configuration files. Supported values are http://www.w3.org/2001/04/xmlenc#sha512 and http://www.w3.org/2001/04/xmlenc#sha256.
9. confSignCertHashAlgoUri – URI of the algorithm that is used to hash global configuration signing certificate. Supported values are http://www.w3.org/2001/04/xmlenc#sha512 and http://www.w3.org/2001/04/xmlenc#sha256.
10. securityServerOwnersGroup – name of the global group where all the members that get ownership of any Security Server are automatically added.
11. confExpireIntervalSeconds – time (in seconds)  during which generated global configuration is considered valid.
12. ocspFreshnessSeconds – time (in seconds) during which Security Servers should consider validity information to be usable. After that time, cached OCSP responses must be discarded. This configuration parameter is distributed to Security Servers as part of global configuration.

Some system parameters can be modified by an X-Road security officer in the user interface. All the system parameters that cannot be changed in the user interface, are assigned default values during the initialization of the Central Server. Later these can only be changed from the database. As these parameters are critical for functioning of entire X-Road instance, these must be modified with extreme care.