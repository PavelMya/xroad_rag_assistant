### 12.2 Restoring the System Configuration in the User Interface

To restore configuration, follow these steps.
1. In the Settings tab, select Back Up and Restore sub-tab.
2. Select a file from the list of configuration backup files and click Restore.
3. Confirm to proceed.
4. A popup notification shows after the restore whether the restoring was successful or not.

If something goes wrong while restoring the configuration it is possible to revert back to the old configuration. Central Server stores so called pre-restore configuration automatically to `/var/lib/xroad/conf_prerestore_backup.tar`. Move it to `/var/lib/xroad/backup/` folder and use the command line interface described in the next chapter (some specific switches with the restore command is required).