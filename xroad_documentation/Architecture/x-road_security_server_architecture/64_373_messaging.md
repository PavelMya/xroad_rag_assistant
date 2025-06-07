#### 3.7.3 Messaging

Xroad-opmonitor communicates with xroad-proxy through operational monitoring query and store interfaces Q and S respectively in \[[Figure 2](#Ref_Security_Server_process_diagram)\]. The protocols are described in \[[PR-OPMON](#Ref_PR-OPMON)\].

Operational monitoring data is also made available via JMX protocol through interface J.

#### 3.7.4 Input/output ports

The input ports for query, store, and JMX access of operational monitoring data are specified in \[[UG-OPMONSYSPAR](#Ref_UG-OPMONSYSPAR)\].

#### 3.7.5 Persistent data

Xroad-opmonitor persists data to postgresql database.

### 3.8 xroad-addon-messagelog

#### 3.7.1 Role and responsibilities

Xroad-addon-messagelog handles message log archiving and cleaning of the message logs from the messagelog database. Instead, message logging and timestamping is handled by the xroad-proxy process.

#### 3.7.2 Encapsulated data

Xroad-addon-messagelog operates on the shared data in the postgresql messagelog database.

#### 3.7.3 Persistent data

Xroad-addon-messagelog persists data on the disk and to postgresql messagelog database.

## 4 Interfaces