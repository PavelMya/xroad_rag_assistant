#### 2.5.2 Attributes

| Name                                              | Type           | Modifiers        | Description           |
|:--------------------------------------------------|:-----------------:|:----------- |:-----------------:|
| id [PK]                                           | integer | NOT NULL | Primary key |
| name                                              | character varying(255) |  | Name of the CA, used in user interfaces. Technically this is the subject name of the top level certification authority certificate. |
| top_ca_id [FK]                                    | integer |  | ID of the top level CA certificate entry of the record. See also documentation of the table ca_infos. Cannot be NULL. |
| authentication_only                               | boolean |  | If true, this CA can only issue authentication certificates. If false, this CA can issue all certificates. |                                                                                                          |
| cert_profile_info                                 | character varying(255) |  | Fully qualified Java class name that implements the CertificateProfileInfoProvider interface. The implementing class is used for extracting subject information from certificates. The implementing class must be present in classpath of both Central Server and securitys servers. Cannot be NULL. |
| created_at                                        | timestamp without time zone | NOT NULL | Record creation time, managed automatically. |
| updated_at                                        | timestamp without time zone | NOT NULL | Record last modified time, managed automatically. |