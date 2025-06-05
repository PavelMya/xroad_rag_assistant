#### 2.7.1 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------|
| id [PK] | integer | NOT NULL | Primary key. Id of the lock. Currently there is only one lock. |
| locked | boolean | NOT NULL | Set to "1" if the Liquibase is running against this database. Otherwise set to "0". |
| lockgranted | timestamp with time zone |  | Date and time when the lock was granted. |
| lockedby | character varying(255) |  | Human-readable description of who the lock was granted to. |