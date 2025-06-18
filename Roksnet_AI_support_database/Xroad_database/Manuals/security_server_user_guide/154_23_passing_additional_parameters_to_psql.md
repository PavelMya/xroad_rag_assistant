## 23 Passing additional parameters to psql

By default any scripts(for example backup/restore) that uses `psql` utility tries to parse `/etc/xroad/db.properties` file for database related configurations like: database name, user, password, host, port. If the file is not found, the script may use default values which will point to local database. When such behaviour doesn't cover the requirements, it is possible to pass additional configurations to `psql` utility using environment variables from file.

First step to pass additional configurations is to create `db_libpq.env` file in `/etc/xroad/` folder if it isn't created yet. It may also require adjustments of access rights to file.

Example of file contents:

```bash
export PGSSLMODE="verify-full"
export PGSSLCERT="/etc/xroad/ssl/internal.crt"
export PGSSLKEY="/etc/xroad/ssl/internal.key"
export PGSSLROOTCERT="/etc/xroad/ssl/root.crt"
#export PGTARGETSESSIONATTRS="read-write"
```

This example shows how SSL configurations for _psql_ could look like. List of possible environment variables can be found in [Postgres documentation](https://www.postgresql.org/docs/current/libpq-envars.html).

Some of the variables like `PGOPTIONS`, `PGDATABASE`, `PGUSER`, `PGPASSWORD` are already used by scripts(created and initialized with values from `/etc/xroad/db.properties` file) so adding same variables to `db_libpq.env` won't have any effect on script behaviour.

In case it is needed to pass additional flags to internally initialized `PGOPTIONS` variable, then `PGOPTIONS_EXTRA` variable can be used. It will be appended to `PGOPTIONS` variable.