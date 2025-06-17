### 10.6 Enable/Disable maintenance mode for the Security Server

**Access rights:** [System Administrator](#xroad-system-administrator)

To enable or disable maintenance mode for the Security Server, follow these steps.
1. In the **Navigation tabs**, select **SETTINGS**.
2. In the opening view select **SYSTEM PARAMETERS** tab.
3. At the top of the **SYSTEM PARAMETERS** tab, click the switch for Maintenance mode to turn it on or off.
4. The confirmation dialog will open with an optional field for message (only when enabling maintenance mode) which will be included in error messages returned to clients when they try to access services when the maintenance mode is enabled.
5. Click **Confirm** to proceed.
6. Next, the maintenance mode request is submitted to the Central Server. This does not affect the Security Server functionality until the change is propagated through the global configuration - the Security Server downloads a new version of the global configuration where the maintenance mode is enabled. Once propagated, the Security Server will have the maintenance mode set to "On" or "Off." Other Security Servers will recognize the change and start/stop sending requests to the Security Server depending on the maintenance mode status.

Notice that if the Security Server is provider of management services, then the maintenance mode is disabled without possibility to enable it.