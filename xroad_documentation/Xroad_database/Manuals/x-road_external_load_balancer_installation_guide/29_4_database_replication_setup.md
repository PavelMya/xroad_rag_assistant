## 4. Database replication setup

For technical details on the PostgreSQL replication, refer to the [official documentation](https://www.postgresql.org/docs/current/high-availability.html).
Note that the versions of PostgreSQL distributed with RHEL and Ubuntu are different. At the time of writing, RHEL 7
distributes PostgreSQL version 9.2 and 12, and RHEL 8 version 10 and 12; the replication configuration is the same
for versions 9.2 and 10. RHEL 9, Ubuntu 20.04, 22.04 and 24.04 using PostgreSQL version 12 and later the configuration has some differences.