### 5.3 Could Not Create Default Cluster

If the following error message is displayed during PostgreSQL installation

`Error: The locale requested by the environment is invalid.`<br>
`Error: could not create default cluster. Please create it manually with pg_createcluster 12 main –start`

Use the following command to create the PostgreSQL data cluster:

`LC_ALL="en_US.UTF-8" sudo  pg_createcluster --start 12 main`

The interrupted installation can be finished using

`sudo apt --fix-broken install`