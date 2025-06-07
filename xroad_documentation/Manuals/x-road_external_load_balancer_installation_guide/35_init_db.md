# Init db
sudo su postgres
cd /tmp
initdb --auth-local=peer --auth-host=scram-sha-256 --locale=en_US.UTF-8 --encoding=UTF8 -D /var/lib/pgsql/serverconf/
exit
```
* >**Note:** if PostgreSQL is not installed with the default configuration, the database creation command may be different, for example:
    ```bash
    # Init db
    sudo su postgres
    cd /tmp
    /usr/pgsql-13/bin/initdb --auth-local=peer --auth-host=scram-sha-256 --locale=en_US.UTF-8 --encoding=UTF8 -D /var/lib/pgsql/13/serverconf/
    exit
    ```

Configure SELinux:

```bash
semanage port -a -t postgresql_port_t -p tcp 5433
systemctl enable postgresql-serverconf
```

#### 4.2.2 on Ubuntu

```bash
sudo -u postgres pg_createcluster -p 5433 16 serverconf
```
In the above command, `16` is the *postgresql major version*. Use `pg_lsclusters` to find out what version(s) are available.