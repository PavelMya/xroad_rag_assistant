## 4 Retrieving the WSDL of a Service

Service clients are able to download WSDL-files that contain the definition of a given service by using the `getWsdl` method. The method is invoked as regular X-Road SOAP service (see specification \[[PR-MESS](#Ref_PR-MESS)\] for details on the X-Road SOAP protocol). The connection type settings of the client subsystem is used when the method is invoked. In addition, the following aspects should be noted:

  * WSDL is retrieved as a SOAP-attachment
  * fetching the WSDL obeys the service's "Verify TLS Certificate" setting.

The service SOAP header MUST contain the identifier of the target service provider and the value of the serviceCode element MUST be `getWsdl`.
The body of the request MUST contain an appropriately named XML element (`getWsdl`) which contains one or two child elements (`serviceCode`, `serviceVersion`) that define the service which service description is returned. The `serviceCode` element is mandatory and the `serviceVersion` element is optional.

An example of a `getWsdl` request to the client security server is documented in annex [C.7](#c7-getwsdl-request) and the corresponding response in annexes [C.8](#c8-getwsdl-response) and [C.9](#c9-getwsdl-response-attachment).