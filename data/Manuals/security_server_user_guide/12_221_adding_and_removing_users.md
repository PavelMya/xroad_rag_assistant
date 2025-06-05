#### 2.2.1 Adding and Removing Users

To add a new user, enter the command:

    adduser username

To grant permissions to the user you created, add it to the corresponding system groups, for example:

    adduser username xroad-security-officer
    adduser username xroad-registration-officer
    adduser username xroad-service-administrator
    adduser username xroad-system-administrator
    adduser username xroad-securityserver-observer

To remove user permission, remove the user from the corresponding system group, for example:

    deluser username xroad-security-officer

Modified user permissions are applied only after a user does a new login.

To remove a user, enter:

    deluser username