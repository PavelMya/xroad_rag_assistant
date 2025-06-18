### 7.2 Adding a Service Client

**Access rights:** [Service Administrator](#xroad-service-administrator)

The service client view (**CLIENTS** -&gt; **SERVICE CLIENTS**) displays all the service level access rights subjects of the services mediated by this Security Server client. In other words, if an X-Road subsystem or group has been granted a service level access right to a service of this client, then the subject is shown in this view. Subjects that have been granted an endpoint level access right to a REST service, are not shown in the view.

To add a service client, follow these steps.

1.  Navigate to **CLIENTS** tab, click the name of the client containing service you wish to view and click the **SERVICE CLIENTS** tab.

2.  Click **ADD SUBJECT**. In the following wizard that opens

    1. Select a subject (a subsystem, or a local or global group) to which you want to grant access rights to and click **NEXT**

    2. Select service(s) whose access rights you want to grant to the selected subject. Click **ADD SELECTED** to grant access rights to the selected services to this subject. Note that access rights to REST API endpoints can not be added using this view, those need to be added on **SERVICES** tab as described in [7.1](#71-changing-the-access-rights-of-a-service).

The subject is added to the list of service clients, after which the service clients view is displayed.