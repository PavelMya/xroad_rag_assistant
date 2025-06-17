#### 2.23.1 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| key | character varying(255) |  | System parameter key. Cannot be NULL. |
| value  | character varying(255) |  | System parameter value corresponding to the key.  |
| created_at  | timestamp without time zone | NOT NULL | Record creation time, managed automatically.  |
| updated_at  | timestamp without time zone | NOT NULL | Record last modified time, managed automatically.  |
| ha_node_name | character varying(255) |  | Name of the cluster node that initiated the insertion in an HA setup; the default value in standalone setup. |