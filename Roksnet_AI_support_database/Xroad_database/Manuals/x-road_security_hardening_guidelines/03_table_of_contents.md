## Table of Contents 


* [License](#license)
* [1. Introduction](#1-introduction)
    * [1.1 Target Audience](#11-target-audience)
    * [1.2 Terms and abbreviations](#12-terms-and-abbreviations)
    * [1.3 References](#13-references)
* [2. User Management](#2-user-management)
    * [2.1 Configuring account lockout](#21-configuring-account-lockout)
        * [2.1.1 Considerations and risks](#211-considerations-and-risks)
        * [2.1.2 Account lockout examples](#212-account-lockout-examples)
    * [2.2 Configuring password policies](#22-configuring-password-policies)
        * [2.2.1 Considerations and risks](#221-considerations-and-risks)
    * [2.3 Ensuring User Account Security](#23-ensuring-user-account-security)
* [3. Admin UI (Central Server and Security Server)](#3-admin-ui-central-server-and-security-server)
    * [3.1 Host header injection mitigation](#31-host-header-injection-mitigation)
* [4. Access control](#4-access-control)
    * [4.1 Minimum Supported Client Security Server Version](#41-minimum-supported-client-security-server-version)
* [5. Publish global configuration over HTTPS](#5-publish-global-configuration-over-https)
    * [5.1 Central Server TLS configuration](#51-central-server-tls-configuration)
    * [5.2 Configuration Proxy TLS configuration](#52-configuration-proxy-tls-configuration)
    * [5.3 Security Server TLS configuration](#53-security-server-tls-configuration)

## License

This document is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/.

## 1. Introduction

You may want to harden the security of your X-Road instance by configuring additional security policies within your X-Road infrastructure.
The security measures that are introduced in this guide are common security policies that can be configured on operating system level.

### 1.1 Target Audience

The intended audience of this User Guide are X-Road administrators (Central or Security server) who are responsible for X-Road instance set-up and/or everyday management of the X-Road infrastructure.

### 1.2 Terms and abbreviations

See X-Road terms and abbreviations documentation \[[TA-TERMS](#Ref_TERMS)\].