### 3.2 Checking the Status of the Nodes of the Cluster

Access rights: Registration Office, System Administrator, Security Officer

In order to check the status of the nodes in an HA setup, execute the following command on the Central Server node's command line:

```bash
curl --header "Authorization: X-Road-ApiKey token=<api key>" -k https://localhost:4000/api/v1/system/high-availability-cluster/status`
```

**Note:** This endpoint requires authentication which can be provided with a valid API KEY (with at least one of the aforementioned roles) in the `Authorization` header of the request. See [Managing API Keys](#23-managing-api-keys) for instructions regarding setting up an API KEY.