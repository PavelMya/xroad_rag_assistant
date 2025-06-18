#### 2.13.2 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------|
| id [PK] | bigint | NOT NULL | Primary key. |
| servicecode | character varying(255) | NOT NULL | The code of the service. |
| serviceversion | character varying(255) |  | The version of the service.|
| title | character varying(255) |  | The title of the service. |
| url | character varying(255) |  | The URL of the service. |
| sslauthentication | boolean |  | A flag indicating whether the certificate of the service provider should be verified for SSL/TLS connections. NULL value is interpreted as true. Trusted service provider certificates are stored as CERTIFICATE entities. |
| timeout | integer |  | The maximum time in seconds that the service provider can  take to respond to a query. |
| servicedescription_id [FK] | bigint |  | The servicedescription of which this service is part of. References id attribute of SERVICEDESCRIPTION entity. |