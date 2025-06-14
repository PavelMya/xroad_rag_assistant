### 2.9 CONFIGURATION_SIGNING_KEYS

Signing context (key identifier used by the signer and signing certificate) for signing the global configuration. A signing key belongs to a configuration source. A configuration signing key is used when it is marked as active in the user interface. Technically it is done by designating the key as active key in the configuration_sources table, see also documentation of table configuration_sources.

The record is created when a new key for signing global configuration is needed (either no keys are present or any of present ones cannot be used). Then an X-Road security officer generates a new signing key in the user interface. Non-active configuration signing keys that are no longer necessary can be deleted by an X-Road security officer in the user interface. The record is never modified.

#### 2.9.1 Indexes

| Name        | Columns           |
|:----------- |:-----------------:|
| index_configuration_signing_keys_on_configuration_source_id | configuration_source_id |