### 10.5 Approved Certificate Authorities

_To list the approved certificate authorities_, follow these steps.

1.  In the **Navigation tabs**, select **SETTINGS**.

2.  In the opening view select **SYSTEM PARAMETERS** tab. Approved certificate authorities are listed in the "Approved Certificate Authorities" section.

Lists approved certificate authorities. The listing contains the following information:

* CA certificate subject distinguished name. Top-level CAs are **emphasized**.
* OCSP response status (not applicable to top-level CAs, shown as N/A). See [5.3 Validity States of Certificates](#53-validity-states-of-certificates) for explanation, with the following exceptions:
  * Disabled status is not used
  * Additional status "not available" if the OCSP response is not available at all, e.g. due to an error.
* Certificate expiration date.