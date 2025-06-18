### 1.5 Creating, Backing Up and Restoring the Database

This database is integrated into X-Road message log component.

The database, the database user and the data model is created by the component's installer. The database updates are packaged as component updates and are applied when the component is upgraded. From the technical point of view, the database structure is created and updated using Liquibase tool (see http://www.liquibase.org/). The migration scripts can be found both in component source and in file system of the installed component.

The database is used for logging purposes only and does not contain any configuration. Backing-up and restoring the database is not necessary for the functioning of the component.