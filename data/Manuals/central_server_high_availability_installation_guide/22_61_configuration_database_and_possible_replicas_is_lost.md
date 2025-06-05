### 6.1 Configuration database (and possible replicas) is lost

* Stop Central Servers.
* Set up a new database.
* Update the db.properties on each Central Server node to point to the new database.
* On one node, restore the database from a backup (see \[[UG-CS](#Ref_UG-CS)\]).
* Start Central Servers.