#### 2.4.1 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------|
| id [PK] | bigint | NOT NULL | Primary key |
| data | oid |  | X.509 public key certificate in binary DER form. |
| client_id [FK] | bigint | | The security server client whose information system server uses this authentication certificate. References id attribute of CLIENT entity. |