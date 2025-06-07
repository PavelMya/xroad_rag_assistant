##### 4.2.1.2 on RHEL 8 and 9

Create a new `systemctl` service unit for the new database. As root, make a copy for the new service
>**Note:** We assume that the default PostgreSQL database service file is `/lib/systemd/system/postgresql.service`, but depending on the PostgreSQL installation, the service file name can be a little bit different, for example `/lib/systemd/system/postgresql-13.service`.

```bash
cp /lib/systemd/system/postgresql.service /etc/systemd/system/postgresql-serverconf.service 
```

Edit `/etc/systemd/system/postgresql-serverconf.service` and override the following properties:

```properties
[Service]
...
Environment=PGPORT=5433
Environment=PGDATA=/var/lib/pgsql/serverconf
```

Create the database:

```bash