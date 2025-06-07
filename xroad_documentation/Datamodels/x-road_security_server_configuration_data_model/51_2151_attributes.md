#### 2.15.1 Attributes

| Name        | Type           | Modifiers   | Description      |
|:----------- |:--------------:|:----------- |:-----------------|
| id [PK]     | bigint         | NOT NULL    | Primary key.     |
| username | character varying(255) | NOT NULL | Name of the user who has customized their user interface language. |
| locale | character varying(255) |  | The preferred language code. Valid values are 'en' for English, and 'et' for Estonian. |