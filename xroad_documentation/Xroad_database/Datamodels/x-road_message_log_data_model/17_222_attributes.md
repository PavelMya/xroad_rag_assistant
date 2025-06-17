#### 2.2.2 Attributes

| Name        | Type                   | Modifiers  | Description |
| ----------- |:----------------------:| ----------:| -----------:|
| id [PK]     | bigint                 | NOT NULL   | Primary key |
| digest      | text                   |            | Digest of the last archive file. |
| filename    | character varying(255) |            | The filename of the last archive. |
| groupname   | character varying(255) |            | The name of the archive group. |