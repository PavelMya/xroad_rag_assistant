### 3.1 Host header injection mitigation

The host header specifies which website or web application should process an incoming HTTP request. The web server uses the value of this header to dispatch the request to the specified website or web application.

By default, this header allows any value which would be a security risk if Admin UI could be accessed by bad actors. To mitigate this issue it suggested to configure `allowed-hostnames` as described in [UG-SYSPAR](ug-syspar_x-road_v6_system_parameters.md). 
For Security server refer to [proxy-ui-api](ug-syspar_x-road_v6_system_parameters.md#39-management-rest-api-parameters-proxy-ui-api), for Central server refer to [admin-service](ug-syspar_x-road_v6_system_parameters.md#413-center-parameters-admin-service)

## 4. Access control