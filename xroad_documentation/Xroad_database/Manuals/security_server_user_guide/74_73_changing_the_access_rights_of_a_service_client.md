### 7.3 Changing the Access Rights of a Service Client

**Access rights:** [Service Administrator](#xroad-service-administrator)

To change the service client's access rights, follow these steps.

1.  Navigate to **CLIENTS** tab, click the name of the client containing service you wish to view and click the **SERVICE CLIENTS** tab.

2.  In the view that opens click the name of a subject (a subsystem, or a local or global group) whose access rights you want to change

3.  In the window that opens, a list of services opened in the Security Server to the selected subject is displayed.

    - To add access rights to a service client, start by clicking **ADD SERVICE**. In the window that opens, select the service(s) that you wish to grant to the subject and click **ADD**. Note that access rights to REST API endpoints can not be added using this view, those need to be added on **SERVICES** tab as described in [7.1](#71-changing-the-access-rights-of-a-service).

    - To remove a single access right to a service from the service client click **Remove** button on the corresponding row and click **YES** in the confirmation dialog.

    - To remove all access rights to a service from the service client click **REMOVE ALL** and click **YES** in the confirmation dialog.

    - Removing service level access rights from the service client also removes all REST API endpoint level access rights to the endpoints of the service. In other words, removing access rights from the service client removes all access rights to a service and its endpoints.