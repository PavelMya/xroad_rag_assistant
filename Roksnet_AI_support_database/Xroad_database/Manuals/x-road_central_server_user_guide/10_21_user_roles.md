### 2.1 User Roles

The Central Server supports the following user roles:

- **Registration Officer** (`xroad-registration-officer`) is responsible for handling the information about X-Road members.
- **System Administrator** (`xroad-system-administrator`) is responsible for the installation, configuration, and maintenance of the Central Server.
- **Security Officer** (`xroad-security-officer`) is responsible for the application of the security policy and security requirements.

One user can have multiple roles, and multiple users can fulfill the same role. Each role has a corresponding system group, created upon the installation of the system. The system user names are used for logging in to the user interface of the Central Server.

The document indicates in sections similar to the following example, which user role is required for performing a particular action in the user interface. For example

`Access rights: System Administrator`

Caution: If the logged-in user does not have a permission to carry out a task, the button that initiates the action is hidden (and neither is it possible to run the task using its corresponding keyboard combinations or mouse actions). Only the permitted information and actions are visible and available to the user.