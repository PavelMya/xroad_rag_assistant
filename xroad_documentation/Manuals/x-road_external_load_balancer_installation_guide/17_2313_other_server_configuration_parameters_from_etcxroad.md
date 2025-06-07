##### 2.3.1.3 Other server configuration parameters from `/etc/xroad/*`
| Data                                  | Replication    | Replication method       |
| ------------------------------------- | -------------- | ------------------------ |
| other server configuration parameters | **replicated** | `rsync+ssh`  (scheduled) |

The following configurations are excluded from replication:
* `db.properties` (node-specific)
* `postgresql/*` (node-specific keys and certs)
* `globalconf/` (syncing globalconf could conflict with `confclient`)
* `conf.d/node.ini` (specifies node type: primary or secondary)

#### 2.3.2 Non-replicated state