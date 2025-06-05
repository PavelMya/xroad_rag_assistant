## Annex B Default Database Users

| User             | Database   | Privileges               | Description                                                                              |
|------------------|------------|--------------------------|------------------------------------------------------------------------------------------|
| serverconf       | serverconf | TEMPORARY,CONNECT        | The database user used to read/write the serverconf database during application runtime. |
| serverconf_admin | serverconf | CREATE,TEMPORARY,CONNECT | The database user used to create/update the serverconf schema.                           |
| messagelog       | messagelog | TEMPORARY,CONNECT        | The database user used to read/write the messagelog database during application runtime. |
| messagelog_admin | messagelog | CREATE,TEMPORARY,CONNECT | The database user used to create/update the messagelog schema.                           |
| opmonitor        | op-monitor | TEMPORARY,CONNECT        | The database user used to read/write the op-monitor database during application runtime. |
| opmonitor_admin  | op-monitor | CREATE,TEMPORARY,CONNECT | The database user used to create/update the op-monitor schema.                           |
| postgres         | ALL        | ALL                      | PostgreSQL database default superuser.                                                   |