## Table of Contents



- [License](#license)
- [1 Introduction](#1-introduction)
  * [1.1 Purpose](#11-purpose)
  * [1.2 Terms and Abbreviations](#12-terms-and-abbreviations)
  * [1.3 References](#13-references)
- [2 Overview](#2-overview)
- [3 Use Case Model](#3-use-case-model)
  * [3.1 Actors](#31-actors)
  * [3.2 UC MESS\_01: X-Road Service Call](#32-uc-mess_01-x-road-service-call)
  * [3.3 UC MESS\_02: Process X-Road SOAP Request](#33-uc-mess_02-process-x-road-soap-request)
  * [3.4 UC MESS\_03: Process X-Road Request Message](#34-uc-mess_03-process-x-road-request-message)
  * [3.5 UC MESS\_04: Verify SOAP Message](#35-uc-mess_04-verify-soap-message)
  * [3.6 UC MESS\_05: Initiate a Secure Connection](#36-uc-mess_05-initiate-a-secure-connection)
  * [3.7 UC MESS\_06: Establish the Secure Connection](#37-uc-mess_06-establish-the-secure-connection)
  * [3.8 UC MESS\_07: Verify Authentication Certificate](#38-uc-mess_07-verify-authentication-certificate)
  * [3.9 UC MESS\_08: Create Signature](#39-uc-mess_08-create-signature)
  * [3.10 UC MESS\_09: Log Message and Signature to Message Log](#310-uc-mess_09-log-message-and-signature-to-message-log)
  * [3.11 UC MESS\_10: Timestamp Message Log Records](#311-uc-mess_10-timestamp-message-log-records)
  * [3.12 UC MESS\_11: Verify Signature](#312-uc-mess_11-verify-signature)
  * [3.13 UC MESS\_12: Verify Certificate Chain](#313-uc-mess_12-verify-certificate-chain)
  * [3.14 UC MESS\_13: Validate an OCSP Response](#314-uc-mess_13-validate-an-ocsp-response)
  * [3.15 UC MESS\_14: Get OCSP Responses](#315-uc-mess_14-get-ocsp-responses)
  * [3.16 UC MESS\_15: Get and Verify OCSP Response](#316-uc-mess_15-get-and-verify-ocsp-response)
  * [3.17 UC MESS\_16: Store Operational Monitoring Data and Forward the Data to Operational Monitoring Daemon](#317-uc-mess_16-store-operational-monitoring-data-and-forward-the-data-to-operational-monitoring-daemon)
- [Annex A Sequence Diagram for Messaging](#annex-a-sequence-diagram-for-messaging)

## License

This document is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/

## 1 Introduction

### 1.1 Purpose

The purpose of this document is to describe the events and verifications that take place in the security servers during the communication between an X-Road service client and an X‑Road service provider.

### 1.2 Terms and Abbreviations

See X-Road terms and abbreviations documentation \[[TA-TERMS](#Ref_TERMS)\].