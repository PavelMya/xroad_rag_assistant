#### 2.7.1 Attributes

| Name        | Type           | Modifiers        | Description           |
|:----------- |:-----------------:|:----------- |:-----------------|
| id [PK] | integer | NOT NULL | Primary key. Id of the lock. Currently there is only one lock. |
| locked | boolean | NOT NULL | Set to "1" if the Liquibase is running against this database. Otherwise set to "0". |
| lockgranted | timestamp with time zone |  | Date and time when the lock was granted. |
| lockedby | character varying(255) |  | Human-readable description of who the lock was granted to. |

### 2.8 GROUPMEMBER

Member of a local group. A group membership record is created when the administrator adds a new subsystem to a local group. The record is deleted when the administrator removes the subsystem from the local group. The record is never modified.

#### 2.8.1 Indexes

| Name        | Columns           |
|:----------- |:-----------------:|
| GROUPMEMBER_GROUPMEMBERID_fkey | groupmemberid |
| GROUPMEMBER_LOCALGROUP_ID_fkey | localgroup_id |