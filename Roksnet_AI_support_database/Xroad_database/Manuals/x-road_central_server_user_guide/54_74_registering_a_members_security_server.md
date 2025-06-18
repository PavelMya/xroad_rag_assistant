### 7.4 Registering a Member's Security Server

Access rights: Registration Officer

The actions required to register an X-Road member's Security Server depend on whether automatic approval of authentication certificate registration requests is enabled or disabled (_default_).

When automatic approval of authentication certificate registration requests is enabled, the following action must be taken:
- An authentication certificate registration request must be sent from the Security Server to the Central Server by the Security Server administrator.

Automatic approval of authentication certificate registration requests is disabled by default. In that case, to register an X-Road member's Security Server, the following actions must be taken.
- An authentication certificate registration request must be sent from the Security Server to the Central Server by the Security Server administrator;
- The requests must be approved or declined by the Central Server administrator.

To approve a request, it can be done either through in the Management request view list or in the Management request details view.

On the approval of the request
- the request moves to the "Approved" state;
- the registered Security Server appears both in the "Owned Servers" section of its owner’s detail view and in the list of Security Servers (in the Security Servers tab);
- the Security Server's owner is added to the global "security-server-owners" group.

Declining a request can be done either in the Management request view list or in the Management request details view.
On the decline of the request
- the request moves to the "Rejected" state.

**Note:** The Security Server administrator is not automatically notified about the rejection of the request. Therefore, they must be notified about the rejection through an external channel, e.g., email. Otherwise, the request remains pending in the "Registration in progress" state on the Security Server.