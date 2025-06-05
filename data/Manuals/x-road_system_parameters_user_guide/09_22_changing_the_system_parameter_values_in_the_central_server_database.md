### 2.2 Changing the System Parameter Values in the Central Server Database

The central server database can be accessed with the psql utility using the following command (password is defined in `/etc/xroad/db.properties`):

	psql -U centerui -h localhost centerui_production

The default value of a system parameter can be overridden by adding the parameter name and value to the *system_parameters* table:

	INSERT INTO system_parameters (key, value, created_at, updated_at) VALUES ('parameter_name', 'parameter_value', (now() at time zone 'utc'), (now() at time zone 'utc'));

To edit the value of a system parameter already inserted into the *system_parameters* table:

	UPDATE system_parameters SET value = '*parameter_value*', updated_at = (now() at time zone 'utc') WHERE key = 'parameter_name';

To restore the default value of a system parameter, delete the parameter from the *system_parameters* table:

	DELETE FROM system_parameters WHERE key = 'parameter_name';

**NB! Modifying or deleting system parameters other than the ones listed in section** [System Parameters in the Database](#system-parameters-in-the-database) **will cause the system to crash.**