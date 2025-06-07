### 1.10 List of Triggers

The following triggers are present in the database, regardless of whether a given Central Server has been installed in standalone or HA setup.

1. `update_history`: Invokes the `add_history_rows` stored procedure upon insertions, updates and deletions of records. Created for each history-aware table.
2. `insert_node_name`: Invokes the `insert_node_name` stored procedure upon insertions. Created for each table with the ha_node_name field.

## 2 Description of Entities