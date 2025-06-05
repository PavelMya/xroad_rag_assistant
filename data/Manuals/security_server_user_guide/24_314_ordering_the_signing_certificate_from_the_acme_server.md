#### 3.1.4 Ordering the Signing Certificate from the ACME server

If an approved CA supports ACME, then an alternative to creating the CSR, sending it to be signed by the CA by some outside means and later importing it manually, is to order the certificate from the ACME server of the CA. In this case all these steps are done automatically. To do this:

1. Start the same way as in Section [3.1.1](#331-registering-an-authentication-certificate)

2. In step 4.ii.d choose a **Certification Service** that supports ACME.

3. Some Certification Services require their ACME Server account to be bound to an external account for added security. If that is the case, the chosen **Client** in step 4.ii.b needs to have external accounts credentials configured in `/etc/xroad/conf.d/acme.yml` (more info on how to configure ACME can be found in section [24. Configuring ACME](#24-configuring-acme)).

4. In step 4.iii make sure the **SAN** field has the correct DNS name. This is used by the ACME server to check that the member owns the domain the certificate is ordered for.

5. Press the **Order certificate** button. This will generate the CSR similarly to the **Generate CSR** button and also order the certificate from the ACME Server. When the order is successful, then certificate is returned and imported to the new key automatically.

Signing Certificate can also be ordered with an already existing CSR. For that follow these steps.

1. On the **Navigation tabs**, select **Keys and Certificates**

2. Show more details about a token by clicking the caret next to the token name.

3. On the row of the desired signing key, click **Order Certificate**. This link is only shown if the CSR has been generated beforehand and there are Certificate Authorities available that support ACME and use the same Certificate Profile that the CSR was created with.

4. In the dialog that opens select the issuer of the certificate from the **Certification Service** drop-down list.

5. Click **Order**. When the order succeeds, the certificate is downloaded and imported to the chosen key automatically.