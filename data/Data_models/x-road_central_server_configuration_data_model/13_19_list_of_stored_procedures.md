### 1.9 List of Stored Procedures

The following stored procedures are present in the database, regardless of whether a given Central Server has been installed in standalone or HA setup.

1. add_history_rows: Detects the changes made as a result of the operation it is invoked on, and calls the insert_history_row stored procedure to insert a row to the history table, for each changed field. For insertions and deletions, a history record is inserted for each field of the original table.
2. insert_history_row: Inserts a single row with values corresponding to a changed field in one of the database tables. Invoked by the add_history_rows stored procedure.
3. insert_node_name: For each record inserted to a table with the field ha_node_name, sets the value of this field to
- the default value in standalone systems
- the name of the cluster node that initiated the insertion, in an HA setup.