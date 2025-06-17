##### 2.3.1.2 Key configuration and software token replication from `/etc/xroad/signer/*`
| Data                           | Replication    | Replication method       |
| ------------------------------ | -------------- | ------------------------ |
| keyconf and the software token | **replicated** | `rsync+ssh`  (scheduled) |

Previously, any external modification to `/etc/xroad/signer/keyconf.xml` was overwritten by the X-Road signer process if
it was running. Therefore, replicating the signer configuration without service disruptions would have required taking the
cluster members offline one-by-one. The load balancing support adds the possibility for external modifications to the
keyconf.xml to be applied on secondary nodes without service disruptions. The actual state replication is done with a scheduled
rsync over ssh. This might take a few minutes so a slight delay in propagating the changes must be tolerated by the
clustered environment. A small delay should usually cause no problems as new keys and certificates are unlikely to be used
immediately for X-Road messaging. Changes to the configuration are also usually relatively infrequent. These were one of
the [basic assumptions](#211-basic-assumptions-about-the-load-balanced-environment) about the environment. 
Users should make sure this holds true for them.

The secondary nodes use the `keyconf.xml` in read-only mode: no changes made from the admin UI are persisted to disk. secondaries
reload the configuration from disk periodically and apply the changes to their running in-memory configuration.