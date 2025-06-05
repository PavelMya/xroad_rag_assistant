### 15.2 OCSP fetch interval

The xroad-signer component has a specific interval how often it downloads new OCSP [RFC-OCSP](#13-references) responses. By default the fetch interval is configured to 1200 seconds. To use something else than the default value a global configuration extension part (see [UC-GCONF](#13-references)) of specific format can be uploaded to Central Server.

```xml
<xro:conf xmlns:xro="http://x-road.eu/xsd/xroad.xsd">
    <ocspFetchInterval>1200</ocspFetchInterval>
</xro:conf>
```

The value is the fetch interval in seconds for new OCSP responses.