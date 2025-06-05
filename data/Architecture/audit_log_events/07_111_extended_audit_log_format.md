#### 1.1.1 Extended Audit Log Format

Security Server and Central Server use REST APIs to update data, and a new audit log implementation adds some features that are useful in
auditing updates done through the API.

Example of extended audit log message for the security server:
```bash
2023-05-25T13:26:32+03:00 dev-ss1.i.x-road.rocks correlation-id: [a81deb2bf312a60f] INFO  [X-Road Proxy Admin REST API] 
2023-05-25T13:26:32.409+03:00 - {
  "event":"Refresh service description",
  "user":"xrd",
  "ipaddress":"192.0.2.1",
  "auth":"Session",
  "url":"/api/v1/service-descriptions/7/refresh",
  "data":{
    "clientIdentifier":{
      "memberClass":"ORG",
      "memberCode":"111",
      "subsystemCode":"MANAGEMENT",
      "fieldsForStringFormat":["ORG","111","MANAGEMENT"],
      "objectType":"SUBSYSTEM",
      "xroadInstance":"DEV"},
   "url":"http://dev-cs.i.x-road.rocks/managementservices.wsdl",
   "serviceType":"WSDL",
   "wsdl":{
     "servicesAdded":[],
     "servicesDeleted":[]
    }
  }
}
```

Log contains (outside the actual audit log event `JSON`) `correlation-id` element which can be used to associate
audit log entry with a specific request, regular log entries and e.g. stack traces from regular log.

Audit log event `JSON` contains these additional elements:

* ipaddress
  * the IP address of the user
* auth
  * authentication type used for this API call
    * possible values:
      * Session - session based authentication (web application)
      * ApiKey - direct API call using API key authentication
      * HttpBasicPam - HTTP basic authentication with PAM login (for api key management API operations)
* url
  * url of called API endpoint
* warning
  * for failed events, boolean indicating whether the failure was caused by unhandled warnings

```json
{
  "event": "...",
  "user": "...",
  "ipaddress":"...",
  "reason": "...",
  "warning": true,
  "auth": "Session",
  "url": "/api/service-descriptions/249",
  "data": {
    "data_field_1": "data_field_1_value", 
    ...
  }
```