### 12.4 Downloading, Uploading and Deleting Configuration Backup Files

The following actions can be performed in the Backup And Restore view.

To save the configuration backup file locally:
- click Download on the respective row and save the prompted file.

To delete the configuration backup file:
- click Delete on the respective row and confirm the action by clicking Yes.

To upload a configuration file from the local file system to the Central Server:
- click Upload backup, select a file to be uploaded and click Open. The uploaded configuration file appears in the list of configuration files.

### 12.5 Automatic Backups

By default the Central Server backs up its configuration automatically once every day. Backups older than 30 days are automatically removed from the server. If needed, the automatic backup policies can be adjusted by editing the `/etc/cron.d/xroad-center` file.