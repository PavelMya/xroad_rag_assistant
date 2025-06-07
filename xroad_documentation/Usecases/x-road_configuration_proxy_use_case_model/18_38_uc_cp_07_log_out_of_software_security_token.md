### 3.8 UC CP\_07: Log Out of Software Security Token

**System:** Configuration proxy

**Level:** User task

**Component:** Configuration proxy

**Actor:** CP administrator

**Brief Description:** CP administrator logs out of a software security
token.

**Preconditions:**

-   The software security token is holding one or more configuration
    signing keys.

-   The software security token is logged in to.

**Postconditions:** The token is logged out of. The system cannot use
the keys on the token for signing configuration.

**Trigger:** CS administrator wishes to log out of a software security
token.

**Main Success Scenario:**

1.  CP administrator selects to log out of a token.

2.  System logs out of the token.

**Extensions: -**

**Related information**: -