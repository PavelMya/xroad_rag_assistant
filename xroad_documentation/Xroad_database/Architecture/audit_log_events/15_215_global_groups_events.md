#### 2.1.5 Global Groups Events

The audit log events related to configuration of the X-Road global groups.

| Event                        | Data fields                                                                                                                                                                                                                                                  |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Add global group                 | code - the group code of the added global groupdescription - the description of the added global group                                                                                                                        |
| Edit global group description    | code - the group code of the edited global groupdescription - the new description of the edited global group                                                                                                                  | 
| Delete global group              | code - the group code of the deleted global groupdescription - the description of the deleted global group                                                                                                                    |
| Add members to global group      | code - the group code of the selected global groupdescription - the description of the selected global groupmemberIdentifiers - the list of member identifiers of the members added to the selected global group     |
| Remove members from global group | code - the group code of the selected global groupdescription - the description of the selected global groupmemberIdentifiers - the list of member identifiers of the members removed from the selected global group |