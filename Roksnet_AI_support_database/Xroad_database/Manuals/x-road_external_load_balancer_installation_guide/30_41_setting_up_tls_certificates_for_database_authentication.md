### 4.1 Setting up TLS certificates for database authentication

This section describes how to create and set up certificate authentication between the secondary and primary database instances.

For further details on the certificate authentication, see the
[PostgreSQL documentation](https://www.postgresql.org/docs/10/auth-methods.html#AUTH-CERT).

1. Generate the Certificate Authority key and a self-signed certificate for the root-of-trust:

   ```bash
   openssl req -new -x509 -days 7300 -nodes -sha256 -out ca.crt -keyout ca.key -subj '/O=cluster/CN=CA'
   ```
   The subject name does not really matter here. Remember to keep the `ca.key` file in a safe place.

   Alternatively, an existing internal CA can be used for managing the certificates. A sub-CA should be created as the database cluster
   root-of-trust and used for issuing the secondary and primary certificates.

2. Generate keys and certificates signed by the CA for each postgresql instance, including the primary. Do not use the CA
   certificate and key as the database certificate and key.

   Generate a key and the Certificate Signing Request for it:
   ```bash
   openssl req -new -nodes -days 7300 -keyout server.key -out server.csr -subj "/O=cluster/CN="
   ```

   **Note:** The `` (the subject common name) will be used for identifying the cluster nodes. For secondary nodes,
   it needs to match the replication user name that is added to the primary database and the username that the secondary node
   database uses to connect to the primary. For example, in a system with one primary and two secondaries, the names of the nodes
   could be `primary`, `replica1` and `replica2`. Other parts of the subject name do not matter and can be named as is
   convenient.

   For more information on adding the replication user name to the primary database, see chapter [4.3 Configuring the primary instance for replication](#43-configuring-the-primary-instance-for-replication).

   Configuring the username on the secondary nodes is detailed in chapter [4.4 Configuring the secondary instance for replication](#44-configuring-the-secondary-instance-for-replication)).

   Sign the CSR with the CA, creating a certificate:

   ```bash
   openssl x509 -req -in server.csr -CAcreateserial -CA ca.crt -CAkey ca.key -days 7300 -out server.crt
   ```
   Repeat the above steps for each node.

3. Copy the certificates and keys to the nodes:

   First, prepare a directory for them:

   ```bash
   sudo mkdir -p -m 0755 /etc/xroad/postgresql
   sudo chmod o+x /etc/xroad
   ```
   Then, copy the certificates (ca.crt, and the instance's server.crt and server.key) to `/etc/xroad/postgresql` on each
   cluster instance.

   Finally, set the owner and access rights for the key and certificates:

   ```bash
   sudo chown postgres /etc/xroad/postgresql/*
   sudo chmod 400 /etc/xroad/postgresql/*
   ```

### 4.2 Creating a separate PostgreSQL instance for the `serverconf` database