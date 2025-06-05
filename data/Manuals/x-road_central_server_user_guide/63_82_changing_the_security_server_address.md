### 8.2 Changing the Security Server Address

Access rights: Registration Officer

By default, the Security Server's address is provided in the registration request of the authentication certificate sent from the Security Server. The address must be changed if it was not set when the request was submitted or if it is no longer valid.

There are several reasons why setting the Security Server’s address matters.
- The services that are relayed through a Security Server become available once the Security Server’s address is set.
- By registering the addresses of Security Servers, the service clients are certain to receive a response to their queries in a reasonable time, even if the relaying Security Server is overloaded with service requests (e.g., the requests from addresses belonging to registered Security Servers are served before requests coming from unknown addresses).

The request can be submitted through the Security Server or changed in the Central Server.

To change the Security Server address from the Central Server, follow these steps.
1. In the Security Servers tab, select the Security Server whose address you wish to change and click server code.
2. In the view that opens, locate the "Address" section and click Edit adjacent to the "Address" field.
3. Enter the Security Server's address and click Save.