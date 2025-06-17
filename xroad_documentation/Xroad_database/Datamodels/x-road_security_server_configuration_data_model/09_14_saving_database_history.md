### 1.4 Saving Database History

This section describes a general mechanism for storing history of the database tables. All the history-aware tables have associated trigger update_history that records all the modifications to data. All the tables of security server database are history-aware, except for

  * history
  * databasechangelog
  * databasechangeloglock

When a row is created, updated or deleted in one of the history-aware tables, the trigger update_history is activated and invokes the stored procedure add_history_rows. For each changed column, add_history_rows inserts a row into the history table. The details of the stored procedures are described in section 1.6.

### 1.5 Entity-Relationship Diagram

![Entity-Relationship Diagram](img/dm-ss_x-road_security_server_configuration_data_model.svg)