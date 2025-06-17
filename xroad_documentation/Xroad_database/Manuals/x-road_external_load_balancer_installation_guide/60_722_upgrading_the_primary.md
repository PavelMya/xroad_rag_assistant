#### 7.2.2 Upgrading the primary

1. Either use the health check maintenance mode or manually disable the primary node from your external load balancer.
   A disabled node on the load balancer should be handled gracefully so that in-flight requests are allowed to finish while
   new requests are routed to other nodes (*connection draining*).

   You can read more about the health check maintenance mode in the chapter about the
   [health check service configuration](#34-health-check-service-configuration).

   In short, to enable the maintenance mode, on the primary node, call the proxy admin port (default port `5566`) with:
   ```bash
   curl http://localhost:5566/maintenance?targetState=true
   ```
   The admin port should respond with:
   ```
   Maintenance mode set: false => true
   ```

2. Check that the primary is no longer processing requests and stop the X-Road services
   (`xroad-proxy`, `xroad-signer`, `xroad-confclient`, `xroad-monitor`, `xroad-proxy-ui-api`) on the primary node. You can read
   more about the services in the Security Server User Guide
   \[[UG-SS](#13-references)\] chapter on [System services](../ug-ss_x-road_6_security_server_user_guide.md#161-system-services).

   To ensure that the node is no longer processing requests, you can monitor `/var/log/xroad/proxy.log` to verify that
   no more requests are arriving or check that there are no connections to the port 5500 with:
   ```bash
   watch -n1 ss -tn state established sport = :5500 or dport = :5500
   ```
3. Upgrade the packages on the primary node to the new software version.

4. Start the X-Road services and wait until the primary node is healthy.

5. a) If the maintenance mode was enabled, the maintenance status from the health check
      port was cleared on startup of the `xroad-proxy` service. The health check should start returning a `200 OK` status
      as soon as Security Server can process messages.

   b) If the primary node was disabled manually from the external load balancer, verify that the primary node is working
      and enable it from the load balancer. To check if a node is healthy, you can use the health check service:
      ```bash
      curl -i http://localhost:
      ```
      See [3.4 Health check service configuration](#34-health-check-service-configuration) for more details.