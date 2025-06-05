### 1.6 List of Stored Procedures

1. add_history_rows: Detects the changes made as a result of the operation it is invoked on, and calls the insert_history_row stored procedure to insert a row to the history table, for each changed field. For insertions and deletions, a history record is inserted for each field of the original table.
2. insert_history_row: Inserts a single row with values corresponding to a changed field in one of the database tables. Invoked by the add_history_rows stored procedure.