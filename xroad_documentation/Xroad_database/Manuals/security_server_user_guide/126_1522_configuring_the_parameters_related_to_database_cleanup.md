#### 15.2.2 Configuring the Parameters Related to Database Cleanup

Depending on the load and resources of the system, it may be necessary to change the interval of the removal of old database records.

The following parameters must be placed in the `[op-monitor]` section of the file `/etc/xroad/conf.d/local.ini`.

The parameter `keep-records-for-days` should be edited, for instance if the disk fills up before cleanup occurs, or alternatively, if the default period of 7 days is too short. The parameter `clean-interval` (a Cron expression \[[CRON](#Ref_CRON)\]) defines how often the system checks whether cleanup should be done. If the default period of 12 hours is too long or short it should be edited according to your needs.