### 7.2 Web UI Access Control

When the end user is successfully authenticated, least privilege-based access control is enforced for access to system resources whereby the frontend receives information about current user's roles and permissions using /api/user resource. The backend defines authorisation rules based on permissions.

Details on Security Server user roles and associated access controls are described in section 15 Security Server Roles.

In X-Road, access control starts by denying all access by default. Access will not be allowed to all roles if a new resource is added and authorisation is somehow configured incorrectly.