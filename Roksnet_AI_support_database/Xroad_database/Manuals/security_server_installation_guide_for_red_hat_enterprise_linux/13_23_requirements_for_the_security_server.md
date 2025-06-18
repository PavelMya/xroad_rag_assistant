### 2.3 Requirements for the Security Server

Minimum recommended hardware parameters:

* the server’s hardware (motherboard, CPU, network interface cards, storage system) must be supported by RHEL in general;
* a x86-64 dual-core Intel, AMD or compatible CPU; AES instruction set support is highly recommended;
* 2 CPU;
* 4 GB RAM;
* 10 GB free disk space (OS partition), 20-40 GB free disk space (`/var` partition);
* a 100 Mbps network interface card.

Requirements to software and settings:

* an installed and configured RHEL (8.0 or newer; 9.3 or newer) x86-64 operating system;
* Java 21 should be installed;
* if the Security Server is separated from other networks by a firewall and/or NAT, the necessary connections to and from the Security Server are allowed (**reference data: 1.4; 1.5; 1.6; 1.7**). The enabling of auxiliary services which are necessary for the functioning and management of the operating system (such as DNS, NTP, and SSH) stay outside the scope of this guide;
* if the Security Server has a private IP address, a corresponding NAT record must be created in the firewall (**reference data: 1.9**).