### 2.3 Requirements for the Configuration Proxy

Minimum recommended hardware parameters:

* the server’s hardware (motherboard, CPU, network interface cards, storage system) must be supported by Ubuntu in general;
* a 64-bit dual-core Intel, AMD or compatible CPU; AES instruction set support is highly recommended;
* 2 GB RAM;
* a 100 Mbps network interface card;
* if necessary, interfaces for the use of hardware tokens.

Requirements to software and settings:

* an installed and configured supported version of Ubuntu x86-64 operating system;
* if the Configuration Proxy is separated from other networks by a firewall and/or NAT, the necessary connections to and from the Security Server must be allowed (reference data: 1.3; 1.4). The enabling of auxiliary services which are necessary for the functioning and management of the operating system (such as DNS, NTP, and SSH) is outside the scope of this guide;
* if the Configuration Proxy has a private IP address, a corresponding NAT record must be created in the firewall (reference data: 1.5).