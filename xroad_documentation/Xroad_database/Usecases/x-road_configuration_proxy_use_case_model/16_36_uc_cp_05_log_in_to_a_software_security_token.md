### 3.6 UC CP\_05: Log In to a Software Security Token

**System:** Configuration proxy

**Level:** User task

**Component:** Configuration proxy

**Actor:** CP administrator

**Brief Description:** CP administrator logs in to the security token,
making it usable for key generation.

**Preconditions:** The token has not been logged in to.

**Postconditions:** -

**Trigger:** CP administrator wishes to make the functionality of the
token available to the system.

**Main Success Scenario:**

1.  CP administrator selects log in to a software security token.

2.  CP administrator inserts the token PIN code.

3.  System verifies the PIN code is correct and logs in to the token.

**Extensions:**

- 3a. The entered PIN code is incorrect:
    - 3a.1. System displays the error message: “PIN incorrect” and terminates the use case.

**Related information:** -