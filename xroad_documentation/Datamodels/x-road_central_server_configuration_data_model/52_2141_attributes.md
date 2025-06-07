#### 2.14.1 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| operation  | character varying(255) | NOT NULL | Name of the database operation (possible values are 'INSERT', 'UPDATE' and 'DELETE').  |
| table_name  | character varying(255) | NOT NULL | Name of the table the operation was made on.  |
| record_id  | integer | NOT NULL | ID of the record that was inserted, updated or deleted, in the original table.  |
| field_name  | character varying(255) | NOT NULL | Name of the column that was inserted, updated or deleted.   |
| old_value  | text |  | Previous value of the column if applicable (NULL for INSERT operations).  |
| new_value  | text |  | New value of the column if applicable (NULL for DELETE operations).  |
| user_name  | character varying(255) | NOT NULL | Name of either the logged in user of the UI or the database user behind the connection, that initiated the operation.  |
| timestamp  | timestamp without time zone | NOT NULL | Date and time of the operation.  |
| ha_node_name | character varying(255) |  | Name of the cluster node that initiated the insertion in an HA setup; the default value in standalone setup. |