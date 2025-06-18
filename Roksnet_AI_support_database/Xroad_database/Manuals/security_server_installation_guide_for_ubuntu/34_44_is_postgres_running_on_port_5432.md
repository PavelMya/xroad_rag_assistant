### 4.4 Is Postgres Running On Port 5432?

If the following error message appears during installation

    Is postgres running on port 5432 ?
    Aborting installation! please fix issues and rerun with apt-get -f install,

check if any of the following errors occurred during the installation of PostgreSQL.

* Error installing the data cluster. Refer to section [“Could not create default cluster”](#43-could-not-create-default-cluster).

* The PostgreSQL data cluster installed during the installation of the Security Server is not configured to listen on port 5432. To verify and configure the listening port, edit the PostgreSQL configuration file in `/etc/postgresql/10/main/postgresql.conf`. If you change the listening port, the postgresql service must be restarted.

The interrupted installation can be finished using

    sudo apt-get -f install