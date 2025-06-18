### 3.4 Configuring Firewall

It is strongly recommended to protect the Security Server from unwanted access using a firewall (hardware or software based). The firewall can be
applied to both incoming and outgoing connections depending on the security requirements of the environment where the Security Server is deployed. 

**Special attention should be paid with the firewall configuration since incorrect configuration may leave the Security Server vulnerable to exploits and attacks.**
This type of abuse could result in compromised access to the Security Server and the data that is exchanged through it.

It is recommended to allow incoming traffic to specific ports only from explicitly defined sources using IP filtering. Access for ports `8080`, `8443` and `4000`
should be especially defined, as these ports are used for making X-Road queries and accessing the user interface.

When installing the Security Server, it is strongly recommended to look over the list of ports at [2.2 Reference Data](#22-reference-data) and define
firewall access rules for specific hosts based on their descriptions.