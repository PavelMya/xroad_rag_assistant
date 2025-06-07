### 6.2 Refreshing a service description

**Access rights:** [Service Administrator](#xroad-service-administrator)

Upon refreshing, the Security Server reloads the service description file from the service description URL to the Security Server and checks the service information in the reloaded file against existing services. If the composition of services in the new service description has changed compared to the current version, a warning is displayed and you can either continue with the refresh or cancel.

To refresh the service description, follow these steps.

1.  Navigate to **CLIENTS** tab, click the name of the client containing service you wish to refresh and click the **SERVICES** tab.

2.  Click the arrow symbol in front of the WSDL or REST to be refreshed and click the **Refresh** button.

3.  If the new service description contains changes compared to the current service description in the Security Server, a warning is displayed. To proceed with the refresh, click **CONTINUE**.

When the service description is refreshed, the existing services' settings are not overwritten.