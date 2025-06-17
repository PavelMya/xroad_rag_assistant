## Table of Contents


- [X-Road: Operational Monitoring Testing Plan](#x-road-operational-monitoring-testing-plan)
  - [Table of Contents](#table-of-contents)
  - [License](#license)
  - [1 Introduction](#1-introduction)
    - [1.1 Purpose](#11-purpose)
    - [1.2 Terms and Abbreviations](#12-terms-and-abbreviations)
    - [1.3 References](#13-references)
  - [2 Components of the Operational Monitoring System in the Context of Testing](#2-components-of-the-operational-monitoring-system-in-the-context-of-testing)
    - [2.1 Testing the Operational Monitoring Database](#21-testing-the-operational-monitoring-database)
    - [2.2 Testing the Operational Monitoring Service](#22-testing-the-operational-monitoring-service)
  - [3 The Protocols and Interfaces used in the Operational Monitoring System in the Context of Testing](#3-the-protocols-and-interfaces-used-in-the-operational-monitoring-system-in-the-context-of-testing)
  - [4 The Use Cases of the Operational Monitoring Daemon in the Context of Testing](#4-the-use-cases-of-the-operational-monitoring-daemon-in-the-context-of-testing)
  - [5 Automated Integration Testing in Detail](#5-automated-integration-testing-in-detail)
  - [6 Testing the JMXMP Interface](#6-testing-the-jmxmp-interface)
    - [6.1 Testing the JMXMP Interface Using jconsole](#61-testing-the-jmxmp-interface-using-jconsole)
  - [7 Manual Integration Testing in Detail](#7-manual-integration-testing-in-detail)
    - [7.1 Test Helpers](#71-test-helpers)
    - [7.2 Send a Request to a Non-operational Service Cluster](#72-send-a-request-to-a-non-operational-service-cluster)
    - [7.3 Run Operational Monitoring Data Cleanup](#73-run-operational-monitoring-data-cleanup)
    - [7.4 Receive Operational Data in Multiple Batches](#74-receive-operational-data-in-multiple-batches)
    - [7.5 Configure an External Monitoring Daemon](#75-configure-an-external-monitoring-daemon)
    - [7.6 Use Invalid Certificates for TLS Connection](#76-use-invalid-certificates-for-tls-connection)

## License

This document is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/.

## 1 Introduction