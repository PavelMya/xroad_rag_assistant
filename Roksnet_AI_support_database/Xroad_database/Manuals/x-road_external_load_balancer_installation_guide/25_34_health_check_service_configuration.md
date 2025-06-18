### 3.4 Health check service configuration
The load balancing support includes a health check service that can be used to ping the Security Server using HTTP to see if
it is healthy and likely to be able to send and receive messages. The service is disabled by default but can be enabled
via configuration options.

| Proxy service configuration option | Default value                      | Description                                                                                                                             |
| ---------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| health-check-interface             | `0.0.0.0` (all network interfaces) | The network interface this service listens to. This should be an address the load balancer component can use to check the server status |
| health-check-port                  | `0` (disabled)                     | The tcp port the service listens to for HTTP requests. The default value `0` disables the service.                                      |

Below is a configuration that can be added to  `/etc/xroad/conf.d/local.ini` on the primary that would enable the health check
service on all the nodes once the configuration has been replicated. Changes to the settings require restarting the
`xroad-proxy` service to take effect. This example enables listening to all available network interfaces (`0.0.0.0`) on
port 5588.

```ini
[proxy]
health-check-interface=0.0.0.0
health-check-port=5588
```

The service can be accessed using plain HTTP. It will return `HTTP 200 OK` if the proxy should be able to process messages
and `HTTP 500 Internal Server Error` otherwise. A short message about the failure reason, if available, is added to the
body of the response. The service runs as a part of the `xroad-proxy` service.

In addition to implicitly verifying that the `xroad-proxy` service is running, the  health checks verify that:
* The server authentication key is accessible and the software token is logged in. This requires a running `xroad-signer` service in good condition.
* The OCSP response for the certificate is `good`. This requires a running `xroad-signer` service in good condition.
* The `serverconf` database is accessible.
* The `global configuration` is valid and not expired.

Each of these status checks has a separate timeout of 5 seconds. If the status check fails to produce a response in this
time, it will be considered a health check failure and will cause a `HTTP 500` response.

In addition, each status check result will be cached for a short while to avoid excess resource usage. A successful status
check result will be cached for 2 seconds before a new verification is triggered. This is to make sure the OK results are
as fresh as possible while avoiding per-request verification. The only exception is checking the software token state
(logged in / out) since the software token status check result is cached for 300 seconds. In contrast, verification failures are 
cached for 30 seconds before a new verification is triggered. This should allow for the Security Server to get up and 
running after a failure or possible reboot before the status is queried again.

Security Server's health check interface can also be manually switched to a maintenance mode in order to inform the load
balancing solution that the Security Server will be undergoing maintenance and should be removed from active use.

When in maintenance mode the health check interface will only respond with `HTTP 503 Service unavailable` and the message
`Health check interface is in maintenance mode` and no actual health check diagnostics will be run. Maintenance mode is disabled
by default and will automatically reset to its default when the proxy service is restarted.

Maintenance mode can be enabled or disabled by sending `HTTP GET`-request from the target Security Server to its proxy admin port `5566`.
The intended new state can be defined using the `targetState` HTTP-parameter:

| Command                  | URI                                                   |
| ------------------------ | ----------------------------------------------------- |
| Enable maintenance mode  | `http://localhost:5566/maintenance?targetState=true`  |
| Disable maintenance mode | `http://localhost:5566/maintenance?targetState=false` |

Proxy admin port will respond with `200 OK` and a message detailing the actualized maintenance mode state change,
e.g. `Maintenance mode set: false => true`. In case the maintenance mode state could not be changed, the returned
message will detail the reason.