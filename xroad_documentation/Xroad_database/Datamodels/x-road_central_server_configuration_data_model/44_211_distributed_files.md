### 2.11 DISTRIBUTED_FILES

Stores global configuration files that are distributed to the X-Road members. There are three kinds of distributed files:

- private parameters (distributed to only members of this X-Road instance),
- shared parameters (distributed to members of this X-Road instance and to members of federation partners),
- other configuration files (optional, depends on the configuration of the instance. The supported optional configuration files are described in the system configuration).

The record can be created in two different ways:

- The record corresponding to either private or shared parameters is created when a new global configuration is generated. Global configuration is triggered periodically (every minute) by a cron job.
- The record corresponding to other configuration file is created when there is a need to distribute new version of a configuration file specific to the X-Road instance. Then an X-Road security officer on an X-Road registration officer uploads a new configuration part file in the user interface.

The record is always deleted before new record with particular file name is created. The record is never modified.