### 7.3 Minimum Supported Client Security Server Version

To increase the security of the X-Road ecosystem, it is recommended to limit the minimum version of the client Security Server that is allowed to access a service. Service providers can configure a minimum client Security Server version that's required to consume their services. For details, refer to \[[UG-SEC](#Ref_UG-SEC)\] section 4.1.

## 8 Input Validation

For compliance with the principle of sanitised input, it is security best practice to validate all inputs at the server. X-Road has two validation aspects; a) web UI input validation and b) messaging validation.