### 2.1 Administration Service

Central Server Administration Service allows management of X-Road members and Security Servers and defines the global configuration parameters that are distributed to the Security Servers. 

User action events that change the system state or configuration are logged into the audit log. The actions are logged regardless of whether the outcome was a success or a failure. The complete list of the audit log events is described in \[[SPEC-AL](#Ref_SPEC-AL)\].

Administration Service is a Spring Boot\[[1](#Ref_1)\] application with embedded Tomcat servlet container.


\[1\] See  for details.