#### 11.1.6 Archive Files

Archive files (ZIP containers) are located in the directory specified by the configuration parameter `archive-path`. File names are in the format `mlog[-grouping]-X-Y-Z.zip[.gpg]`, where X is the timestamp (UTC time in the format `YYYYMMDDHHmmss`) of the first message log record, Y is the timestamp of the last message log record (records are processed in chronological order) and Z is the first 16 characters of the last linking info digest entry. If grouping is enabled, [-grouping] is a (possibly truncated and filename safe) member identifier. If encryption is enabled, the `[.gpg]` suffix is added. Creating archive files is deterministic -- given the same input (grouping, message records, previous archive linking info digest), the output (file name and contents) is the same after possible encryption is removed.

The most basic example of an archive file name when the encryption and grouping are switched off:

    mlog-20210901100858-20210901100905-95b1f27097524105.zip

When the archive encryption switched on:

    mlog-20210901101923-20210901101926-95b1f27097524105.zip.gpg

Switching on archive grouping by member produces the following:

    mlog-INSTANCE_CLASS_CODE-20210901102251-20210901102254-95b1f27097524105.zip.gpg

Finally, switching to archive grouping by subsystem gives:

    mlog-INSTANCE_CLASS_CODE_CONSUMERSUBSYSTEM-20210901102521-20210901102524-95b1f27097524105.zip.gpg
    mlog-INSTANCE_CLASS_CODE_PROVIDERSUBSYSTEM-20210901102521-20210901102524-b1f27097524105ac.zip.gpg