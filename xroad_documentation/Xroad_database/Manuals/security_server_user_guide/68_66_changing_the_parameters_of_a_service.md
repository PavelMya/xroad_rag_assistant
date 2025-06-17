### 6.6 Changing the Parameters of a Service

**Access rights:** [Service Administrator](#xroad-service-administrator)

Service parameters are

-   "Service URL" – the URL where requests targeted at the service are directed;

-   "Timeout (s)" – the maximum duration of a request to the database, in seconds;

-   "Verify TLS certificate" – toggles the verification of the certificate when a TLS connection is established. This option is used for two different scenarios:
    -   Between Security Server and service endpoint.
    -   Between Security Server and service description URL, when metaservices getWsdl or getOpenAPI are used for this subsystem and service. See \[[PR-META](#Ref_PR-META)\] and \[[PR-MREST](#Ref_PR-MREST)\].

To change service parameters, follow these steps.

1.  Navigate to **CLIENTS** tab, click the name of the client containing service you wish to view and click the **SERVICES** tab.

2.  Click the arrow symbol in front of a REST or WSDL service and in the list that is displayed click the service code which you wish to edit.

3.  In the view that opens, configure the service parameters. To apply the selected parameter to all services described in the same service description, select the checkbox adjacent to this parameter in the **Apply to All in WSDL** column. To apply the configured parameters, click **SAVE**.