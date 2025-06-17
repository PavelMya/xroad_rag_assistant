### 4.2 PostgreSQL Is Not UTF8 Compatible

If the Security Server installation is aborted with the error message

    postgreSQL is not UTF8 compatible,

then the PostgreSQL package is installed with a wrong locale. One way to resolve it is to remove the data store created upon the PostgreSQL installation and recreate it with the correct encoding.

**WARNING**: All data in the database will be erased!

    sudo pg_dropcluster --stop 10 main
    LC_ALL="en_US.UTF-8" sudo pg_createcluster --start 10 main

To complete the interrupted installation, run the command

    sudo apt-get -f install