#### 2.1.1 Indexes

| Name                           | Columns                                    | Partial index details  |
| ------------------------------ |:------------------------------------------:| ----------------------:|
| logrecordpk                    | id                                         | N/A                    |
| LOGRECORD_TIMESTAMPRECORD_fkey | timestamprecord                            | N/A                    |
| ix_logrecord_grouping          | memberclass, membercode, subsystemcode, id | WHERE discriminator::text = 'm'::text AND archived = false AND timestamprecord IS NOT NULL |
| ix_not_archived_logrecord      | id                                         | WHERE discriminator::text = 't'::text AND archived = false |
| ix_not_timestamped_logrecord   | id, discriminator, signaturehash           | WHERE discriminator::text = 'm'::text AND signaturehash IS NOT NULL |
| LOGRECORD_TIMESTAMPRECORD_fkey | timestamprecord                            | N/A                    |
| LOGRECORD_TIMESTAMPRECORD_fkey | timestamprecord                            | N/A                    |
| LOGRECORD_TIMESTAMPRECORD_fkey | timestamprecord                            | N/A                    |
| IX_NOT_ARCHIVED_LOGRECORD      | id                                         | where discriminator = 't' and archived = false |
| IX_NOT_TIMESTAMPED_LOGRECORD   | id, discriminator, signaturehash           | where discriminator = 'm' and signaturehash is not null |