### 2.11 LOCALGROUP

Group of members and/or subsystems. The group is local to a security server client and is used in access rights management. Local groups are connected to a security server client and can only be used for services belonging to that client. A local group record is created when the administrator adds a new local group to a security server client. The record is modified when the administrator changes the description of the group. The record is deleted when the administrator deletes the group or the security server client for whom the group is defined.

#### 2.11.1 Indexes

| Name        | Columns           |
|:----------- |:-----------------:|
| LOCALGROUP_CLIENT_ID_fkey | client_id |