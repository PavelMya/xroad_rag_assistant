## 5 Monitoring HA State on a Node

It is possible to get HA status via a web interface, for example using curl:
```bash
curl --header "Authorization: X-Road-ApiKey token=<api key>" -k https://cs1.example.org:4000/api/v1/system/high-availability-cluster/status
```

See [Central Server User Guide](ug-cs_x-road_6_central_server_user_guide.md#32-checking-the-status-of-the-nodes-of-the-cluster) for more information about the API KEY Authorization

Response:
```json
{
  "ha_configured": true,
  "node_name": "node_0",
  "nodes": [
    {
      "node_name": "node_0",
      "node_address": "cs1.example.org",
      "configuration_generated": "2023-06-06T09:48:02.000Z",
      "status": "OK"
    },
    {
      "node_name": "node_1",
      "node_address": "cs2.example.org",
      "configuration_generated": "2023-06-06T09:46:02.000Z",
      "status": "WARN"
    }
  ],
  "all_nodes_ok": false
}
```
The status information is based on the data in the configuration database and other nodes are not directly accessed.
A node can be:
  * "OK" if the configuration is recently generated.
  * "WARN" if the timestamp is more than a global configuration generation interval in the past.
  * "ERROR" if the timestamp is older than the global configuration expriry time.
  * "UNKNOWN" if the node has not been seen at all.

The combined status "all_nodes_ok" is true if the status of all nodes is "OK" and false otherwise.

For a global view of the cluster status, the check should be executed on each node and compared to verify that nodes have a consistent view of the status.

In addition, one should monitor the database status, and if a replication solution is used, the database replication status using the tools provided by the database and/or replication solution.