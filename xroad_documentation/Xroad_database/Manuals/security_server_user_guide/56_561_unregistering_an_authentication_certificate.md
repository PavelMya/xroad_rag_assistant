#### 5.6.1 Unregistering an Authentication Certificate

**Access rights:** [Security Officer](#xroad-security-officer)

To unregister an authentication certificate, follow these steps.

1.  In the **Navigation tabs**, select **KEYS AND CERTIFICATES**.

2.  Show more details about a token by clicking the caret next to the token name.

3.  Click on an authentication certificate that is in the state "Registered" or "Registration in progress".

    3.1 In the opening **Certificate** dialog, click **UNREGISTER**.

    Next, an authentication certificate deletion request is automatically sent to the X-Road Central Server, upon the receipt of which the associated authentication certificate is deleted from the Central Server. If the request was successfully sent, the message "Certificate unregistration request sent successfully" is displayed and the authentication certificate is moved to the "Deletion in progress" state.

A registered authentication certificate can be deleted from the Central Server without sending a deletion request through the Security Server. In this case, the Security Server's administrator must transmit a request containing information about the authentication certificate to be deleted to the Central Server's administrator. If the authentication certificate has been deleted from the Central Server without a deletion request from the Security Server, the certificate is shown in the "Global error" state in the Security Server.