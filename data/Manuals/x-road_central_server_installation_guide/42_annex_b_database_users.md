## Annex B Database Users

| User     | Database            | Privileges               | Description                                                                                         |
|----------|---------------------|--------------------------|-----------------------------------------------------------------------------------------------------|
| centerui | centerui_production | CREATE,TEMPORARY,CONNECT | The database user used to create the schema and read/write the database during application runtime. |
| postgres | ALL                 | ALL                      | PostgreSQL database default superuser.                                                              |