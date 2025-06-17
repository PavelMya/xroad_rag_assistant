### 6.1 Configuration database (and possible replicas) is lost

* Stop Central Servers.
* Set up a new database.
* Update the db.properties on each Central Server node to point to the new database.
* On one node, restore the database from a backup (see \[[UG-CS](#Ref_UG-CS)\]).
* Start Central Servers.

### 6.2 One or more cental server nodes lost, backup available

* Setup the missing nodes like described in [3.4](#34-workflow-for-adding-new-nodes-to-an-existing-ha-configuration)
* Restore configuration from a backup, skipping database restoration (see \[[UG-CS](#Ref_UG-CS)\]).

### 6.3 Some Central Server nodes lost, backup not available

See [3.4 Workflow for Adding New Nodes to an Existing HA Configuration](#34-workflow-for-adding-new-nodes-to-an-existing-ha-configuration)