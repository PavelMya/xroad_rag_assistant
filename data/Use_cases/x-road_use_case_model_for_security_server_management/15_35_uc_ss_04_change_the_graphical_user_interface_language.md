### 3.5 UC SS\_04: Change the Graphical User Interface Language

**System**: Security server

**Level**: User task

**Component:** Security server

**Actor**: SS administrator

**Brief Description**: SS administrator changes the language of the GUI.

**Preconditions**: -

**Postconditions**:

-   The language of the GUI has been changed.

-   An audit log record for the event is created.

**Trigger**: SS administrator wishes to change the language of the GUI.

**Main Success Scenario**:

1.  SS administrator selects to change the language of the GUI.

2.  System displays the list of supported languages.

3.  SS administrator selects a language.

4.  System saves the SS administrator's choice and displays the GUI in
    the language the SS administrator selected.

5.  System logs the event “Set UI language” to the audit log.

**Extensions**: -

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].