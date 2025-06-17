### 4.1 Security Server Client States

The Security Server distinguishes between the following client states.

![](img/ug-ss_saved.svg) **Saved** – the client's information has been entered and saved into the Security Server's configuration (see [4.2](#42-adding-a-security-server-client)), but the association between the client and the Security Server is not registered in the X-Road governing authority. (If the association is registered in the Central Server prior to the entry of data, the client will move to the "Registered" state upon data entry.) From this state, the client can move to the following states:

-   "Registration in progress", if a registration request for the client is submitted from the Security Server (see [4.5.1](#451-registering-a-security-server-client));

-   "Deleted", if the client's information is deleted from the Security Server configuration (see [4.6.2](#462-deleting-a-client)).

![](img/ug-ss_registration_in_progress.svg) **Registration in progress** – a registration request for the client is submitted from the Security Server to the Central Server, but the association between the client and the Security Server is not yet approved by the X-Road governing authority. From this state, the client can move to the following states:

-   "Registered", if the association between the client and the Security Server is approved by the X-Road governing authority (see [4.4.1](#441-registering-a-security-server-client));

-   "Deletion in progress", if a client deletion request is submitted from the Security Server (see [4.6.1](#461-unregistering-a-client)).

![](img/ug-ss_registered.svg) **Registered** – the association between the client and the Security Server has been approved in the X-Road governing authority. In this state, the client can provide and use X-Road services (assuming all other prerequisites are fulfilled). From this state, the client can move to the following states:

-   "Global error", if the association between the client and the Security Server has been revoked by the X-Road governing authority;

-   "Deletion in progress", if a client deletion request is submitted from the Security Server (see [4.6.1](#461-unregistering-a-client)).

-   "Disabling in progress", if a client disabling request is submitted from the Security Server (see [4.7.1](#471-disabling-client-substystem))

![](img/ug-ss_disabled.svg) **Disabled** - The association between the client and the Security server is disabled temporarily (see [4.7](#47-disabling-client-subsystem-temporarily)). From this state the client can move to the following states:

- "Enabling in progress", if client enabling request is submitted from the Security Server (see [4.7.2](#472-enabling-client-subsystem))
- "Deletion in progress", if a client deletion request is submitted from the Security Server (see [4.6.1](#461-unregistering-a-client)).

![](img/ug-ss_disabling_in_progress.svg) **Disabling in progress** - a request is made from Security Server to disable client subsystem temporarily, but it has not propagated yet through global configuration. Once the configuration is propagated, client enters the "Disabled" state.

![](img/ug-ss_enabling_in_progress.svg)  **Enabling in progress** - a request is made from Security Server to enable client subsystem, but it has not propagated yet through global configuration. Once the configuration is propagated, client returns to "Registered" state.

![](img/ug-ss_global_error.svg) **Global error** – the association between the client and the Security Server has been revoked in the Central Server. From this state, the client can move to the following states:

-   "Registered", if the association between the client and the Security Server has been restored in the Central Server (e.g., the association between the client and the Security Server was lost due to an error);

-   "Deleted", if the client's information is deleted from the Security Server's configuration (see [4.6.2](#452-deleting-a-client)).

![](img/ug-ss_deletion_in_progress.svg) **Deletion in progress** – a client deletion request has been submitted from the Security Server. From this state, the client can move to the following state:

-   "Deleted", if the client's information is deleted from the Security Server's configuration (see [4.6.2](#452-deleting-a-client)).

**Deleted** – the client's information has been deleted from the Security Server's configuration.