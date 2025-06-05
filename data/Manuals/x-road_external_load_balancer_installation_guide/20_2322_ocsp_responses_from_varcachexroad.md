##### 2.3.2.2 OCSP responses from `/var/cache/xroad/`

The OCSP responses are currently not replicated. Replicating them could make the cluster more fault tolerant but the
replication cannot simultaneously create a single point of failure. A distributed cache could be used for the responses.