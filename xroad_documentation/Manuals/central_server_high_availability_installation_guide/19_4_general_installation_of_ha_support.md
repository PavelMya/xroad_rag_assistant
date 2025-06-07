## 4 General Installation of HA Support

The HA support requires that an external database is initialized and available (see [X-Road Central Server Installation Guide](#Ref_IG-CS) about using an external database). 
The database can also be installed on the Central Server node(s), but that is not recommended unless a multi-master setup (e.g. BDR) is used.

In addition, it is necessary to configure a unique node name for each node participating in the cluster preferably before installing the X-Road software.

1.  On each node, edit file `/etc/xroad/conf.d/local.ini`, creating it if necessary
2.  Add the following lines
    ```ini
    [center]
    ha-node-name=
    ```
    Where `` is the unique name for the HA node. It is suggested to follow a naming scheme where the first node is `node_0` and subsequent ones `node_1`, `node_2`, etc..
    
    When upgrading an existing Central Server to HA configuration, the name of the existing server *must be* `node_0`.

    If upgrading an existing cluster with BDR, the name of the node **must be** the same as the local BDR node name.

3.  Install the X-Road Central Server software according to the X-Road Central Server Installation Guide \[[IG-CS](#Ref_IG-CS)\] on the first node.
    
    When the installation asks for a database host, provide the details of the external database.

4. On the subsequent nodes, first copy the database configuration file /etc/xroad/db.properties from the first node. Then install the Central Server according to the X-Road Central Server Installation Guide \[[IG-CS](#Ref_IG-CS)\].