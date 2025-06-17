### 10.3 Managing the Timestamping Services

**Access rights:** [Security Officer](#xroad-security-officer)

To add a timestamping service, follow these steps.

1.  In the **Navigation tabs**, select **SETTINGS**.

2.  In the opening view select **SYSTEM PARAMETERS** tab.

3.  In the **Timestamping Services** section, click **ADD**.

4.  In the dialog that opens, select a service and click **ADD**.

To delete a timestamping service, follow these steps.

1.  In the **Navigation tabs**, select **SETTINGS**.

2.  In the opening view select **SYSTEM PARAMETERS** tab.

3.  In the **Timestamping Services** section, click **DELETE** at the end of the row of the service you wish to delete.

*Note*: If more than one timestamping service is configured, the Security Server will try to get a timestamp from the topmost service in the table, moving down to the next service if the try was unsuccessful. The failover covers both connection and timestamp response verification issues. For example, Security Server is not able to establish a connection to a timestamping service because of a misconfigured firewall, or verification of a timestamp response fails because of the sign certificate of the timestamping service is changed.