### 2.17 OCSP_INFOS

Information about OCSP service that is offered by a particular CA. See also documentation of table approved_cas.

The record is created when a new OCSP responder needs to be registered for either top CA or intermediate CA of approved CA (see also documentation of tables approved_cas and ca_infos). Then an X-Road system administrator adds new OCSP info in the user interface. The record can be modified or deleted in the user interface.

#### 2.17.1 Indexes

| Name        | Columns           |
|:----------- |:-----------------:|
| index_ocsp_infos_on_ca_info_id | ca_info_id |