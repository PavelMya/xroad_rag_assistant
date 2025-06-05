### 2.5 APPROVED_CAS

Approved certification authority (CA) that is used when verifying authentication and signing certificates. Exactly one top-level CA certificate is associated with each approved CA. Multiple intermediate CA certificates can be associated with each approved CA. The intermediate CA certificates form a hierarchy with top-level CA used as a trust anchor. The intermediate CAs are used for certificate path building and for finding OCSP responders.

New record creation process starts when an X-Road system administrator receives a certificate from a CA which is going to be trusted by the X-Road instance. Having received the certificate, an X-Road system administrator uploads it in the user interface. The record is deleted when for any reason the governing authority of the X-Road instance does not trust the CA any more. Then an X-Road system administrator deletes the approved CA in the user interface. The record is modified when the user changes parameters of the approved CA. Parameters that can be changed, are following:

1. Flag “authentication only”, see also documentation of the column authentication_only of this table.
2. Certificate profile info class name, see also documentation of the column cert_profile_info of this table.