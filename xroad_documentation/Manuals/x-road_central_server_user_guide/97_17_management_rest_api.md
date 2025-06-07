## 17 Management REST API

Central Server has a REST API that can be used to do all the same server configuration operations that can be done
using the web UI.

Management REST API is protected with an API key based authentication. To execute REST calls, API keys need to be created.

REST API is protected by TLS. Since server uses self-signed certificate, the caller needs to accept this (for example
with `curl` you might use `--insecure` or `-k` option).

Requests sent to REST API have a *limit for maximum size*. If a too large request is sent
to REST API, it will not be processed, and http status 413 Payload too large will be returned.
There is a different limit for binary file uploads, and for other requests.

Limits are
- 10MB for file uploads
- 50KB for other requests

REST API is also *rate limited*. Rate limits apply per each calling IP. If the number of calls
from one IP address exceeds the limit, endpoints return http status 429 Too Many Requests.

Limits are
- 600 requests per minute
- 20 requests per second

If the default limits are too restricting (or too loose), they can be overridden with [admin-service](ug-syspar_x-road_v6_system_parameters.md#413-center-parameters-admin-service) parameters:
- `request-sizelimit-regular`
- `request-sizelimit-binary-upload`
- `rate-limit-requests-per-second`
- `rate-limit-requests-per-minute`

Size limit parameters support formats from Formats from [DataSize](https://docs.spring.io/spring/docs/current/javadoc-api/org/springframework/util/unit/DataSize.html),
for example `5MB`.