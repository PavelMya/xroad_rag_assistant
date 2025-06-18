#### 2.2.6 Backup and Restore Events

The audit log events related to backup and restore.

| Event                 | Data fields                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------|
| Back up configuration | backupFileName - the name of the created backup file                       |
| Upload backup file    | backupFileName - the name of the uploaded backup file                      |
| Delete backup file    | backupFileName - the name of the deleted backup file                       |
| Restore configuration | backupFileName - the name of the backup file used to restore configuration |