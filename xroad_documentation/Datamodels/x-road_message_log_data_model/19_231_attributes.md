#### 2.3.1 Attributes

| Name          | Type                     | Modifiers  | Description |
| ------------- |:------------------------:| ----------:| -----------:|
| id            | character varying(255)   | NOT NULL   | The identifier of the migration. |
| author        | character varying(255)   | NOT NULL   | The author of the migration. |
| filename      | character varying(255)   | NOT NULL   | The filename containing the migration script. |
| dateexecuted  | timestamp with time zone | NOT NULL   | The time when the migration was executed. Used with orderexecuted to determine rollback order. |
| orderexecuted | integer                  | NOT NULL   | The order number in which the migration was executed. Used in addition to dateexecuted to ensure order is correct even when the databases datetime supports poor resolution. |
| exectype      | character varying(10)    | NOT NULL   | The type of the execution that was performed. Possible values are EXECUTED, FAILED, SKIPPED, RERAN, and MARK_RAN. |
| md5sum        | character varying(35)    |            | The MD5 hash of the migration script when it was executed. Used on each run to ensure there have been no unexpected changes to the migration script. |
| description   | character varying(255)   |            | Short auto-generated human readable description of the migration. |
| comments      | character varying(255)   |            | The comments of the migration. |
| tag           | character varying(255)   |            | The tag of the migration. |
| liquibase     | character varying(20)    |            | The version of the Liquibase that performed the migration. |
| contexts      | character varying(255)   |            | Context(s) used to execute the changeset. |
| labels        | character varying(255)   |            | Label(s) used to execute the changeset. |
| deployment_id | character varying(10)    |            | Changesets deployed together will have the same unique identifier. |

### 2.4 DATABASECHANGELOGLOCK

Lock used by Liquibase to allow only one migration of the database to run at a time. This table has a technical nature and is not managed by X-Road application software.