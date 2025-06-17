### 4.7 Security

Secure REST services should only provide HTTPS endpoints. This concerns both the consumer Security Server and the
provider service. HTTPS protects authentication credentials in transit, for example passwords, API keys or JSON Web
Tokens. It also allows clients to authenticate the service and guarantees integrity of the transmitted data.

It is RECOMMENDED to use mutually authenticated client-side certificates in the connections between the Security Server
and information systems - both service consumers and service providers, to provide additional protection for highly
privileged web services. Security Server MUST support mutually authenticated client-side certificates on both consumer
and provider side. Use of JWT tokens as an authentication method between the Security Server and information system is
not supported. Instead, sending JWT tokens in HTTP headers from the service consumer to the service provider is
supported - X-Road passes the headers unmodified.