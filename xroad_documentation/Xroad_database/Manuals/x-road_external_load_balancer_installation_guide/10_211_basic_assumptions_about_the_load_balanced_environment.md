#### 2.1.1 Basic assumptions about the load balanced environment
* Adding or removing nodes to or from the cluster is infrequent. New nodes need to be added manually and this takes some
  time.
* Changes to the configuration files are relatively infrequent and some downtime in ability to propagate the changes can
  be tolerated.
* The cluster uses a primary-secondary model and the configuration primary is not replicated.