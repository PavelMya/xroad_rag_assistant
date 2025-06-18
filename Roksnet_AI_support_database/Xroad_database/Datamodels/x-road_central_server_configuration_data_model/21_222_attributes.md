#### 2.2.2 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------:|
| id [PK] | integer | NOT NULL | Primary key |
| trusted_anchor_id [FK] | integer |  | ID of the trusted anchor that contains this anchor URL. References id attribute of trusted_anchors entity. Cannot be NULL. |
| url | character varying(255) | | The URL that can be used by the configuration client to download the configuration from the configuration source. Must correspond to the URL format (See also URL specification: http://www.w3.org/Addressing/URL/url-spec.txt). Cannot be NULL. |

### 2.3 APIKEY

API key which grants access to REST API operations.

#### 2.3.1 Attributes

| Name        | Type           | Modifiers |   Description    |
|:----------- |:-----------------:|:----------|:----------------:|
| id [PK] | bigint | NOT NULL  |   Primary key    |
| encodedkey | character varying(255) | NOT NULL  | Encoded API key. |

### 2.4 APIKEY_ROLES

Roles linked to one API key.

#### 2.4.1 Indexes

| Name               |     Columns     |
|:-------------------|:---------------:|
| unique_apikey_role | apikey_id, role |