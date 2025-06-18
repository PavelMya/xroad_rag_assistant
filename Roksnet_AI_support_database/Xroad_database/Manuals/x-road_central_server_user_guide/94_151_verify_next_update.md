### 15.1 Verify next update

For additional robustness the OCSP [RFC-OCSP](#13-references) response verifier can be configured to skip checking of nextUpdate parameter. By default the checking is turned on and to turn it off the user has to take action.

Configuration is done by updating a specific optional configuration file (see [UC-GCONF](#13-references)) nextupdate-params.xml. This configuration file is distributed to all Security Servers through the global configuration distribution process (see [UC-GCONF](#13-references)).

```xml

  true

```

With verifyNextUpdate element value “false” the nextUpdate parameter checking is switched off.