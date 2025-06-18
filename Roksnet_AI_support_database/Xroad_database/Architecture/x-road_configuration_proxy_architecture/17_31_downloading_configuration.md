### 3.1 Downloading Configuration

Configuration clients download the generated global configuration files from the configuration proxy (protocol used for downloading configuration is described in \[[PR-GCONF](#Ref_PR-GCONF)\]). The configuration proxy uses this interface to download global configuration files from a remote configuration source.

The configuration download interface is a synchronous interface that is provided by the configuration proxy. It is used by configuration clients such as security servers and other configuration proxies.

The interface is described in more detail in \[[ARC-G](#Ref_ARC-G)\].

Should the configuration proxy fail to download the global configuration files from a remote configuration source, no updated configuration directory will be generated for that source's configuration proxy instance. The old configuration directory will remain valid until it's validity period expires.