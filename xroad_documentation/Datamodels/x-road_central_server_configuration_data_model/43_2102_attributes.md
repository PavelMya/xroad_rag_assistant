#### 2.10.2 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| source_type  | character varying(255) |  | Type of the configuration source, can be either 'internal' or 'external'.  |
| active_key_id [FK] | integer |  | ID of the active key that is used to sign the distributed configuration (all the other keys are only included in the generated configuration anchor).References id attribute of configuration_signing_keys entity.  |
| anchor_file  | qqbytea |  | Configuration anchor file (in XML format). The anchor is re-generated if any information contained in the anchor is saved. |
| anchor_file_hash  | text |  | Configuration anchor file hash (for displaying in user interface). Updated when the configuration anchor is re-generated. |
| anchor_generated_at  | timestamp without time zone |  | Configuration anchor generation time. Updated when the configuration anchor is re-generated. |
| ha_node_name | character varying(255) |  | Name of the cluster node that initiated the insertion in an HA setup; the default value in standalone setup. |