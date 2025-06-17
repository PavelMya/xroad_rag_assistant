### 6.1 Registration Requests

As the registration of associations in the X-Road governing authority is security-critical, the following measures are applied to increase security by default:

- The registration request must be submitted to the X-Road Central Server through the Security Server. Manual approval is still required by default.
- The association must be approved by the X-Road governing authority.

There are three types of registration requests:

- authentication certificate registration request (see Sections 7.4 and 8.3);
- Security Server client registration request (see Section 7.5);
- Security Server owner change request (see Section 7.7)

It is possible to streamline the registration process of authentication certificates and Security Server clients by enabling automatic approval.

- authentication certificate registration requests
  - When automatic approval is enabled, it is enough to submit an authentication certificate registration request to the X-Road Central Server through the Security Server, and the request will be automatically approved immediately.
  - Automatic approval is applied to existing members only.
  - By default, automatic approval of authentication certificate registration requests is disabled. It can be enabled by setting the `auto-approve-auth-cert-reg-requests` property value to `true` on Central Server.
- Security Server client registration requests
  - When automatic approval is enabled, it is enough to submit a Security Server client registration request to the X-Road Central Server through the Security Server, and the request will be automatically approved immediately.
  - Automatic approval is applied to existing members only. In addition, automatic approval is applied only if the client registration request has been signed by the member owning the subsystem to be registered as a Security Server client.
  - By default, automatic approval of Security Server client registration requests is disabled. It can be enabled by setting the `auto-approve-client-reg-requests` property value to `true` on Central Server.
- Security Server owner change requests
  - When automatic approval is enabled, it is enough to submit a Security Server owner change request to the X-Road Central Server through the Security Server, and the request will be automatically approved immediately.
  - Automatic approval is applied to existing members only.
  - By default, automatic approval of Security Server owner change requests is disabled. It can be enabled by setting the `auto-approve-owner-change-requests` property value to `true` on Central Server.