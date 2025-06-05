#### 2.2.6 Backup and Restore Events

The audit log events related to backup and restore.

| Event                 | Data fields                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------|
| Back up configuration | <ul><li>backupFileName - the name of the created backup file</li></ul>                       |
| Upload backup file    | <ul><li>backupFileName - the name of the uploaded backup file</li></ul>                      |
| Delete backup file    | <ul><li>backupFileName - the name of the deleted backup file</li></ul>                       |
| Restore configuration | <ul><li>backupFileName - the name of the backup file used to restore configuration</li></ul> |