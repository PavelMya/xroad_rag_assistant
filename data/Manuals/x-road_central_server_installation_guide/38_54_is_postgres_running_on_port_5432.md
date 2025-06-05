### 5.4 Is Postgres Running on Port 5432?

If the following error message appears during installation

`Is postgres running on port 5432 ?`<br>
`Aborting installation! please fix issues and rerun with apt -f install`

Then check if any of the following errors occurred during the installation of PostgreSQL.

- Error installing the data cluster. Refer to section 4.3.
- The PostgreSQL data cluster installed during the installation of the Security Server is not configured to listen on port 5432. To verify and configure the listening port, edit the PostgreSQL configuration file in /etc/postgresql/12/main/postgresql.conf. If you change the listening port, the postgresql service must be restarted.

The interrupted installation can be finished using

`sudo apt --fix-broken install`