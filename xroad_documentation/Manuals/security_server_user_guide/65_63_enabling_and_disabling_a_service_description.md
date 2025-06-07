### 6.3 Enabling and Disabling a service description

**Access rights:** [Service Administrator](#xroad-service-administrator)

A disabled service description is displayed in the services' list with a disabled switch icon on the same row.

Services described by a disabled service description cannot be accessed by the service clients – if an attempt is made to access the service, an error message is returned, containing the information entered by the Security Server's administrator when the service description was disabled.

If a service description is enabled, the services described there become accessible to users. Therefore it is necessary to ensure that before enabling the service description, the parameters of all its services are correctly configured (see [6.6](#66-changing-the-parameters-of-a-service)).

To **enable** or **disable** a service description, follow these steps.

1.  Navigate to **CLIENTS** tab, click the name of the client containing service you wish to view and click the **SERVICES** tab.

2. Click the switch icon on the same row with service WSDL or REST service you wish to enable or disable

(3.) If the service was disabled a popup will appear. In the popup, enter a Disable notice which is shown to clients who try to access any of the services in the service description, and click **OK**.