### 7.5 Registering a Client to a Security Server

Access rights: Registration Officer

The actions required to register a subsystem of an X-Road member as a Security Server client depend on whether automatic approval of Security Server client registration requests is enabled or disabled (_default_).

When automatic approval of Security Server client registration requests is enabled, the following action must be taken:
- A Security Server client registration request must be sent from the Security Server to the Central Server by the Security Server administrator.

Automatic approval of Security Server client registration requests is disabled by default. In that case, to register a subsystem of an X-Road member as a Security Server client, the following actions must be taken.
- A Security Server client registration request must be sent from the Security Server to the Central Server by the Security Server administrator;
- The requests must be approved or declined by the Central Server administrator.

To approve a request, it can be done either through in the Management request view list or in the Management request details view.

On the approval of the request, follow these steps.
- The request moves to the "Approved" state.
- The client's information is displayed in the "Clients" section of the detailed view of the Security Server to which the client was registered.

To decline a request, it can be done either through in the Management request view list or in the Management request details view.
On the decline of the request
- the request moves to the "Rejected" state.

**Note:** The Security Server administrator is not automatically notified about the rejection of the request. Therefore, they must be notified about the rejection through an external channel, e.g., email. Otherwise, the request remains pending in the "Registration in progress" state on the Security Server.