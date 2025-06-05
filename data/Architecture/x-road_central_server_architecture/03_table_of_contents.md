## Table of Contents

<!-- toc -->

- [X-Road: Central Server Architecture](#x-road-central-server-architecture)
  - [Version history](#version-history)
  - [Table of Contents](#table-of-contents)
  - [License](#license)
  - [1 Introduction](#1-introduction)
    - [1.1 Overview](#11-overview)
    - [1.2 Terms and Abbreviations](#12-terms-and-abbreviations)
    - [1.3 References](#13-references)
  - [2 Component View](#2-component-view)
    - [2.1 Administration Service](#21-administration-service)
    - [2.2 Web Server](#22-web-server)
    - [2.3 Management Services](#23-management-services)
    - [2.4 Signer](#24-signer)
    - [2.5 Database](#25-database)
    - [2.6 User Interface Frontend](#26-user-interface-frontend)
    - [2.7 Password Store](#27-password-store)
    - [2.8 SSCD](#28-sscd)
  - [3 Interfaces](#3-interfaces)
    - [3.1 Management Services](#31-management-services)
    - [3.1.1 Member Management Web Service](#311-member-management-web-service)
    - [3.1.2 Registration Web Service](#312-registration-web-service)
    - [3.2 Download Configuration](#32-download-configuration)
    - [3.3 Administration Service REST API](#33-administration-service-rest-api)
  - [4 Configuration Creation Workflow](#4-configuration-creation-workflow)
  - [5 Deployment View](#5-deployment-view)
    - [5.1 Simple Deployment](#51-simple-deployment)
    - [5.2 Deployment in High Availability Setup](#52-deployment-in-high-availability-setup)

<!-- tocstop -->