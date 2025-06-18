### 3.3 API key considerations in High-Availability setup

API keys are cached in memory, which is typically not a problem in non-clustered Central Server configuration.
However, in case of High-Availability setup, the caches of different nodes can become out of sync.

For instance, revoking an API key from `node 1` may not be recognized by `node 2`, which can still grant access to REST API endpoints with the revoked API key. To address this issue, there are a few potential solutions:

- **Option A:** Consider decreasing [time-to-live](ug-syspar_x-road_v6_system_parameters.md#413-center-parameters-admin-service) value for API key cache from the default of **60 seconds** to a more lenient value. Doing so will reduce the risk of stale values being returned, thus improving security.
- **Option B:** Direct all REST API operations to the same Central Server node.
- **Option C:** Always restart REST API modules when API key operations are executed.
- **Option D:** Disable Api key cache. (See [admin-service parameters](ug-syspar_x-road_v6_system_parameters.md#413-center-parameters-admin-service) for more details). This option will degrade API throughput and should only be used when other options do not work.

## 4. System Settings