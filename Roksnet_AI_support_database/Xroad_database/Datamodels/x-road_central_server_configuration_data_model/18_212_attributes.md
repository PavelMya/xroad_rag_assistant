#### 2.1.2 Attributes

| Name               |  Type   | Modifiers        | Description          |
|:-------------------|:-------:|:----------- |:-----------------:|
| id [PK]            | integer | NOT NULL | Primary key |
| anchor_url_id [FK] | integer |  | ID of the configuration anchor URL the certificate belongs to. References id attribute of anchor_urls entity. As every anchor URL certificate must belong to particular anchor URL, the column cannot be NULL (currently set in the data model layer of the user interface). |
| cert               |  bytea  |  |                                                                                                                                                                                                                                                                              |