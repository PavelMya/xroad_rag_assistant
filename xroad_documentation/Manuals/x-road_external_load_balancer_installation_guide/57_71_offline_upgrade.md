### 7.1 Offline upgrade
If the X-Road Security Server cluster can be shut down for an offline upgrade, the procedure remains fairly simple:
1. Stop the X-Road services (`xroad-proxy`, `xroad-signer`, `xroad-confclient`, `xroad-proxy-ui-api` and `xroad-monitor`) on all
   the nodes. You can read more about the services in the Security Server User Guide
\[[UG-SS](#13-references)\] chapter on [System services](../ug-ss_x-road_6_security_server_user_guide.md#161-system-services).
2. Upgrade the packages on the primary node to the new software version.
3. Let any database and configuration changes propagate to the cluster members.
4. Upgrade the packages on the secondary nodes.
5. Start the X-Road services.