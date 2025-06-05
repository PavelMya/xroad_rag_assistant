#### 11.1.2 Logging Parameters

1.  `message-body-logging` - if set to true, the messages are logged in their original form. If false, the message body is emptied of its contents.

2.  `enabled-body-logging-local-producer-subsystems` - when message-body-logging is set to false, this field contains the overrides for the local producer subsystems.

3.  `enabled-body-logging-remote-producer-subsystems` - when message-body-logging is set to false, this field contains the overrides for the remote producer subsystems.

4.  `disabled-body-logging-local-producer-subsystems` - when message-body-logging is set to true, this field contains the overrides for the local producer subsystems.

5.  `disabled-body-logging-remote-producer-subsystems` - when message-body-logging is set to true, this field contains the overrides for the remote producer subsystems.

6.  `max-loggable-message-body-size` - the maximum REST message body size that will be written to the messagelog.

7.  `truncated-body-allowed` - if the REST message body size exceeds the max-loggable-message-body-size truncate the body (true) or reject the message (false)

8.  `messagelog-encryption-enabled` - if set to true, the message bodies are written to the database in an encrypted format

9.  `messagelog-keystore` - path to the messagelog keystore

10.  `messagelog-keystore-password` - messagelog keystore password

11.  `messagelog-key-id` - messagelog keystore key id