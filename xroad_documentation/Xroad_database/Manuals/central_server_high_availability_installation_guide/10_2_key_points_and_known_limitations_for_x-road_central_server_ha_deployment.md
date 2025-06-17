## 2 Key Points and Known Limitations for X-Road Central Server HA Deployment

1.  Correct timekeeping is important.

    It is assumed that the clocks of the cluster nodes are synchronized using e.g. NTP. The administrator must configure a time synchronization service (e.g. ntpd, chrony, systemd-timesyncd) and take care to keep the time synced.

2.  Network security and speed.

    Even though all the database connections are secured and authenticated with TLS, network security (especially confidentiality, availability) must be reviewed on infrastructure level. The network speed and reliability between Central Server nodes and the shared database is important for the functionality of the system. A Central Server node can not function if it can not write to and read from the database.

3.  All the nodes must run the same patch-level X-Road software and database software.

4.  Time window for node failure repairing.

    A node can work (i.e. provide valid global configuration to the X-Road instance) as long as it can read from and write to the shared configuration database. If one node loses database access, other nodes continue providing valid global configuration, and Security Servers will switch downloading the configuration from a healthly node. In the case all nodes or the shared database fails, Security Servers can function until global configuration exprires, but new Security Servers can not be added to the X-Road instance.

5.  Configuration files (located in `/etc/xroad/`) are not synchronized between nodes. It is the responsibility of the system administrator to change them in all nodes if required or stated by the user manual.

## 3 Requirements and Workflows for HA Configuration