#### Example 5 (Tracking the source of error)

When an error occurs it is important to be able to track the component that is causing the error. One of the most
confusing error responses can be HTTP 500 Internal Error.

HTTP 500 can come from the service provider or from the Security Servers.

**A)** If the response does not contain the `X-Road-Error` header, the source of the error is the provider information
system.

**B)** If the response contains the `X-Road-Error` header the source of the error is X-Road and the more specific
component can be deduced from the `type` field in the response body. For example `Server.ServerProxy.ServiceFailed`
means that the provider Security Server did not get answer from the provider service. `Server.ServerProxy.DatabaseError`
means that provider Security Server encountered internal error. `Server.ClientProxy.OutdatedGlobalConf` points to
consumer Security Server's problem.