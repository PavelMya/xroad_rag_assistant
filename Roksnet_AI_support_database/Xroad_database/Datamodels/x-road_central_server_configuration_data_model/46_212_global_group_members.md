### 2.12 GLOBAL_GROUP_MEMBERS

Join table that associates global group member identifier with the global group the member belongs to. See also documentation of the table global_groups.

The record is created when a new member needs to be added to a global group. Then an X-Road registration officer adds global group member in the user interface. The record is deleted when a global group member or the group where the member belongs to is deleted in the user interface. The record is never modified.

#### 2.12.1 Indexes

| Name        | Columns           |
|:----------- |:-----------------:|
| index_global_group_members_on_global_group_id | global_group_id |
| index_global_group_members_on_group_member_id | group_member_id |