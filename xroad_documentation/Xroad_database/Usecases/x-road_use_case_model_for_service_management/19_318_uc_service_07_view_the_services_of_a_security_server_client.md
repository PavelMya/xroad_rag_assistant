#### 3.1.8 UC SERVICE\_07: View the Services of a Security Server Client

**System**: Security server

**Level**: User task

**Component**: Security server

**Actors**: SS administrator

**Brief** **Description**: SS administrator views the list of a security
server client's services.

**Preconditions**: -

**Postconditions**: The list of a security server client's services has
been displayed to SS administrator.

**Trigger**: SS administrator wants to view the list of a security
server client's services.

**Main** **Success** **Scenario**:

1.  SS administrator selects to view the list of a security server
    client's services.

2.  System displays the list of services. For each service, the
    following information is displayed:

    -   the code and the version of the service (formatted as
        'code.version');

    -   the number of subjects that have access rights to the service;

    -   the title of the service;

    -   the URL of the service;

    -   the connection type for accessing the service (http, https or
        https with no authentication);

    -   the service timeout value in seconds;

    -   the date of when the WSDL containing the description of the
        service was last refreshed.

    The SS administrator has a possibility to choose amongst the following actions:

    -   view the access rights of a service: 3.1.18;
    
    -   edit the timeout value of a service: 3.1.23;
    
    -   edit the address of a service: 3.1.21;
    
    -   set the option to verify internal TLS certificate 3.1.22;
    
    -   apply the parameter value of one service to all the services in the
        WSDL or REST: 3.1.24.

**Extensions**: -

**Related** **information**: -