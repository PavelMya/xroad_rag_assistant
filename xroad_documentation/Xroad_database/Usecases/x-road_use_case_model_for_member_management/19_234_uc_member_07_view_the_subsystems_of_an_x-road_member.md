#### 2.3.4 UC MEMBER\_07: View the Subsystems of an X-Road Member

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator views the list of an X-Road member's subsystems.

**Preconditions**: -

**Postconditions**: The list of X-Road member's subsystems has been displayed to CS administrator.

**Trigger**: -

**Main Success Scenario**:

1.  CS administrator selects to view the subsystems of an X-Road member.

2.  System displays the list of subsystems of the member. The following information is displayed for each subsystem:

    -   the code of the subsystem;

    -   the code of the security server where the subsystem is registered as the security server client.

    The following user action options are displayed:

    -   add a subsystem to the X-Road member [2.3.11](#2311-uc-member_56-add-a-subsystem-to-an-x-road-member);

    -   delete a subsystem that is not registered as a client to any security servers: [2.3.12](#2312-uc-member_14-delete-an-x-road-members-subsystem).

**Extensions**: -

**Related information**: -