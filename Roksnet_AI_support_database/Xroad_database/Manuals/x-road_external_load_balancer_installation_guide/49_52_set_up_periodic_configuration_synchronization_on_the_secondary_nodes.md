### 5.2 Set up periodic configuration synchronization on the secondary nodes

The following configuration, which will be set up on the secondary nodes will synchronize the configuration in `/etc/xroad`
periodically (once per minute) and before the services are started. That means that during boot, if the primary server is
available, the configuration will be synchronized before the `xroad-proxy` service is started. If the primary node is down,
there will be a small delay before the services are started.

Note that only modifications to the signer keyconf will be applied when the system is running. Changes to any other
configuration files,  like `local.ini`, require restarting the services, which is not automatic.