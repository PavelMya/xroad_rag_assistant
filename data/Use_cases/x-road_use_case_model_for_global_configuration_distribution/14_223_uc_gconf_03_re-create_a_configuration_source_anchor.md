#### 2.2.3 UC GCONF\_03: Re-Create a Configuration Source Anchor

**System**: Central server

**Level**: User task

**Component:** Central server

**Actor**: CS administrator

**Brief Description**: CS administrator re-creates the configuration
anchor of a configuration source. Under normal system behaviour,
generation of the anchor file by CS administrator is unnecessary, as the
system generates the anchor file automatically when needed. The
re-creation allows to recover from system malfunctions.

**Preconditions**: -

**Postconditions**: An audit log record for the event has been created.

**Trigger**: CS administrator wishes to re-create the configuration
anchor for a configuration source.

**Main Success Scenario**:

1.  CS administrator selects to re-create the configuration anchor.

2.  System generates the configuration anchor: 2.2.17.

3.  System displays the message: “Internal configuration anchor
    generated successfully” or “External configuration anchor generated
    successfully, depending on the configuration source the anchor was
    re-created for.

4.  System logs the event “Re-create internal configuration anchor” or
    “Re-create external configuration anchor”, depending on which
    configuration source the anchor file was re-created for, to the
    audit log.

**Extensions**:

- 2a. The process of generating the anchor terminated with an error message.
    - 2a.1. System displays the error message: “X configuration anchor generation failed: Y”, where “X” is the type of the configuration source (internal or external) and “Y” is the reason for the failure.
    - 2a.2. System logs the event “Re-create internal configuration anchor failed” or “Re-create external configuration anchor failed”, depending on the configuration source, to the audit log. Use case terminates.

**Related information**:

-   The audit log is located at /var/log/xroad/audit.log. The data set
    of audit log records is described in the document “X-Road: Audit Log
    Events” \[[SPEC-AL](#Ref_SPEC-AL)\].