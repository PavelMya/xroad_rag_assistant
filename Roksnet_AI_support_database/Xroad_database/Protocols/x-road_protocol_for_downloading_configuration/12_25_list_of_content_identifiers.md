### 2.5 List of Content Identifiers

This specification defines the following content identifiers. The X-Road implementations are free to define additional types of configuration parts that are distributed to configuration clients.

- *PRIVATE-PARAMETERS –* XML file conforming to private-parameters.xsd (see Annex C ).
- *SHARED-PARAMETERS* – XML file conforming to shared-parameters.xsd (see Annex B ). The configuration source can distribute several files of type *SHARED-PARAMETERS*. In this case each of the shared parameters files MUST describe separate X-Road instance.

In both of these cases, the implementation MUST include parameter *instance* whose value is the identifier for X-Road instance described by the configuration part. For example:

Content-Identifier: SHARED-PARAMETERS; instance="EE"