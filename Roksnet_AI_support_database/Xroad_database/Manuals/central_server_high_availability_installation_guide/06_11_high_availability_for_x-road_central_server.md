### 1.1 High Availability for X-Road Central Server

The High Availability (HA) solution for the X-Road Central Server relies on a shared, optionally highly available database. This enables every node to work as a standalone Central Server which receives configuration updates from all other nodes. Security servers can download identical configuration from any of the public addresses published in a configuration anchor file.

Every Central Server node has its own:
- node specific keys to sign configuration;
- node specific public address which is distributed to the configuration clients in configuration anchor files;
- optionally, a management Security Server.

In addition, a highly-available PostgreSQL compatible database is required for storing the shared configuration. Setting up the database is out of the scope of this document.

The minimum X-Road Central Server version is 6.23.