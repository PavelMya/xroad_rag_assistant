## Annex B Database Users

| User     | Database            | Privileges               | Description                                                                                         |
|----------|---------------------|--------------------------|-----------------------------------------------------------------------------------------------------|
| centerui | centerui_production | CREATE,TEMPORARY,CONNECT | The database user used to create the schema and read/write the database during application runtime. |
| postgres | ALL                 | ALL                      | PostgreSQL database default superuser.                                                              |

## Annex C Deployment Options

### C.1 General

X-Road Central Server can be deployed in multiple ways. The simplest option is to have a single Central Server with local database. This is usually fine for development purposes, but there are multiple reasons to tailor the deployment.