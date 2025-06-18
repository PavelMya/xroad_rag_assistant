#### 2.2.1 Attributes

| Name        | Type           | Modifiers        | Description          |
|:----------- |:--------------:|:----------------:|:--------------------:|
| id [PK]     | bigint         | NOT NULL         | Primary key          |
| encodedkey | character varying(255) | NOT NULL | Encoded API key |

### 2.3 APIKEY_ROLES

Roles linked to one API key.

#### 2.3.1 Indexes

| Name        | Columns           |
|:----------- |:-----------------:|
| unique_apikey_role | apikey_id, role |