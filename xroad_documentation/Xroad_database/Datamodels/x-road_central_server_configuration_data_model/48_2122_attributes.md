#### 2.12.2 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| group_member_id [FK] | integer |  | ID of the member identifier that belongs to this global group. References id attribute of identifiers entity. Cannot be NULL. |
| created_at  | timestamp without time zone | NOT NULL | Record creation time, managed automatically.  |
| updated_at  | timestamp without time zone | NOT NULL | Record last modified time, managed automatically.  |
| global_group_id [FK] | integer |  | ID of the global group the member referenced by group_member_id belongs to. References id attribute of global_groups entity. Cannot be NULL. |