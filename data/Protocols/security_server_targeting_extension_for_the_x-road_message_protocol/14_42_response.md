### 4.2 Response
```xml
<SOAP-ENV:Envelope
    xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:id="http://x-road.eu/xsd/identifiers"
    xmlns:m="http://x-road.eu/xsd/monitoring"
    xmlns:xrd="http://x-road.eu/xsd/xroad.xsd">
   <SOAP-ENV:Header>
      <xrd:client id:objectType="MEMBER">
         <id:xRoadInstance>fdev</id:xRoadInstance>
         <id:memberClass>GOV</id:memberClass>
         <id:memberCode>1710128-9</id:memberCode>
      </xrd:client>
      <xrd:service id:objectType="SERVICE">
         <id:xRoadInstance>fdev</id:xRoadInstance>
         <id:memberClass>GOV</id:memberClass>
         <id:memberCode>1710128-9</id:memberCode>
         <id:serviceCode>getSecurityServerMetrics</id:serviceCode>
      </xrd:service>
      <xrd:securityServer id:objectType="SERVER">
         <id:xRoadInstance>fdev</id:xRoadInstance>
         <id:memberClass>GOV</id:memberClass>
         <id:memberCode>1710128-9</id:memberCode>
         <id:serverCode>fdev-ss1.i.x-road.global</id:serverCode>
      </xrd:securityServer>
      <xrd:id>ID11234</xrd:id>
      <xrd:protocolVersion>4.0</xrd:protocolVersion>
      <xrd:requestHash algorithmId="http://www.w3.org/2001/04/xmlenc#sha512">mChpBRMvFlBBSNKeOxAJQBw4r6XdHZFuH8BOzhjsxjjOdaqXXyPXwnDEdq/NkYfEqbLUTi1h/OHEnX9F5YQ5kQ==</xrd:requestHash>
   </SOAP-ENV:Header>
   <SOAP-ENV:Body>
      <m:getSecurityServerMetricsResponse>
         <m:metricSet>
            <m:name>SERVER:fdev/GOV/1710128-9/fdev-ss1.i.x-road.global</m:name>
            <m:stringMetric>
               <m:name>proxyVersion</m:name>
               <m:value>6.7.7-1.20151201075839gitb72b28e</m:value>
            </m:stringMetric>
            <m:metricSet>
               <m:name>systemMetrics</m:name>
               <m:stringMetric>
                  <m:name>OperatingSystem</m:name>
                  <m:value>Linux version 3.13.0-70-generic</m:value>
               </m:stringMetric>
               <m:numericMetric>
                  <m:name>TotalPhysicalMemory</m:name>
                  <m:value>2097684480</m:value>
               </m:numericMetric>
               <m:numericMetric>
                  <m:name>TotalSwapSpace</m:name>
                  <m:value>2097684480</m:value>
               </m:numericMetric>
            </m:metricSet>
            ...
         </m:metricSet>
      </m:getSecurityServerMetricsResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```