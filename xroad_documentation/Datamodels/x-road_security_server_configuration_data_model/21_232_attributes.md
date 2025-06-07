#### 2.3.2 Attributes

| Name        | Type           | Modifiers        | Description          |
|:----------- |:--------------:|:----------------:|:--------------------:|
| id [PK]     | bigint         | NOT NULL         | Primary key          |
| apikey_id [FK]     | bigint         | NOT NULL         | Links one role to an API key          |
| role | character varying(255) | NOT NULL | Role name. Check constraint `valid_role` limits value to valid ones. |