### 2.4 Managing API Keys

API keys are used to authenticate API calls to Central Server's management REST API. API keys are associated with roles that define the permissions granted to the API key. If an API key is lost, it can be revoked.

In addition to the user roles, an API key can be added to the Management Services role. The Management Services role is used for registration and management services to authenticate and successfully communicate with the management REST API. Registration and management services are automatically configured with valid API keys during installation.

Access rights: System Administrator

To create API key, follow these steps.

1. In the Navigation tabs, select Settings --> API Keys, click Create API key.
2. In the window that opens, check selected roles checkbox and then click Next.
3. In the next window click Create Key.
4. Copy and save the API key in a secure place. _The API key is visible only at the time of key generation. It will not be presented again and cannot be retrieved later_.
5. Click Finish.

To edit API key related roles, follow these steps.

1. In the Navigation tabs, select Settings --> API Keys.
2. Select a API key and click Edit.
3. In the window that opens, check selected roles checkbox and click Save.

To revoke API key from roles, follow these steps.

1. In the Navigation tabs, select Settings --> API Keys.
2. Select a API key and click Revoke key.
3. Confirm the revoking by clicking Yes.