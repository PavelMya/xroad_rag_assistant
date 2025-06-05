#### 3.3.1 Registering an Authentication Certificate

**Access rights:** [Security Officer](#xroad-security-officer)

The Security Server's registration request is signed in the Security Server with the server owner's signing key and the server's authentication key. Therefore, ensure that the corresponding certificates are imported to the Security Server and are in a usable state (the tokens holding the keys are in logged in state and the OCSP status of the certificates is "good").

To submit an authentication certificate registration request, follow these steps.

1.  In the **Navigation tabs**, select **KEYS AND CERTIFICATES**.

2.  Show more details about a token by clicking the caret next to the token name.

3.  Click **Register** at the end of the desired certificate row. Note that the certificate must be in "Saved" state.

4.  In the dialog that opens, enter the Security Server's public DNS name or its external IP address and click **ADD**.

On submitting the request, the message "Certificate registration request successful" is displayed, and the authentication certificate's state is set to "Registration in process".

After the X-Road governing authority has accepted the registration, the registration state of the authentication certificate is set to "Registered" and the registration process is completed.

**Note:** If the registration request is rejected by the X-Road governing authority, no automatic notification is sent to the Security Server administrator and the authentication certificate remains in the "Registration in process" state on the Security Server. The X-Road governing authority must notify the Security Server administrator about the rejection of the request through an external channel, e.g., email.

After a rejected authentication certificate registration request, complete the following steps to send a new authentication certificate registration request:

1.  Unregister the authentication certificate (see [5.6.1](#561-unregistering-an-authentication-certificate)).
2.  Delete the authentication certificate (see [5.6.2](#562-deleting-a-certificate-or-a-certificate-signing-request-notice)).
3.  Import an authentication certificate from the local file system (see [3.2.3](#323-importing-an-authentication-certificate-from-the-local-file-system)).
4.  Register the authentication certificate (see [3.3.1](#331-registering-an-authentication-certificate)).