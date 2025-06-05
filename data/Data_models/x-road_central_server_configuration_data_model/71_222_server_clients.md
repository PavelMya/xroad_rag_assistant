### 2.22 SERVER_CLIENTS

Join table enabling many-to-many relationship between Security Servers and Security Server clients. In other words, associates Security Servers with its clients.

The record is created when a new client is added to the Security Server. It requires approval of a client registration request (see documentation of tables requests and request_processings for details). An X-Road registration officer can do it in the user interface. The record is deleted when a client of a Security Server is deleted in the user interface by an X-Road registration officer. The record is never modified.