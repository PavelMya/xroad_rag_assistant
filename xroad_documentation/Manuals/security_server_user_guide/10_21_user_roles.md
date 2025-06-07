### 2.1 User Roles

Security servers support the following user roles:

-   **Security Officer** (`xroad-security-officer`) is responsible for the application of the security policy and security requirements, including the management of key settings, keys, and certificates.

-   **Registration Officer** (`xroad-registration-officer`) is responsible for the registration and removal of Security Server clients.

-   **Service Administrator** (`xroad-service-administrator`) manages the data of and access rights to services

-   **System Administrator** (`xroad-system-administrator`) is responsible for the installation, configuration, and maintenance of the Security Server.

-   **Security Server Observer** (`xroad-securityserver-observer`) can view the status of the Security Server without having access rights to edit the configuration. This role can be used to offer users read-only access to the Security Server admin user interface.

One user can have multiple roles and multiple users can be in the same role. Each role has a corresponding system group, created upon the installation of the system.

Henceforth each applicable section of the guide indicates, which user role is required to perform a particular action. For example:

**Access rights:** [Security Officer](#xroad-security-officer)

If the logged-in user does not have a permission to carry out a particular task, the button that would initiate the action is hidden (and neither is it possible to run the task using its corresponding keyboard combinations or mouse actions). Only the permitted data and actions are visible and available to the user.

### 2.2 Managing the Users

User management is carried out on the command line in root user permissions.