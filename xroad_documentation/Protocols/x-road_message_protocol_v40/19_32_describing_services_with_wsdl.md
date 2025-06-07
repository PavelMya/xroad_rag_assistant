### 3.2 Describing Services with WSDL

Service descriptions are written in the WSDL language, subject to the following restrictions and extensions.

The combination of WSDL binding style/use MUST be document/literal wrapped (binding *style="document"; use="literal"*). The WSDL must conform to the following rules \[[WRAPPED](#Ref_WRAPPED)\]:

> 1. **Only "One" Part Definition in the Input & Output Messages in WSDL**
>    "Wrapped" is a form of document/literal. When defining a WS-I compliant document/literal service, there can be at most one body part in your input message and at most one body part in your output message. You do \*not\* define each method parameter as a separate part in the message definition. (The parameters are defined in the WSDL "types" section, instead).
>
> 2. **"Part" Definitions are wrapper elements**
>    Each part definition must reference an element (not a type, type is used in RPC) defined to make it document style of messaging. This element definition can be imported, or included in the types section of the WSDL document. These element definitions are "wrapper" elements (hence the name of this convention). Define the input and output parameters as element structures within these wrapper elements.
>
> 3. **Child Elements of "Part" Element Type will be SEI Method parameter**
>    An input wrapper element must be defined as a complex type that is a sequence of elements. Each child element-type in that sequence will be generated (while using code generation tool on WSDL) as a parameter of the operation in the service interface.
>
> 4. **Input Wrapper Element name should match with Operation name**
>    The name of the input wrapper element must be the same as the web service operation name in WSDL.
>
> 5. **&lt;Output Wrapper Element Name&gt; = &lt;Operation Name&gt; + "Response"**
>    The name of the output wrapper element could be (but doesn't have to be) the operation name appended with "Response" (e.g., if the operation name is "add", the output wrapper element should be called "addResponse").
>
> 6. **In the WSDL Binding section, soap:binding style = "document"**
>    Since, the style is document/literal for this wrapped pattern, hence in the binding definition, the soap:binding should specify style="document" (although this is the default value, so the attribute may be omitted), and the soap:body definitions must specify use="literal" and nothing else. You must not specify the namespace or encodingStyle attributes in the soap:body definition.

The input and output parameters of the services are described using XML Schema 1.1 \[[XSD1](#Ref_XSD1), [XSD2](#Ref_XSD2)\].

In order to avoid confusion from the client's side in determining whether an empty response indicates a silent error or simply contains no output records, it is a good practice to design the output of a data-returning service in such a way that for any service calls the response contains at least one non-empty scalar parameter. This parameter can be a non-technical error message (technical error messages should be returned with SOAP Fault messages). For error message examples see [Annex D](#annex-d-example-fault-messages).

For a service description WSDL example and messages conforming to this description see [Annex C](#annex-c-example-wsdl) and [Annex E](#annex-e-example-messages), respectively.

The traditional way of describing SOAP attachments in WSDL documents \[[WSDL](#Ref_WSDL)\] is considered to be legacy approach because it cannot bind SOAP envelope with attachments. Instead of that it is recommended to use swaRef types \[[SWAREF](#Ref_SWAREF)\]. It is also possible to describe attachments using MTOM \[[MTOM](#Ref_MTOM)\].

For example of swaRef and MTOM on-the-wire messages with attachments see [Annex F](#annex-f-example-request-with-attachment) and [Annex G](#annex-g-example-request-with-mtom-attachment) respectively. For both swaRef and MTOM service description WSDL examples see [Annex C](#annex-c-example-wsdl).

[Table 2](#Ref_WSDL_elements_for_X_Road_services) lists elements that can be added to a WSDL description to transfer information specific to X-Road. The namespace prefix `xrd` is bound to namespace `http://x-road.eu/xsd/xroad.xsd`.



Table 2. WSDL elements for X-Road services

 Field                                                                  | Description
----------------------------------------------------------------------- | -----------------------------------------------------
 /definitions/binding/operation/@name                                   | Code of the service
 /definitions/binding/operation/xrd:version                             | Version of the service
 /definitions/portType/operation/documentation/xrd:title                | Title of the service (for displaying to users)
 /definitions/portType/operation/documentation/xrd:notes                | Description of the service (for displaying to users)
 /definitions/portType/operation/documentation/xrd:techNotes            | Description of the service (for developers)