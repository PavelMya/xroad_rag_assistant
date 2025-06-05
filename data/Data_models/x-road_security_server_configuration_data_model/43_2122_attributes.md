#### 2.12.2 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------|
| id [PK] | bigint | NOT NULL | Primary key. |
| servercode  | character varying(255) |  | The code of this security server.  |
| owner [FK]  | bigint |  | The security server client who is the owner of this security server. References id attribute of CLIENT entity. |