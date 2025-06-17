### C.4 Remote Database Cluster

When aiming for production it's recommended to use redundant front-end nodes (clustered Central Server) and a remote database cluster. This way there's no single point of failure and the system can recover from both front-end node and database failures.

![Central Server with remote database cluster](img/ig-cs_remote_db_cluster.svg)