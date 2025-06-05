#### WSDL-information modifications

Security server MUST replace endpoint location with value `http://example.org/xroad-endpoint`.
This is done for security reasons, to hide the endpoint addresses which often point
to information systems which should be hidden from the clients, and be accessed only through
the provider security server.

For example service definition

```xml
    <wsdl:service name="testService">
        <wsdl:port binding="tns:testServiceBinding" name="testServicePort">
            <soap:address location="http://some-server.company.com:8080/testService/Endpoint"/>
        </wsdl:port>
    </wsdl:service>
```

becomes

```xml
    <wsdl:service name="testService">
        <wsdl:port binding="tns:testServiceBinding" name="testServicePort">
            <soap:address location="http://example.org/xroad-endpoint"/>
        </wsdl:port>
    </wsdl:service>
```

when retrieved through the meta-service.