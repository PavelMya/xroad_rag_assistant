### A.4 authCertDeletion

Request message

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:id="http://x-road.eu/xsd/identifiers"
        xmlns:xroad="http://x-road.eu/xsd/xroad.xsd">
    <SOAP-ENV:Header>
        <xroad:client id:objectType="MEMBER">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>TS1OWNER</id:memberCode>
        </xroad:client>
        <xroad:service id:objectType="SERVICE">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>TS1OWNER</id:memberCode>
            <id:serviceCode>authCertDeletion</id:serviceCode>
        </xroad:service>
        <xroad:id>2c3094ae-3e19-46f7-b26d-e7ecb35dfc63</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:authCertDeletion>
            <xroad:server id:objectType="SERVER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>GOV</id:memberClass>
                <id:memberCode>TS1OWNER</id:memberCode>
                <id:serverCode>TS1</id:serverCode>
            </xroad:server>
            <xroad:authCert>
                MIIDtzCCAp+gAwIBAgIIaAPFaI/REfAwDQYJKoZIhvcNAQEFBQAwNzERMA8GA1UE
                AwwIQWRtaW5DQTExFTATBgNVBAoMDEVKQkNBIFNhbXBsZTELMAkGA1UEBhMCU0Uw
                HhcNMTUxMDA1MTEyNzQzWhcNMTcxMDA0MTEyNzQzWjAuMQswCQYDVQQGEwJFRTEM
                MAoGA1UECgwDR09WMREwDwYDVQQDDAhUUzFPV05FUjCCASIwDQYJKoZIhvcNAQEB
                BQADggEPADCCAQoCggEBAIkX6/b/yUNSIvZatpFDqUDJ4l+igH+z8/kyLlu92VL6
                H7hkCL6ggn7qsHOTGaxOupXQBKx/EDMOt+cpbhQlQCSoU2LmXYklv9FEGXTUBt5U
                VlT1mZXQkfPVT2ozWQeGEOe7RLApaldgfFgg6AklsuOTe0FgJTfqXrnjVy84MRht
                56nw0V6SnujGMVxQJR1IJC13I5wRbVbkyOxX52vqJ7Kh/2GWtNj2AgY9VbZA6/8E
                S3fMVHWQUbVtFV/2LyjQ0OrwPm0VXsrqRnlh0tln3AtgNOiPgmg72aWNPwlPx7+r
                E02t+0O+KieC3IZppY2044tC699ui5/nOZPrlIqC1XcCAwEAAaOBzzCBzDBNBggr
                BgEFBQcBAQRBMD8wPQYIKwYBBQUHMAGGMWh0dHA6Ly9sb2NhbGhvc3Q6ODA4MC9l
                amJjYS9wdWJsaWN3ZWIvc3RhdHVzL29jc3AwHQYDVR0OBBYEFCB7AE2wTs7iLMMx
                GtilpSg8bShnMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgwFoAUdy2JLgO2/fjSZTkx
                NSLQRhro0gkwDgYDVR0PAQH/BAQDAgO4MB0GA1UdJQQWMBQGCCsGAQUFBwMBBggr
                BgEFBQcDAjANBgkqhkiG9w0BAQUFAAOCAQEATCbKukYbOV5R4I/ivhEXIJAA8aze
                JNONWg0+74v9hdInDSDuXreJkkpJNz0pZaaDnbsWFF+LGcB8UDTc6jOGOaH1b2iS
                hqzq/jL+Le9iSi8V26aWmKJipt5fsU5E/OJAA0KMnNjhtq5FDdP7gCD7+pPVq2Fw
                EWf9nsNtAq8uETc5f9PNGxE6PrDl2Gy2K3m4T/0kvQIiMFsk1z054/9rW/w+dQSS
                sxHhYHOPzwbSEsoeSw3UEqeKdaYUspFs+eGD4b3dexwEe5M0oZAwL/+/56eTcOhn
                enP9A+8jF1vlXnP/m+tThaftcMZa/NTvpceLx36TDUIwB222ddkyN2Offw==
            </xroad:authCert>
        </xroad:authCertDeletion>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

Response message

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
        xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:id="http://x-road.eu/xsd/identifiers"
        xmlns:xroad="http://x-road.eu/xsd/xroad.xsd">
    <SOAP-ENV:Header>
        <xroad:client id:objectType="MEMBER">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>TS1OWNER</id:memberCode>
        </xroad:client>
        <xroad:service id:objectType="SERVICE">
            <id:xRoadInstance>EE</id:xRoadInstance>
            <id:memberClass>GOV</id:memberClass>
            <id:memberCode>TS1OWNER</id:memberCode>
            <id:serviceCode>authCertDeletion</id:serviceCode>
        </xroad:service>
        <xroad:id>2c3094ae-3e19-46f7-b26d-e7ecb35dfc63</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
        <xroad:requestHash
                algorithmId="http://www.w3.org/2001/04/xmlenc#sha512">
            Zvs1uF2GW3zdma1r9K9keOGhNPOjCr3TEZNpxfpRCtsqqy3ljiLorMZ3e5iNZtX6Ek60
            xtV12Gue8Mme1ryZmQ==
        </xroad:requestHash>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:authCertDeletionResponse>
            <xroad:server id:objectType="SERVER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>GOV</id:memberClass>
                <id:memberCode>TS1OWNER</id:memberCode>
                <id:serverCode>TS1</id:serverCode>
            </xroad:server>
            <xroad:authCert>
                MIIDtzCCAp+gAwIBAgIIaAPFaI/REfAwDQYJKoZIhvcNAQEFBQAwNzERMA8GA1UE
                AwwIQWRtaW5DQTExFTATBgNVBAoMDEVKQkNBIFNhbXBsZTELMAkGA1UEBhMCU0Uw
                HhcNMTUxMDA1MTEyNzQzWhcNMTcxMDA0MTEyNzQzWjAuMQswCQYDVQQGEwJFRTEM
                MAoGA1UECgwDR09WMREwDwYDVQQDDAhUUzFPV05FUjCCASIwDQYJKoZIhvcNAQEB
                BQADggEPADCCAQoCggEBAIkX6/b/yUNSIvZatpFDqUDJ4l+igH+z8/kyLlu92VL6
                H7hkCL6ggn7qsHOTGaxOupXQBKx/EDMOt+cpbhQlQCSoU2LmXYklv9FEGXTUBt5U
                VlT1mZXQkfPVT2ozWQeGEOe7RLApaldgfFgg6AklsuOTe0FgJTfqXrnjVy84MRht
                56nw0V6SnujGMVxQJR1IJC13I5wRbVbkyOxX52vqJ7Kh/2GWtNj2AgY9VbZA6/8E
                S3fMVHWQUbVtFV/2LyjQ0OrwPm0VXsrqRnlh0tln3AtgNOiPgmg72aWNPwlPx7+r
                E02t+0O+KieC3IZppY2044tC699ui5/nOZPrlIqC1XcCAwEAAaOBzzCBzDBNBggr
                BgEFBQcBAQRBMD8wPQYIKwYBBQUHMAGGMWh0dHA6Ly9sb2NhbGhvc3Q6ODA4MC9l
                amJjYS9wdWJsaWN3ZWIvc3RhdHVzL29jc3AwHQYDVR0OBBYEFCB7AE2wTs7iLMMx
                GtilpSg8bShnMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgwFoAUdy2JLgO2/fjSZTkx
                NSLQRhro0gkwDgYDVR0PAQH/BAQDAgO4MB0GA1UdJQQWMBQGCCsGAQUFBwMBBggr
                BgEFBQcDAjANBgkqhkiG9w0BAQUFAAOCAQEATCbKukYbOV5R4I/ivhEXIJAA8aze
                JNONWg0+74v9hdInDSDuXreJkkpJNz0pZaaDnbsWFF+LGcB8UDTc6jOGOaH1b2iS
                hqzq/jL+Le9iSi8V26aWmKJipt5fsU5E/OJAA0KMnNjhtq5FDdP7gCD7+pPVq2Fw
                EWf9nsNtAq8uETc5f9PNGxE6PrDl2Gy2K3m4T/0kvQIiMFsk1z054/9rW/w+dQSS
                sxHhYHOPzwbSEsoeSw3UEqeKdaYUspFs+eGD4b3dexwEe5M0oZAwL/+/56eTcOhn
                enP9A+8jF1vlXnP/m+tThaftcMZa/NTvpceLx36TDUIwB222ddkyN2Offw==
            </xroad:authCert>
            <xroad:requestId>392</xroad:requestId>
        </xroad:authCertDeletionResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```