### 3.1 General

Services are described using the Web Services Description Language (WSDL) 1.1 \[[WSDL](#Ref_WSDL)\].

X-Road supports versioned services. Different versions of the service represent minor technical changes in the service description. For example, a new version must be created when restructuring the service description (e.g., renaming or refactoring types in the XML Schema) or when changing types or names of fields. However, when the service semantics or data content of messages changes, a new service with a new code must be created.

In the context of service provision contracts, services are considered without version, meaning that all versions of the same service are considered to be equivalent. This also applies to access control restrictions applied in security servers – i.e., access control restrictions are specified for a service code without version. In order for this to work, all versions of the same service must implement the same contract.