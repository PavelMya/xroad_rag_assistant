#### 6.1.1 State Model for Registration Requests

A registration request can be in one of the following states. See Figure 1 for the state diagram.

![State diagram for registration requests](img/ug-cs_state_diagram_for_registration_requests.svg)

Figure 1. State diagram for registration requests

Pending – a registration request has been submitted from a Security Server. From this state, the request can move to the following states.
- “Approved”, if the registration request is approved in the Central Server (see 7.4, 7.5 and 8.3). The association between the objects of the registration request has been created.
- “Rejected”, if the registration request is declined in the Central Server (see 7.4, 7.5 and 8.3).
- “Revoked”.
  - Registration request received from a Security Server are automatically revoked by deletion requests sent from the Security Server for the same object that was submitted for registration with the registration request.

If automatic approval of authentication certificate registration requests, Security Server client registration requests and/or Security Server owner change requests is enabled, the request is approved automatically. Therefore, the request moves directly to Approved state.