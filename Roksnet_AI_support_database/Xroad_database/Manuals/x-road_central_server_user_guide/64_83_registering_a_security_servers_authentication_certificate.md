### 8.3 Registering a Security Server's Authentication Certificate

Access rights: Registration Officer

The actions required to register a Security Server's authentication certificate depend on whether automatic approval of authentication certificate registration requests is enabled or disabled (_default_).

When automatic approval of authentication certificate registration requests is enabled, the following action must be taken:
- An authentication certificate registration request must be sent from the Security Server to the Central Server by the Security Server administrator.

Automatic approval of authentication certificate registration requests is disabled by default. In that case, to register a Security Server's authentication certificate, the following actions must be taken.
- An authentication certificate registration request must be sent from the Security Server to the Central Server by the Security Server administrator;
- The requests must be approved or declined by the Central Server administrator.

To approve/decline a request, it can be done either through in the Management request view list or in the Management request details view.

Upon approving the request
- the request moves to the "Approved" state;
- the registered authentication certificate appears in the Security Server's detail view, in the "Authentication Certificates" section.

To decline the request
- the request moves to the "Rejected" state;