### 3.3 Message Transport Protocol

The X-Road Message Transport Protocol is used by security server to exchange service requests and service responses.

The protocol is a synchronous RPC style protocol that is initiated by the security server of the service client.

The protocol is based on HTTPS and uses mutual certificate-based TLS authentication. The SOAP/REST messages received from the client and the service provider IS are wrapped in MIME multipart message together with additional security-related data, such as signatures and OCSP responses. See \[[PR-MESSTRANSP](#Ref_PR-MESSTRANSP)\] for details.

This protocol (together with X-Road message protocol) forms the core of the X-Road data exchange. If the involved components are not available, then the data exchange is impossible. X-Road architecture makes possible to improve the availability of the involved components by using redundancy.