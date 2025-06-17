### 1.1 Format of the Audit Log Event

The audit log record contains description of the audit log event in `JSON` format. The field event represents the
description of the event, the field user represents the user name of the performer (events started by the system have
the user name `system`), and the field data represents data fields related with the event:

```json
{
  "event": "...",
  "user": "...",
  "reason": "...",
  "data": {
    "data_field_1": "data_field_1_value", 
    ...
  }
}
```

In case of failure the event description ends with suffix failed and related data set may contain less data fields than
normally. Also, an additional field reason for the error message will be added.

Security Server and Central Server audit log contains some additional elements, described in the next chapter.

Section 2 lists all the possible (successful) event descriptions and corresponding set of data fields (some fields are
optional).