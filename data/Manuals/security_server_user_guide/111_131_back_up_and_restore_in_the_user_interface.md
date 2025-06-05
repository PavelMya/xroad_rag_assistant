### 13.1 Back up and Restore in the User Interface

**Access rights:** [System Administrator](#xroad-system-administrator)

The backup and restore view can be accessed from the **Navigation tabs** by selecting **Back Up and Restore**.

To **back up configuration**, follow these steps.

1.  Navigate to **SETTINGS** tab and in the view that opens click **BACKUP AND RESTORE** tab.

2.  Click **BACK UP CONFIG.**

3.  The configuration backup file appears in the list of configuration backup files.

4.  To save the configuration backup file to the local file system, click **DOWNLOAD** on the configuration file's row.

To **restore configuration**, follow these steps.

1.  Click **Restore** on the appropriate row in the list of configuration backup files and click **YES**.

2.  A popup notification shows after the restore whether the restoring was successful or not.

If something goes wrong while restoring the configuration it is possible to revert back to the old configuration.
Security Server stores so called pre-restore configuration automatically to `/var/lib/xroad/conf_prerestore_backup.tar`. Either move it to `/var/lib/xroad/backup/` folder and utilize the user interface to restore it or use the command line interaface described in the next chapter.

To **delete a configuration backup file**, click **Delete** on the appropriate row in the configuration backup file list and then click **YES**.

To **upload a configuration backup file** from the local file system to the Security Server, click **UPLOAD BACKUP**,
select a file and click **YES**. The uploaded configuration file appears in the list of configuration files. Bear in mind
that only files signed with current Security Server encryption key can be restored via user interface. All other archives
can be restored only from command line.

As long as original keypair is intact no additional steps are needed even when backup encryption is turned on.