### 2.5 Error Conditions

The *asic* service responds with the HTTP error code and plain text error message if error occurs. The possible error codes are:

1. *400 Bad Request* – the combination of received parameters is invalid or some required parameter is missing.
2. *401 Unauthorized* – the connection was made via HTTPS and the user failed to provide the correct certificate.
3. *404 Not Found* – no signed documents matching the provided parameters were found. Also, the signed document may be not time-stamped yet.
4. *500 Internal Server Error* – an unexpected internal error occurred (e.g., the provided service client identifier does not match any registered client on the security server).