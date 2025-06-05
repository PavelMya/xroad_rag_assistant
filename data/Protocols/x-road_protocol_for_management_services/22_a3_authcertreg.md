### A.3 authCertReg

Request message

```xml
--jetty113950090iemuz6a3
Content-Type: text/xml; charset=UTF-8

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
            <id:serviceCode>authCertReg</id:serviceCode>
        </xroad:service>
        <xroad:id>9a82c2d1-27d6-4053-85a7-f37327c6dba7</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:authCertReg>
            <xroad:server id:objectType="SERVER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>GOV</id:memberClass>
                <id:memberCode>TS1OWNER</id:memberCode>
                <id:serverCode>TS1</id:serverCode>
            </xroad:server>
            <xroad:address>192.168.74.202</xroad:address>
            <xroad:authCert>
                MIIDtzCCAp+gAwIBAgIIaAPFaI/REfAwDQYJKoZIhvcNAQEFBQAwNzERMA8GA1UE
                AwwIQWRtaW5DQTExFTATBgNVBAoMDEVKQkNBIFNhbXBsZTELMAkGA1UEBhMCU0Uw
                HhcNMTUxMDA1MTEyNzQzWhcNMTcxMDA0MTEyNzQzWjAuMQswCQYDVQQGEwJFRTEM
                MAoGA1UECgwDR09WMREwDwYDVQQDDAhUUzFPV05FUjCCASIwDQYJKoZIhvcNAQEB
                BQADggEPADCCAQoCggEBAIkX6/b/yUNSIvZatpFDqUDJ4l+igH+z8/kyLlu92VL6
                H7hkCL6ggn7qsHOTGaxOupXQBKx/EDMOt+cpbhQlQCSoU2LmXYklv9FEGXTUBt5U
                VlT1mZXQkfPVT2ozWQeGEOe7RLApaldgfFgg6AklsuOTe0FgJTfqXrnjVy84MRht
                56nw0V6SnujGMVxQJR1IJC13I5wRbVbkyOxX52vqJ7Kh/2GWtNj2AgY9VbZA6/8S
                3fMVHWQUbVtFV/2LyjQ0OrwPm0VXsrqRnlh0tln3AtgNOiPgmg72aWNPwlPx7+rE
                02t+0O+KieC3IZppY2044tC699ui5/nOZPrlIqC1XcCAwEAAaOBzzCBzDBNBggrB
                gEFBQcBAQRBMD8wPQYIKwYBBQUHMAGGMWh0dHA6Ly9sb2NhbGhvc3Q6ODA4MC9la
                mJjYS9wdWJsaWN3ZWIvc3RhdHVzL29jc3AwHQYDVR0OBBYEFCB7AE2wTs7iLMMxG
                tilpSg8bShnMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgwFoAUdy2JLgO2/fjSZTkxN
                SLQRhro0gkwDgYDVR0PAQH/BAQDAgO4MB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrB
                gEFBQcDAjANBgkqhkiG9w0BAQUFAAOCAQEATCbKukYbOV5R4I/ivhEXIJAA8azeJ
                NONWg0+74v9hdInDSDuXreJkkpJNz0pZaaDnbsWFF+LGcB8UDTc6jOGOaH1b2iSh
                qzq/jL+Le9iSi8V26aWmKJipt5fsU5E/OJAA0KMnNjhtq5FDdP7gCD7+pPVq2FwE
                Wf9nsNtAq8uETc5f9PNGxE6PrDl2Gy2K3m4T/0kvQIiMFsk1z054/9rW/w+dQSSs
                xHhYHOPzwbSEsoeSw3UEqeKdaYUspFs+eGD4b3dexwEe5M0oZAwL/+/56eTcOhne
                nP9A+8jF1vlXnP/m+tThaftcMZa/NTvpceLx36TDUIwB222ddkyN2Offw==
            </xroad:authCert>
        </xroad:authCertReg>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
--jetty113950090iemuz6a3
Content-Type: application/octet-stream
signature-algorithm-id: SHA512withRSA

[AUTHENTICATION CERTIFICATE SIGNATURE BYTES]
--jetty113950090iemuz6a3
Content-Type: application/octet-stream
signature-algorithm-id: SHA512withRSA

[SECURITY SERVER OWNER SIGNATURE BYTES]
--jetty113950090iemuz6a3
Content-Type: application/octet-stream

[AUTHENTICATION CERTIFICATE BYTES]
--jetty113950090iemuz6a3
Content-Type: application/octet-stream

[SECURITY SERVER OWNER CERTIFICATE BYTES]
--jetty113950090iemuz6a3
Content-Type: application/octet-stream

[SECURITY SERVER OWNER CERTIFICATE OCSP RESPONSE BYTES]
--jetty113950090iemuz6a3--
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
            <id:serviceCode>authCertReg</id:serviceCode>
        </xroad:service>
        <xroad:id>9a82c2d1-27d6-4053-85a7-f37327c6dba7</xroad:id>
        <xroad:protocolVersion>4.0</xroad:protocolVersion>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <xroad:authCertRegResponse>
            <xroad:server id:objectType="SERVER">
                <id:xRoadInstance>EE</id:xRoadInstance>
                <id:memberClass>GOV</id:memberClass>
                <id:memberCode>TS1OWNER</id:memberCode>
                <id:serverCode>TS1</id:serverCode>
            </xroad:server>
            <xroad:address>192.168.74.202</xroad:address>
            <xroad:authCert>
                MIIDtzCCAp+gAwIBAgIIaAPFaI/REfAwDQYJKoZIhvcNAQEFBQAwNzERMA8GA1UE
                AwwIQWRtaW5DQTExFTATBgNVBAoMDEVKQkNBIFNhbXBsZTELMAkGA1UEBhMCU0Uw
                HhcNMTUxMDA1MTEyNzQzWhcNMTcxMDA0MTEyNzQzWjAuMQswCQYDVQQGEwJFRTEM
                MAoGA1UECgwDR09WMREwDwYDVQQDDAhUUzFPV05FUjCCASIwDQYJKoZIhvcNAQEB
                BQADggEPADCCAQoCggEBAIkX6/b/yUNSIvZatpFDqUDJ4l+igH+z8/kyLlu92VL6
                H7hkCL6ggn7qsHOTGaxOupXQBKx/EDMOtcpbhQlQCSoU2LmXYklv9FEGXTUBt5UV
                lT1mZXQkfPVT2ozWQeGEOe7RLApaldgfFgg6AklsuOTe0FgJTfqXrnjVy84MRht5
                6nw0V6SnujGMVxQJR1IJC13I5wRbVbkyOxX52vqJ7Kh/2GWtNj2AgY9VbZA6/8ES
                3fMVHWQUbVtFV/2LyjQ0OrwPm0VXsrqRnlh0tln3AtgNOiPgmg72aWNPwlPx7+rE
                02t+0O+KieC3IZppY2044tC699ui5nOZPrlIqC1XcCAwEAAaOBzzCBzDBNBggrBg
                EFBQcBAQRBMD8wPQYIKwYBBQUHMAGGMWh0dHA6Ly9sb2NhbGhvc3Q6ODA4MC9lam
                JjYS9wdWJsaWN3ZWIvc3RhdHVzL29jc3AwHQYDVR0OBBYEFCB7AE2wTs7iLMMxGt
                ilpSg8bShnMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgwFoAUdy2JLgO2/fjSZTkxNS
                LQRhro0gkwDgYDVR0PAQH/BAQDAgO4MB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBg
                EFBQcDAjANBgkqhkiG9w0BAQUFAAOCAQEATCbKukYbOV5R4I/ivhEXIJAA8azeJN
                ONWg0+74v9hdInDSDuXreJkkpJNz0pZaaDnbsWFF+LGcB8UDTc6jOGOaH1b2iShq
                zq/jL+Le9iSi8V26aWmKJipt5fsU5E/OJAA0KMnNjhtq5FDdP7gCD7+pPVq2FwEW
                f9nsNtAq8uETc5f9PNGxE6PrDl2Gy2K3m4T/0kvQIiMFsk1z054/9rW/w+dQSSsx
                HhYHOPzwbSEsoeSw3UEqeKdaYUspFs+eGD4b3dexwEe5M0oZAwL/+/56eTcOhnen
                P9A+8jF1vlXnP/m+tThaftcMZa/NTvpceLx36TDUIwB222ddkyN2Offw==
            </xroad:authCert>
            <xroad:requestId>392</xroad:requestId>
        </xroad:authCertRegResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```