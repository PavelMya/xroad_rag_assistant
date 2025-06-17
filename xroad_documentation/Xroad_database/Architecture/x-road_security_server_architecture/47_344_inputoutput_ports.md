#### 3.4.4 Input/output ports

Xroad-proxy has input ports for message exchange from internal and external network (C and S) and one input port meant for uploading OCSP responses (O). The Security Server ports are described in \[[IG-SS](#Ref_IG-SS)\] and \[[IG-SS-RHEL](#Ref_IG-SS-RHEL)\].

Additionally there is an input port for admin queries and commands (P). The port number is specified in \[[IG-XLB](#Ref_IG-XLB)\].

#### 3.4.5 Persistent data

Xroad-proxy uses postgresql for persistent data storage. The database model is specified in \[[DM-SS](#Ref_DM-SS)\].

### 3.5 postgresql

#### 3.5.1 Role and responsibilities

Postgresql is the primary persistent data storage used by Security Server.

#### 3.5.2 Encapsulated data

Postgresql stores databases, tables, and triggers.

#### 3.5.3 Messaging

Postgresql is used by xroad-proxy-ui-api, xroad-proxy and xroad-opmonitor for persistent data storage.

#### 3.5.4 Input/output ports

Postgresql has single input port for querying and storing data. The Security Server installation uses the default port of PostgreSQL, but it is possible to customize.

#### 3.5.5 Persistent data

Postgresql persists databases, tables, and triggers based on the needs of its clients.

### 3.6 xroad-monitor

#### 3.6.1 Role and responsibilities

Xroad-monitor is responsible for environmental monitoring of Security Server. It gathers statistics about different things like running processes, memory usage, certificate statuses etc. using its sensors.

#### 3.6.2 Encapsulated data

The sensor data is stored in memory of the xroad-monitor process.

#### 3.6.3 Messaging

Xroad-monitor's sensor data is queried by xroad-proxy using interface Q in \[[Figure 2](#Ref_Security_Server_process_diagram)\].

Sensor data is also accessible via JMX protocol through interface J.

#### 3.6.4 Input/output ports

The input port for querying sensor data is internal and can be found from the source code.

The input port for accessing sensor data through JMX protocol is closed by default and must be opened separately by editing /etc/xroad/services/monitor.conf.

#### 3.6.5 Persistent data

Xroad-monitor doesn't persist the sensor data, but rather stores it in the process memory only.

### 3.7 xroad-opmonitor

#### 3.7.1 Role and responsibilities

Xroad-opmonitor is responsible for operational monitoring of Security Server. Operational monitoring means gathering statistics about service calls, successes and failures etc.

#### 3.7.2 Encapsulated data

Xroad-opmonitor stores the operational data in postgresql database. There is also a buffer for this data in xroad-proxy process.