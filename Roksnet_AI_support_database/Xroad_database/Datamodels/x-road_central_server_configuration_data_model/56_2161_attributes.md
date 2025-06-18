#### 2.16.1 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| code  | character varying(255) |  | Member class code, unique inside an X-Road instance. Cannot be NULL. |
| description  | character varying(255) |  | Member class description.  |
| created_at  | timestamp without time zone | NOT NULL | Record creation time, managed automatically.  |
| updated_at  | timestamp without time zone | NOT NULL | Record last modified time, managed automatically. |