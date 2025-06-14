## Table of Contents

- [1 Introduction](#1-introduction)
    * [1.1 Purpose](#11-purpose)
    * [1.2 Terms and Abbreviations](#12-terms-and-abbreviations)
    * [1.3 References](#13-references)
- [2 Overview](#2-overview)
    * [2.1 Actors](#21-actors)
    * [2.2 Central Server Use Cases](#22-central-server-use-cases)
        * [2.2.1 UC GCONF\_01: View a Configuration Source](#221-uc-gconf_01-view-a-configuration-source)
        * [2.2.2 UC GCONF\_02: Download a Configuration Source Anchor File](#222-uc-gconf_02-download-a-configuration-source-anchor-file)
        * [2.2.3 UC GCONF\_03: Re-Create a Configuration Source Anchor](#223-uc-gconf_03-re-create-a-configuration-source-anchor)
        * [2.2.4 UC GCONF\_04: Describe Optional Configuration Part Data](#224-uc-gconf_04-describe-optional-configuration-part-data)
        * [2.2.5 UC GCONF\_05: Upload an Optional Configuration Part File](#225-uc-gconf_05-upload-an-optional-configuration-part-file)
        * [2.2.6 UC GCONF\_06: Download a Configuration Part File](#226-uc-gconf_06-download-a-configuration-part-file)
        * [2.2.7 UC GCONF\_07: Log In to a Software Security Token](#227-uc-gconf_07-log-in-to-a-software-security-token)
        * [2.2.8 UC GCONF\_08: Log In to a Hardware Security Token](#228-uc-gconf_08-log-in-to-a-hardware-security-token)
        * [2.2.9 UC GCONF\_09: Log Out of a Software Security Token](#229-uc-gconf_09-log-out-of-a-software-security-token)
        * [2.2.10 UC GCONF\_10: Log Out of a Hardware Security Token](#2210-uc-gconf_10-log-out-of-a-hardware-security-token)
        * [2.2.11 UC GCONF\_11: Add a Configuration Source Signing Key](#2211-uc-gconf_11-add-a-configuration-source-signing-key)
        * [2.2.12 UC GCONF\_12: Activate a Configuration Source Signing Key](#2212-uc-gconf_12-activate-a-configuration-source-signing-key)
        * [2.2.13 UC GCONF\_13: Delete a Configuration Source Signing Key](#2213-uc-gconf_13-delete-a-configuration-source-signing-key)
        * [2.2.14 UC GCONF\_14: View System Parameters](#2214-uc-gconf_14-view-system-parameters)
        * [2.2.15 UC GCONF\_15: Edit the Address of the Central Server](#2215-uc-gconf_15-edit-the-address-of-the-central-server)
        * [2.2.16 UC GCONF\_16: Parse User Input](#2216-uc-gconf_16-parse-user-input)
        * [2.2.17 UC GCONF\_17: Generate a Configuration Anchor](#2217-uc-gconf_17-generate-a-configuration-anchor)
        * [2.2.18 UC GCONF\_18: Generate Configuration](#2218-uc-gconf_18-generate-configuration)
        * [2.2.19 UC GCONF\_19: Handle a Configuration Download Request](#2219-uc-gconf_19-handle-a-configuration-download-request)
    * [2.3 Security Server Use Cases](#23-security-server-use-cases)
        * [2.3.1 UC GCONF\_20: View the Configuration Anchor Information](#231-uc-gconf_20-view-the-configuration-anchor-information)
        * [2.3.2 UC GCONF\_21: Download the Configuration Anchor File](#232-uc-gconf_21-download-the-configuration-anchor-file)
        * [2.3.3 UC GCONF\_22: Upload a Configuration Anchor File](#233-uc-gconf_22-upload-a-configuration-anchor-file)
        * [2.3.4 UC GCONF\_23: Update Configuration](#234-uc-gconf_23-update-configuration)
        * [2.3.5 UC GCONF\_24: Download Configuration from a Configuration Source](#235-uc-gconf_24-download-configuration-from-a-configuration-source)
        * [2.3.6 UC GCONF\_25: Verify the Signature of the Configuration Directory](#236-uc-gconf_25-verify-the-signature-of-the-configuration-directory)
        * [2.3.7 UC GCONF\_26: Handle a Configuration Part of the Configuration Directory](#237-uc-gconf_26-handle-a-configuration-part-of-the-configuration-directory)

## License

This work is licensed under the Creative Commons Attribution-ShareAlike
3.0 Unported License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/3.0/.

## 1 Introduction