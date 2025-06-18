### 6.7 Managing REST Endpoints

**Access rights:** [Service Administrator](#xroad-service-administrator)

REST type service descriptions can contain API endpoints. The purpose of the endpoints is more fine-grained access control. More about that in chapter [7 Access Rights](#7-access-rights).

When URL type of the REST service is an OpenAPI 3 description, endpoints are parsed from the service description automatically. These endpoints cannot be manually updated or deleted. Additionally manual endpoints can be added as needed. When URL type is REST API base path, all the endpoints need to be created manually. Manually created endpoints can also be edited and deleted as needed.

To create API endpoint manually, follow these steps

1.  Navigate to **CLIENTS** tab, click the name of the client containing service you wish to view and click the **SERVICES** tab.

2.  Click the arrow symbol in front of a REST service and click the service code that is displayed.

3.  Click the **ENDPOINTS** tab and in the following view click **ADD ENDPOINTS**.

4.  In the dialog that opens fill in the HTTP Request method and path for the endpoint and click **ADD**