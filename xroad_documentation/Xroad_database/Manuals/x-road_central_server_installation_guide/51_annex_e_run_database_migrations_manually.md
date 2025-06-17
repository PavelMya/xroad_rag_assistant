## Annex E Run Database Migrations Manually

When installing/upgrading the Central Server, it's possible to skip the automatic database migrations. The installer respects the setting `skip_migrations = true/false` in the file `/etc/xroad/db.properties`. For clean installations the installer asks the setting value (among other settings) using debconf. For upgrade installations the setting `skip_migrations = true` needs to be set before upgrading by editing the aforementioned properties file or by running `dpkg-reconfigure xroad-center` to alter the settings via debconf.

To run the database migrations manually, follow the next steps.

1. Login to the Central Server console and issue the following command as root.

2. Ensure that the Central Server user interface process is stopped.

```bash
systemctl stop xroad-center
```

3. Run the database migrations.

```bash
/usr/share/xroad/db/migrate.sh db:migrate
```

4. Start the services, if they are not yet running.

```bash
systemctl start xroad-center
```

5. Verify that everything is working by performing the steps described in [2.12 Post-Installation Checks](#212-post-installation-checks).