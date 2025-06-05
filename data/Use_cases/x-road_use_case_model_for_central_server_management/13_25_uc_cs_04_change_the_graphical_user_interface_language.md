### 2.5 UC CS\_04: Change the Graphical User Interface Language

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator changes the language of the GUI.

**Preconditions**: -

**Postconditions**: An audit log record for the event has been created.

**Trigger**: CS administrator wants to change the language of the GUI.

**Main Success Scenario**:

1.  CS administrator selects to change the language of the GUI.

2.  System displays the list of supported languages.

3.  CS administrator selects a language.

4.  System saves the CS administrator's choice and displays the GUI in
    the language in the selected language.

5.  System logs the event “Set UI language” to the audit log.

**Extensions**: -

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].