### 2.8 CA_INFOS

CA certificates with additional data that is displayed in the user interface. The CA info can describe either certificate of a top-level CA or an intermediate CA. The record is created when a new top-level CA or an intermediate CA is added in the user interface.
The record is created on two occasions:

1. When a new approved CA is added in the user interface (for details, see documentation of table approved_cas), CA info corresponding to top CA is added.
2. When the certification chain of the approved CA includes intermediate CA-s. Then an X-Road system administrator adds intermediate CA certificate(s) in the user interface.

Accordingly, the record is deleted when either the approved CA is deleted (see also documentation of table approved_cas) or the intermediate CA is deleted in the user interface. The latter can happen when certification chain for approved CA changes. The record is never modified.

#### 2.8.1 Indexes

| Name        | Columns           |
|:----------- |:-----------------:|
| index_ca_infos_on_intermediate_ca_id | intermediate_ca_id |