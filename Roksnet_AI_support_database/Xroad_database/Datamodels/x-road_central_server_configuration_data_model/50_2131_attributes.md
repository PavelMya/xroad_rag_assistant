#### 2.13.1 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| group_code  | character varying(255) |  | Global group code that is unique inside the X-Road instance. Cannot be modified after the record is created. Cannot be NULL. |
| description  | character varying(255) |  | Longer, human-readable description of the group. Can be modified after the record is created. |
| created_at | timestamp without time zone | NOT NULL | Record creation time, managed automatically.  |
| updated_at | timestamp without time zone | NOT NULL | Record last modified time, managed automatically. |