### 1.6 Saving Database History

This section describes the general mechanism for storing the history of the database tables. All the history-aware tables have an associated trigger update_history that records all the modifications to data. All the tables of central database are history-aware, except for

- history,
- distributed_files

When a row is created, updated or deleted in one of the history-aware tables, the trigger update_history is activated and invokes the stored procedure add_history_rows. For each changed column, add_history_rows inserts a row into the history table. The details of the stored procedures are described in section 1.9.