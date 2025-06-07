### 5.1 Availability States of Security Tokens

**Notice that the colors were introduced in version 6.25.0**

To display the availability of tokens, the following colors and labels are used in the "Keys and Certificates" view.

-   **Red** text and a label **Not saved** – the token is available to the Security Server, but it's information has not been saved to the Security Server configuration. For example, a smartcard could be connected to the server, but the certificates on the smartcard may not have been imported to the server. The user cannot interact with the token or it's content.

-   **Red** text and a label **Blocked** – the token is available to the Security Server and it's information has been saved to the Security Server's configuration but the token is unavailable. The user cannot interact with the token or it's content.

-   **Gray** text and a label **Inactive** – the token is not available for the Security Server. The user cannot interact with the token or it's content.

-   **Black** text and a **LOG IN** button – the token is logged out. The user must log in the token before interacting the content.

-   **Black** text and a **LOG OUT** button – the token is logged in. The user can interact with the token and it's content.

**Caution:** The key device's and key's information is automatically saved to the configuration when a certificate associated with either of them is imported to the Security Server, or when a certificate signing request is generated for the key. Similarly, the key device's and key's information is deleted from the Security Server configuration automatically upon the deletion of the last associated certificate and/or certificate signing request.