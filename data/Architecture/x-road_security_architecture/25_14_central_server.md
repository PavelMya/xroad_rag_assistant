## 14 Central Server

The Central Server manages the database of X-Road members and Security Servers. In addition, the Central Server contains the security policy of the X-Road instance. The security policy consists of the following: 

  * list of trusted certification authorities,
  * list of trusted time-stamping authorities,
  * tuneable parameters such as maximum allowed lifetime of an OCSP response.
   
Both the member database and the security policy are made available to the Security Servers via the HTTP protocol. This distributed set of data forms the global configuration. The integrity of the global configuration is guaranteed using digital signatures - the Central Server signs the global configuration, and the signature is verified by the Security Servers.

The set of information that is needed to access the configuration source and to verify the downloaded global configuration is distributed to the Security Servers using the configuration anchor. The configuration anchor is an XML file, and it is uploaded to the Security Server by the Security Server administrator during the initialization process. The X-Road operator is responsible for providing the configuration anchor to the new member organisations.

For Central Server components, refer to \[[ARC-CS](#Ref_ARC-CS)\] section 2.

For Central Server roles, refer to \[[UG-CS](#Ref_UG-CS)\] section 2.