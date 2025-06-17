### 2.1 ANCHOR_URL_CERTS

Certificate belonging to a configuration source that is represented in database by an anchor URL. The certificates are used to verify signed configuration downloaded from a given URL.

The record is created when an X-Road security officer has received trusted anchor from federation partner and uploads it in the user interface. The record is deleted when the federation contract between two X-Road instances has come to an end and an X-Road security officer deletes the anchor associated with the record in the user interface. The record is never modified. Records in tables trusted_anchors and anchor_urls are created and deleted in exactly the same way. See also documentation of these tables.

#### 2.1.1 Indexes

| Name        | Columns           |
|:----------- |:-----------------:|
| index_anchor_url_certs_on_anchor_url_id | anchor_url_id |