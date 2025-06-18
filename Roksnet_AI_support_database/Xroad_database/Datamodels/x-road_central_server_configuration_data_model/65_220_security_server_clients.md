### 2.20 SECURITY_SERVER_CLIENTS

Contains X-Road members or subsystems. The subject that can be associated with a Security Server. There are two types of associations:

- X-Road members can be Security Server owners. Members cannot provide and consume regular X-Road services (but can consume the X-Road management services).
- X-Road subsystems can be Security Server clients and can provide or consume X-Road services.

The way records are added depends on whether the record holds a member or a subsystem:

- members can be added in the user interface by the X-Road registration officer;
- subsystem can be added in the user interface by the X-Road registration officer and are also added when a client registration request for registering a subsystem that does not previously exist in this table is approved. See also documentation for tables requests and request_processings.

The record is modified when the X-Road registration officer edits the member's name in the user interface.

The record can be deleted in the user interface by an X-Road registration officer.