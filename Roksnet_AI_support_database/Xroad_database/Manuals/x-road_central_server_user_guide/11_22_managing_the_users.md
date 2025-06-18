### 2.2 Managing the Users

During the installation, a super user equipped with all the roles is created. You can create additional users that have restricted rights. User management is carried out in root user's permissions using the command line.

To add a new user, issue the command:

`adduser username`

To grant permissions to the user you created, add it to the corresponding system groups, for example:

`adduser username xroad-registration-officer`
`adduser username xroad-system-administrator`
`adduser username xroad-security-officer`

To remove a user’s permission, remove the user from the corresponding system group, for example:

`deluser username xroad-registration-officer`

To remove a user, enter:

`deluser username`