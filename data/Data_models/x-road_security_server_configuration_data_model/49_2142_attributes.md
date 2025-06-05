#### 2.14.2 Attributes

| Name        | Type           | Modifiers   | Description      |
|:----------- |:--------------:|:----------- |:-----------------|
| id [PK]     | bigint         | NOT NULL    | Primary key.     |
| conf_id [FK] | bigint |  | Identifies the serverconf. References the id in SERVERCONF table. |
| name  | character varying(255) |  | The name of the TSP. Used for displaying in the user interface. |
| url  | character varying(255) | NOT NULL | The URL of the TSP. The security server will send time-stamping request using HTTP POST method.  |