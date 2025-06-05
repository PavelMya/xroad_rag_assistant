### 1.3 Identifying Entities

Significant entities in the X-Road system have globally unique identifiers. Identifiers consist of an object type and a sequence of hierarchical codes.

All the identifiers start with the code identifying the instance of the X-Road system. Typically, this should be the ISO code of the country running the X-Road instance, optionally amended with a suffix corresponding to the environment. For example, for Estonia, the production environment is designated as “EE”, whereas the test environment is “EE-test”. The codes for X-Road instances are the only ones that need to be globally unique. All other parts of the identifiers are managed by X-Road instances.

Next, we will describe how globally unique identifiers are constructed for various types of entities. When representing entities as strings the format *T:C1/C2/...* is used, where *T* is type of the entity and *C1, C2, ...* are the component codes. Note: the given format is only used in this document. In messages and configuration files, the identifiers are represented in XML format described in [Section 2.1](#21-identifiers).

-   **X-Road member** – *MEMBER:\[X-Road instance\]/\[member class\]/\[member code\]*. The identifier consists of the following components:

    – code corresponding to the X-Road instance;

    – code identifying the member class (e.g., government agency, private enterprise, physical person. Typically, member codes are issued by an authority guaranteeing the uniqueness of the codes within the given member class); and

    – member code that uniquely identifies the given X-Road member within its member class.

    Example: identifier MEMBER:EE/BUSINESS/123456789 represents an organization registered in Estonia (EE) with a business registry code (BUSINESS) of 123456789.

-   **Subsystem** – *SUBSYSTEM:\[subsystem owner\]/\[subsystem code\]*. Identifier for a subsystem consists of the identifier of the X-Road member that owns the subsystem, and a subsystem code. The subsystem code is chosen by the X-Road member and it must be unique among the subsystems of this member.
    Example: SUBSYSTEM:EE/BUSINESS/123456789/highsecurity identifies a subsystem with code highsecurity belonging to the X-Road member from the previous example (MEMBER:EE/BUSINESS/123456789).

-   **Service** – *SERVICE:\[service provider\]/\[service code\]/\[service version\]*. Identifier for a service consists of an identifier of the service provider (either an X-Road member or a subsystem), service code, and version. The service code is chosen by the service provider. Version is optional and can be used to distinguish between technically incompatible versions of the same basic service.
    Example: SERVICE:EE/BUSINESS/123456789/highsecurity/getSecureData/v1 identifies version v1 of service getSecureData that is offered by subsystem SUBSYSTEM:EE/BUSINESS/123456789/highsecurity.