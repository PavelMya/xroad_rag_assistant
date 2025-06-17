### 11.1 Changing the Configuration of the Message Log

Configuration parameters are defined in INI files \[[INI](#Ref_INI)\], where each section contains the parameters for a particular Security Server component. The default message log configuration is located in the file

    /etc/xroad/conf.d/addons/message-log.ini

In order to override default values, create or edit the file

    /etc/xroad/conf.d/local.ini

Create the `[message-log]` section (if not present) in the file. Below the start of the section, list the values of the parameters, one per line.

For example, to configure the parameters `archive-path` and `archive-max-filesize`, the following lines must be added to the configuration file:

    [message-log]
    archive-path=/my/archive/path/
    archive-max-filesize=67108864

#### 11.1.1 Common Parameters

1.  `hash-algo-id` – the hash algorithm that is used for hashing in the message log. Possible choices are `SHA-256`, `SHA-384`, `SHA-512`. Defaults to `SHA-512`.