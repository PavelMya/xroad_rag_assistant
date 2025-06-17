### 2.6 User Interface Frontend

User Interface allows a user to manage X-Road members and Security Servers and define the global configuration parameters that are distributed to the Security Servers.

User Interface Frontend is a single page web application that makes requests to Administration Service REST API to read and modify configuration.

### 2.7 Password Store

Stores security token passwords in a shared memory segment of the operating system that can be accessed by the Central Server interface and signer. Allows security token logins to persist, until the Central Server is restarted, without compromising the passwords.