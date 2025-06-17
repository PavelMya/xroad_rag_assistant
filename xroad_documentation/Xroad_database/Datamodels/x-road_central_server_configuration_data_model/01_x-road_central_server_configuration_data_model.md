# X-Road: Central Server Configuration Data Model

Version: 1.16
Doc. ID: DM-CS

| Date       | Version | Description                                                                      | Author               |
|------------|---------|----------------------------------------------------------------------------------|----------------------|
| 15.06.2015 | 0.1     | Initial version                                                                  | Martin Lind          |
| 30.06.2015 | 0.2     | Comments and revisions                                                           | Margus Freudenthal   |
| 09.07.2015 | 0.3     | Rearrangements for consistency                                                   | Martin Lind          |
| 28.08.2015 | 0.4     | Corrections according to feedback to first 7 tables                              | Martin Lind          |
| 01.09.2015 | 0.5     | Better explanations for modifications to all tables                              | Martin Lind          |
| 09.09.2015 | 0.6     | Made minor editorial changes                                                     | Margus Freudenthal   |
| 16.09.2015 | 0.7     | Added the descriptions of the fields and procedures related to high availability | Marju Ignatjeva      |
| 21.09.2015 | 1.0     | Editorial changes made                                                           | Imbi Nõgisto         |
| 16.10.2015 | 1.1     | Field cert_profile_info for approved CA-s table and one missing index            | Martin Lind          |
| 17.10.2015 | 1.2     | Clarified description of the cert_profile_info field                             | Margus Freudenthal   |
| 11.12.2015 | 1.3     | Subsystems can only be clients of security servers                               | Siim Annuk           |
| 02.02.2017 | 1.4     | Update distributed_files and convert to markdown format                          | Ilkka Seppälä        |
| 05.06.2017 | 1.5     | System parameter *confSignAlgoId* replaced with *confSignDigestAlgoId*           | Kristo Heero         |
| 02.03.2018 | 1.6     | Added uniform terms and conditions reference                                     | Tatu Repo            |
| 11.09.2019 | 1.7     | Remove Ubuntu 14.04 support                                                      | Jarkko Hyöty         |
| 11.08.2021 | 1.8     | Update chapter 1.7 about high availability support                               | Ilkka Seppälä        |
| 26.09.2022 | 1.9     | Remove Ubuntu 18.04 support                                                      | Andres Rosenthal     |
| 17.04.2023 | 1.9     | Remove security server category support                                          | Ričardas Bučiūnas    |
| 17.04.2023 | 1.10    | Remove central services support                                                  | Justas Samuolis      | 
| 30.05.2023 | 1.11    | Remove security_server_client_names table                                        | Ovidijus Narkevičius | 
| 14.06.2023 | 1.12    | New Central Server updates                                                       | Eneli Reimets        |
| 08.12.2023 | 1.13    | Added enabled field to server_clients table                                      | Madis Loitmaa        |
| 09.01.2025 | 1.14    | Restructure heading levels to work better with the documentation platform        | Raido Kaju           |
| 21.03.2025 | 1.15    | Syntax dand styling fixes                                                        | Pauline Dimmek       |
| 30.04.2025 | 1.16    | Added maintenance mode related fields to security_servers table                  | Ovidijus Narkevičius |