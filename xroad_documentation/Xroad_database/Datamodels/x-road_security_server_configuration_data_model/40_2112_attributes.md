#### 2.11.2 Attributes

| Name           |            Type             | Modifiers | Description                                                                                               |
|:---------------|:---------------------------:|:----------|:----------------------------------------------------------------------------------------------------------|
| id [PK]        |           bigint            | NOT NULL  | Primary key                                                                                               |
| groupcode]     |   character varying(255)    | NOT NULL  | The code of the group.                                                                                    |
| description    |   character varying(255)    | NOT NULL  | The description of the group.                                                                             |
| updated        | timestamp without time zone | NOT NULL  | The time when the description of the group was last updated.                                              |
| client_id [FK] |           bigint            |           | The security server client for whom the local group is defined. References id attribute of CLIENT entity. |

### 2.12 SERVERCONF

The top-level configuration of the security server, specifying the owner and the code of this security server. This table contains only one record that is created when the security server is initialized. The record is never modified or deleted.

#### 2.12.1 Indexes

| Name        | Columns           |
|:----------- |:-----------------:|
| SERVERCONF_OWNER_fkey | owner |