### 19.3 Correlation ID HTTP header

The REST API endpoints return an **x-road-ui-correlation-id** HTTP header. This header is also logged in `proxy_ui_api.log`, so it
can be used to find the log messages related to a specific API call.

The correlation ID header is returned for all requests, both successful and failed ones.

For example, these log messages are related to an API call with correlation ID `3d5f193102435242`:
```
2019-08-26 13:16:23,611 [https-jsse-nio-4000-exec-10] correlation-id:[3d5f193102435242] DEBUG o.s.s.w.c.HttpSessionSecurityContextRepository - The HttpSession is currently null, and the HttpSessionSecurityContextRepository is prohibited from creating an HttpSession (because the allowSessionCreation property is false) - SecurityContext thus not stored for next request
2019-08-26 13:16:23,611 [https-jsse-nio-4000-exec-10] correlation-id:[3d5f193102435242] WARN  o.s.w.s.m.m.a.ExceptionHandlerExceptionResolver - Resolved [org.niis.xroad.restapi.exceptions.ConflictException: local group with code koodi6 already added]
2019-08-26 13:16:23,611 [https-jsse-nio-4000-exec-10] correlation-id:[3d5f193102435242] DEBUG o.s.s.w.a.ExceptionTranslationFilter - Chain processed normally
```