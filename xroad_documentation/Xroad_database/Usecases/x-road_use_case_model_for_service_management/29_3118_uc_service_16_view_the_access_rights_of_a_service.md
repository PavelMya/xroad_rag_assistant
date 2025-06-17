#### 3.1.18 UC SERVICE\_16: View the Access Rights of a Service

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator views the access rights of a
security server client's service.

**Preconditions**: -

**Postconditions**: The access rights of the security server client's
service have been displayed to SS administrator.

**Trigger**: SS administrator wants to view the access rights of a
security server client's service.

**Main** **Success** **Scenario**:

1.  SS administrator selects to view the access rights of a security
    server client's service.

2.  System displays the list of service clients that have been given
    access rights to the service. For each service client, the following
    information is displayed:

    -   the name of the X-Road member responsible for the subsystem if
        the service client is a subsystem, or the description of the
        group, if the service client is an access rights group;

    -   the X-Road identifier of the service client;

    -   the date of when the access right to the service was granted.

    The SS administrator has a possibility to choose amongst the following actions:

    -   add access rights to the service: 3.1.19;
    
    -   remove subjects from the access rights list of the service: 3.1.20.

**Extensions**: -

**Related** **information**: -