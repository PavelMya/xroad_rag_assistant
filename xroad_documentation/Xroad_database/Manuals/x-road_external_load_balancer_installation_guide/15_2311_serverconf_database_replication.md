##### 2.3.1.1 `serverconf` database replication
| Data                | Replication              | Replication method                             |
| ------------------- | ------------------------ | ---------------------------------------------- |
| serverconf database | **replication required** | PostgreSQL streaming replication (Hot standby) |

The serverconf database replication is done using streaming replication with hot standby. Note that PostgreSQL replication
is all-or-nothing: it is not possible to exclude databases from the replication. This is why the replicated serverconf and
non-replicated messagelog databases need to be separated to different instances.