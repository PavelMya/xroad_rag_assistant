### 2.2 ANCHOR_URLS

URL pointing to a configuration source that is described by a trusted anchor. Anchor URL is HTTP URL that can be used to download signed configuration.

The record is created or modified exactly the same way as described in the documentation of table anchor_url_certs. The record is never modified.

#### 2.2.1 Indexes

| Name        | Columns           |
|:----------- |:-----------------:|
| index_anchor_urls_on_trusted_anchor_id | trusted_anchor_id |