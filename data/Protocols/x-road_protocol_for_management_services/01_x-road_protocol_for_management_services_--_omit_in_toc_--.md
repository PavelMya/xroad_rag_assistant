# X-Road: Protocol for Management Services <!-- omit in toc -->

**Technical Specification**

Version: 1.19  
Doc. ID: PR-MSERV

| Date       | Version | Description                                                                  | Author               |
|------------|---------|------------------------------------------------------------------------------|----------------------|
| 19.08.2015 | 0.1     | Initial version                                                              | Martin Lind          |
| 28.08.2015 | 0.2     | Added comments and made editorial changes                                    | Margus Freudenthal   |
| 03.09.2015 | 0.3     | Re-structuring and accuracy improvements                                     | Martin Lind          |
| 13.09.2015 | 0.4     | Made editorial changes                                                       | Margus Freudenthal   |
| 16.09.2015 | 0.5     | Correct example message for authentication certificate registration request  | Martin Lind          |
| 17.09.2015 | 0.6     | Improvements for example messages and referential improvements               | Martin Lind          |
| 17.09.2015 | 0.7     | Improvements for Schema fragments                                            | Martin Lind          |
| 18.09.2015 | 0.8     | Updating Schema in the WSDL                                                  | Martin Lind          |
| 21.09.2015 | 1.0     | Editorial changes made                                                       | Imbi Nõgisto         |
| 21.09.2015 | 1.1     | Document renamed                                                             | Imbi Nõgisto         |
| 01.10.2015 | 1.2     | Field *requestId* added and redundant elements removed                       | Martin Lind          |
| 05.10.2015 | 1.3     | Updated example messages                                                     | Martin Lind          |
| 06.10.2015 | 1.4     | Correct header fields for WSDL                                               | Martin Lind          |
| 17.10.2015 | 1.6     | Editorial changes related to *requestId* field                               | Margus Freudenthal   |
| 28.10.2015 | 1.7     | Complete X-Road identifiers schema added                                     | Siim Annuk           |
| 30.10.2015 | 1.8     | Header field *userId* removed from management services WSDL                  | Kristo Heero         |
| 11.12.2015 | 1.9     | Corrected documentation about registering only subsystems                    | Siim Annuk           |
| 07.06.2017 | 1.10    | Additional signature algorithms supported                                    | Kristo Heero         |
| 06.03.2018 | 1.11    | Added terms section, term doc reference and link, fixed references           | Tatu Repo            |
| 06.02.2019 | 1.12    | Update *clientReg* message description                                       | Petteri Kivimäki     |
| 03.06.2019 | 1.13    | Add ownerChange management service                                           | Ilkka Seppälä        |
| 29.06.2019 | 1.14    | Rename *newOwner* element to *client* in ownerChange management service      | Petteri Kivimäki     |
| 10.05.2023 | 1.15    | Security Categories removed.                                                 | Justas Samuolis      |
| 20.11.2023 | 1.16    | Add *addressChange* management service                                       | Justas Samuolis      |
| 11.12.2023 | 1.17    | *clientDisable* and *clientEnable* services                                  | Madis Loitmaa        |
| 07.03.2025 | 1.18    | Add *clientRename* management service and update *clientReg* service         | Ovidijus Narkevičius |
| 29.04.2025 | 1.19    | Add *maintenanceModeEnable* and *maintenanceModeDisable* management services | Ovidijus Narkevičius |