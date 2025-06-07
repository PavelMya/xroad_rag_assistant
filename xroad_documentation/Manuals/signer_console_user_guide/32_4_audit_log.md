## 4 Audit log

User actions events that are made by the signer-console utility and that change the system state or configuration are logged to the audit log. The actions are logged regardless of whether the outcome was a success or a failure. The complete list of the audit log events is described in \[[SPEC-AL](#Ref_SPEC-AL)\].

An audit log record contains
* the description of the user action,
* the date and time of the event,
* the user name of the user performing the action, and
* the data related to the event.

For example, logging in to the token produces the following log record:
```
2015-09-14T17:41:28+03:00 my-server-host INFO  [X-Road Signer Console] 2015-09-14 17:41:28+0300 - {"event":"Log into the token","user":"xroad","data":{"tokenId":"0"}}
```

The event is present in \[[JSON](#Ref_JSON)\] format, in order to ensure machine processability. The field `event` represents the description of the event, the field `user` represents the user name of the performer, and the field `data` represents data related with the event. The failed action event record contains an additional field `reason` for the error message. 

For example:
```
2015-09-14T17:43:07+03:00 my-server-host INFO  [X-Road Signer Console] 2015-09-14 17:43:07+0300 - {"event":"Log into the token failed","user":"xroad","reason":"Signer.PinIncorrect: PIN incorrect","data":{"tokenId":"0"}}
```

By default, in the X-Road security server and central server, audit log is located in the file
`/var/log/xroad/audit.log`