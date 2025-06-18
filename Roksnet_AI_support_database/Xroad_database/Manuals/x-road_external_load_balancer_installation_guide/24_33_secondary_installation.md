### 3.3 Secondary installation
1. Install Security Server packages using the normal installation procedure. Alternatively you can also install only the packages
   required for secondary nodes. `xroad-proxy-ui-api` package can be omitted, but the admin graphical user interface
   (which is provided by this package) can be handy for diagnostics. It should be noted that changing a secondary's
   configuration via the admin gui is not possible (except entering token PIN).
2. Stop the `xroad` services.
3. Create a separate PostgreSQL instance for the serverconf database (see section
   [4. Database replication setup](#4-database-replication-setup) for details)
4. Change `/etc/xroad/db.properties` to point to the separate database instance and change password to match the one
   defined in the primary database (the password is part of the data that is replicated to the secondaries).
    * `serverconf.hibernate.connection.url` : Change the url port number from `5432` to `5433` (or the port you specified)
    * `serverconf.hibernate.connection.password`: Change to match the primary db's password (in plaintext).
5. Set up SSH between the primary and the secondary (the secondary must be able to access `/etc/xroad` via ssh)
   * Create an SSH keypair for `xroad` user and copy the public key to authorized keys of the primary node
   (`/home/xroad-slave/.ssh/authorized_keys`)
   > On RHEL 8, 9: generate a new key which is compliant with FIPS-140-2, for example ECDSA with curve nistp256
      ```bash
      sudo -u xroad ssh-keygen -t ecdsa
      ```
6. Set up state synchronization using rsync+ssh. See section
   [5. Configuring data replication with rsync over SSH](#5-configuring-data-replication-with-rsync-over-ssh)
   * Make the initial synchronization between the primary and the secondary.
   ```bash
   sudo -u xroad rsync -e ssh -avz --delete --exclude db.properties --exclude "/postgresql" --exclude "/conf.d/node.ini" --exclude "/gpghome" xroad-slave@:/etc/xroad/ /etc/xroad/
   ```
   Where `` is the primary server's DNS or IP address.
7. Configure the node type as `slave` in `/etc/xroad/conf.d/node.ini`.

      ```bash
      [node]
      type=slave
      ```
      Change the owner and group of the file to `xroad:xroad` if it is not already.
8. Start the X-Road services.
9. If you wish to use the secondary Security Server's admin user interface, you need to implement additional user group restrictions. As noted in step 1, changes to the secondary node Security Server configuration must not be made through its admin user interface, as any such changes would be overwritten by the replication. To disable UI editing privileges for all users, remove the following user groups from the secondary Security Server:

   * `xroad-registration-officer`
   * `xroad-service-administrator`
   * `xroad-system-administrator`
   
   Note: `xroad-security-officer` should remain, otherwise you will not be able to enter token PIN codes.

   After removing these groups, the super user created during the Security Server installation is a member of two UI privilege groups: `xroad-securityserver-observer` and `xroad-security-officer`. These groups allow read-only access to the admin user interface and provide a safe way to use the UI for checking the configuration status of the secondary Security Server. In addition, the groups allow the user to enter the token PIN code. Since admin UI users are UNIX users that are members of specific privilege groups, more users can be added to the groups as necessary. Security Server installation scripts detect the node type of existing installations and modify user group creation accordingly. Instead, version upgrades do not overwrite or modify this configuration during Security Server updates.

   For more information on user groups and their effect on admin user interface privileges in the Security Server, see the  Security Server User Guide \[[UG-SS](#13-references)\].

   Also, the secondary Security Server's management REST API can be used to read the secondary's configuration. However, modifying the secondary's configuration using the management REST API is blocked. API keys are replicated from the primary to the secondaries, and the keys that are associated with the `xroad-securityserver-observer` role have read-only access to the secondary. In addition, the keys that are associated with the `xroad-securityserver-observer` and `xroad-security-officer` roles, are able to enter token PIN codes. The keys that are not associated with the `xroad-securityserver-observer` role, don't have any access to the secondary. See next item for more details.

   For more information on the management REST API, see the  Security Server User Guide \[[UG-SS](#13-references)\].

10. Note about API keys and caching.
    If API keys have been created for primary node, those keys are replicated to secondaries, like everything else from `serverconf` database is.
    The keys that are associated with the `xroad-securityserver-observer` role have read-only access to the secondary.
    Instead, the keys that are not associated with the `xroad-securityserver-observer` role, don't have any access to the secondary and API calls will fail.
    To avoid this, secondary REST API should only be accessed using keys associated with the `xroad-securityserver-observer` role, and only for operations that read configuration, not updates. 
   
    Furthermore, API keys are accessed through a cache that assumes that all updates to keys (e.g. revoking keys, or changing permissions) are done using the same node.
    If API keys are changed on primary, the changes are not reflected on the secondary caches until the next time `xroad-proxy-ui-api` process is restarted.
    To address this issue, you should restart secondary nodes' `xroad-proxy-ui-api` processes after API keys are modified (and database has been replicated to secondaries), to ensure correct operation.
   
    Improvements to API key handling in clustered setups will be included in later releases.

11. It is possible to use the autologin-package with secondary nodes to enable automatic PIN-code insertion, however the autologin-package default implementation stores PIN-codes in plain text and should not be used in production environments. Instructions on how to configure the autologin-package to use a more secure custom PIN-code storing implementation can be found in [autologin documentation](../Utils/ug-autologin_x-road_v6_autologin_user_guide.md)

The configuration is now complete. If you do not want to set up the health check service, continue to [chapter 6](#6-verifying-the-setup)
 to verify the setup.