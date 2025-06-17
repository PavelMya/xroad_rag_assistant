#### 3.4.1 Role and responsibilities

Xroad-proxy is the most significant process on the Security Server. It is responsible for transmitting messages.

Also, xroad-proxy process handles message logging and timestamping. Instead, message log archiving and cleaning of the message logs is handled by the xroad-addon-messagelog process.

#### 3.4.2 Encapsulated data

Xroad-proxy configuration is stored in postgresql database.