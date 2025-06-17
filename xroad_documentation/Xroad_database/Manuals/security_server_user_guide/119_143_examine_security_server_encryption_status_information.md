### 14.3 Examine Security Server encryption status information

**Backup encryption status**

The status shows is the backup encryption `enabled` or `disabled`. The Configured key ID list contains all the additional encryption keys that are present in the configuration. If the list is empty, only the system generated default encryption key is used. When the backup encryption is `disabled`, the list is always empty.

The status colors indicate the following:
- **Red indicator** – there's an error with checking the backup encryption status
- **Yellow indicator** – backup encryption is disabled
- **Green indicator** – backup encryption is enabled

**Message log archive encryption status**

The status shows is the message log archive encryption `enabled` or `disabled`. The Grouping rule shows the grouping level (`NONE`, `MEMBER`, `SUBSYSTEM`) of the message log archives.

The list of Member Identifier / Key ID pairs includes a list of members using the Security Server and the encryption key(s) associated with the member when the grouping level is `MEMBER` or `SUBSYSTEM`. When the grouping level is `NONE`, the list is always empty. If no member-specific key is associated with a member, there's a warning icon in the Key ID column. If the Key ID is missing and there's only the warning icon in the Key ID column, the member is using the system generated default encryption key. Instead, if the warning icon is after the Key ID, the member is using the user generated default encryption key (defined using the `archive-default-encryption-key` property). It's strongly recommended to use user generated member-specific encryption keys.

Each member can have multiple member-specific encryption keys configured. If multiple keys are configured for a single member, the key IDs are presented as a comma separated list.

The status colors indicate the following:
- **Red indicator** – there's an error with checking the message log archive encryption status
- **Yellow indicator** – message log archive encryption is disabled
- **Green indicator** – message log archive encryption is enabled
-
**Message log database encryption status**

The status shows is the message log database encryption `enabled` or `disabled`.

The status colors indicate the following:
- **Red indicator** – there's an error with checking the message log database encryption status
- **Yellow indicator** – message log database encryption is disabled
- **Green indicator** – message log database encryption is enabled