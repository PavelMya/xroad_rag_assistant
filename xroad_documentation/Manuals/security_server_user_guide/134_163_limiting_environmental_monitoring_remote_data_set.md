### 16.3 Limiting environmental monitoring remote data set

It is possibility to limit what allowed non-owners can request via environmental monotiring data request by changing monitor-env limit-remote-data-set parameter. By changing flag to be true non-owners who are allowed to query environmental monitoring data will get only certificate, operating system and xroad version information. This parameters is set by default false. Security server owner will always get full data set as requested.

## 17 Logs and System Services

**To read logs**, a user must have root user's rights or belong to the `xroad` and/or `adm` system group.