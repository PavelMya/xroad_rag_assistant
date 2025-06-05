### 4.8 Renaming Client subsystem

**Access rights:** [Registration Officer](#xroad-registration-officer)

To rename a client subsystem, follow these steps.

1.  In the **CLIENTS** view click the name of subsystem that you wish to rename

2.  In the window that opens, click **Edit** and then enter name for subsystem and click **Save**. The Security Server automatically sends a client rename request to the X-Road Central Server.

3.  Next, a subsystem is put into "Name change is submitted" state, which doesn't affect the subsystem functionality. Once the name change is propagated through the global configuration, subsystem name is updated.

**Note:** In case of "Registered" no additional renames are allowed for the subsystem while its rename isn't propagated through global configuration. Only exception is "Saved" subsystem in which case multiple renames are allowed, where the latest rename replaces the previous one and rename will be executed on client registration request using last provided name.