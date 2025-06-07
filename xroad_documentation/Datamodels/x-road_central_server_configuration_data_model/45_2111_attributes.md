#### 2.11.1 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| file_name  | character varying(255) |  | Name of the distributed file. Any valid file name. Cannot be NULL. |
| file_data  | bytea |  | Contents of the distributed file. Cannot be NULL. |
| content_identifier  | character varying(255) |  | Content identifier of the distributed file. The content identifier is used by Security Server to determine the exact type of the file. Must be unique inside an X-Road instance. Cannot be NULL. |
| file_updated_at  | timestamp without time zone |  | Time when the distributed file was last updated.  |
| ha_node_name | character varying(255) |  | Name of the cluster node that initiated the insertion in an HA setup; the default value in standalone setup. |
| version | integer | NOT NULL | Version of the distributed file. Cannot be NULL. Default is 0 which means it is not versioned and belongs to all versions of global configuration. |