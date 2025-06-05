### 2.2 LAST_ARCHIVE_DIGEST

Records the last digest of the archive file. When archiving signatures, the message log links them together using cryptographic hash functions. When creating an archive, the last link is saved in the last_archive_digest table. This makes it possible to continue the hash chain for the next archive file.

The record is created when the first archive file is created. The record is modified every time when an archive file s created. The record is never deleted.