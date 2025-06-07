#### 2.2.1 UC GCONF\_01: View a Configuration Source 

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator views the information about a
configuration source provided by the central server.

**Preconditions**: -

**Postconditions**: The configuration source information has been
displayed to CS administrator.

**Trigger**: CS administrator wishes to view the configuration source
information.

**Main Success Scenario**:

1.  CS administrator selects to view a configuration source.

2.  System displays a configuration source provided by the central
    server. The following information is displayed.

    -   Type of the configuration source (internal/external).

    -   The SHA-224 hash value of the configuration anchor.

    -   The generation date and time (UTC) of the configuration anchor.

    -   The configuration download URL – address from where the
        configuration directory provided by this source can be
        downloaded. The system composes the download URL by adding
        */internalconf* or */externalconf*
        (depending on the type of the configuration source) to the
        address of the central server.

    -   List of configuration signing keys. For each key, the following
        information is displayed:

        -   the identifier of the device holding the key,

        -   the identifier of the key,

        -   the key generation date and time.

    The key currently used to sign configuration is displayed is
    emphasised. Only the keys that have a certificate associated with them are displayed.

    -   List of configuration part files distributed by the source. For each
     configuration part, the following information is displayed:

    -   name of the configuration part file,

    -   content identifier of the configuration part,

    -   date and time when the configuration part file was last updated.
    
    The following user action options are displayed:

    -   download the configuration source anchor file: 2.2.2;
    
    -   re-create the configuration source anchor file: 2.2.3;
    
    -   add a configuration signing key: 2.2.11;
    
    -   delete a configuration signing key: 2.2.13;
    
    -   activate a configuration signing key: 2.2.12;
    
    -   log in to a security token holding a configuration signing key:
        2.2.7 or 2.2.8;
    
    -   log out of a security token holding a configuration signing key:
        2.2.9 or 2.2.10;
    
    -   download a configuration part file: 2.2.6;
    
    -   upload an optional configuration part file: 2.2.5, in case the
        optional part is described in the system: 2.2.4.

**Extensions**: -

**Related information**: -