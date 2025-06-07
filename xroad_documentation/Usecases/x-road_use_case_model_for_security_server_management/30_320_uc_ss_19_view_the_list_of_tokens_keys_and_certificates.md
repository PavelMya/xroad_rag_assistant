### 3.20 UC SS\_19: View the List of Tokens, Keys and Certificates

**System**: Security server

**Level**: User task

**Component:** Security server

**Actors:** SS administrator

**Brief Description**: SS administrator views the list of tokens, keys,
certificates and certificate signing request notices.

**Preconditions**: -

**Postconditions**: The list of tokens, keys and certificates has been
displayed to SS administrator.

**Trigger**: SS administrator wants to view the list of tokens, keys and
certificates.

**Main Success Scenario**:

1.  SS administrator selects to view the list of tokens, keys and
    certificates that are saved in the system configuration and/or
    visible to the system.

2.  System displays the list of tokens, keys and certificates.

    For each token, the following information is displayed:
    
    -   the friendly name of the token. For tokens that are not saved in the system configuration, and for tokens that are saved in the system configuration but the friendly name of the token has not been changed, the friendly name is displayed in the format &lt;module ID&gt;-&lt;serial number&gt;-&lt;label&gt;-&lt;slot index&gt;;
    
    -   the status of the token marked as 'BLOCKED', when the token is blocked.
    
    For each key, the following information is displayed:
    
    -   the friendly name of the key. For keys that are not saved in the system configuration, and for keys that are saved in the system configuration but the friendly name of the key has not been set, the label or identifier (if the label is not set) of the key is displayed as the friendly name;
    
    -   the type of the key ('sign' for keys that are used for signing; 'auth' for keys that are used for authentication; '?' for keys the usage is undefined).
    
    For each certificate, the following information is displayed:
    
    -   the common name (CN) of the issuer of the certificate;
    
    -   the serial number of the certificate;
    
    -   the identifier of the X-Road member the certificate was issued for in the format *member class : member code* for signing certificates (if a certificate has not been imported to a hardware token the identifier of the X-Road member is not displayed);
    
    -   the last OCSP response for certificates in the registered state, or the disabled status notice if the certificate is disabled;
    
    -   the expiry date of the certificate;

    -   the registration state of the certificate (if a certificate has not been imported to a hardware token the registration state is not displayed).

    For each certificate signing request notice, the following information is displayed:

    -   the identifier of the X-Road member the certificate signing request was generated for in the format *member class : member code* (only displayed for signing CSRs)*.*

    The SS administrator has a possibility to choose amongst the following actions:

    -   view the details of a token: 3.21;
    
    -   view the details of a key: 3.22;
    
    -   view the details of a certificate: 3.10;
    
    -   log in to a token: 3.25 and 3.26;
    
    -   log out of a token: 3.27 and 3.28 ;
    
    -   generate a key on a security token: 3.29;
    
    -   generate a certificate signing request: 3.30;
    
    -   import a certificate: 3.31 and 3.32;
    
    -   activate a certificate: 3.33;
    
    -   disable a certificate: 3.34;
    
    -   send an authentication certificate registration request: 3.35;
    
    -   delete a key: 3.36, 3.37 and 3.38;
    
    -   unregister an authentication certificate: 3.39;
    
    -   delete a certificate signing request notice: 3.40;
    
    -   delete a certificate: 3.40, and 3.41.

**Extensions**: -

**Related information**:

-   The information about tokens, keys and certificates configured for
    the system is stored in the file /etc/xroad/signer/keyconf.xml.