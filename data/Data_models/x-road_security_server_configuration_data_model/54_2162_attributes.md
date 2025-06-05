#### 2.16.2 Attributes

| Name           |            Type             | Modifiers | Description                                                                                                                       |
|:---------------|:---------------------------:|:----------|:----------------------------------------------------------------------------------------------------------------------------------|
| id [PK]        |           bigint            | NOT NULL  | Primary key.                                                                                                                      |
| client_id [FK] |           bigint            |           | The security server client providing the services described in this SERVICEDESCRIPTION. References id attribute of CLIENT entity. |
| url            |   character varying(255)    | NOT NULL  | The URL of the SERVICEDESCRIPTION. The URL points to the information system of the security server client.                        |
| disabled       |           boolean           | NOT NULL  | A flag indicating whether the SERVICEDESCRIPTION and all its services are disabled.                                               |
| disablednotice |   character varying(255)    |           | The error message returned in response to a call to a service belonging to a disabled SERVICEDESCRIPTION.                         |
| refresheddate  | timestamp without time zone |           | The time when the SERVICEDESCRIPTION was last refreshed.                                                                          |
| type           |   character varying(255)    | NOT NULL  | The type of the service description. At the time of writing 'WSDL' and 'OPENAPI3' types are supported.                            |