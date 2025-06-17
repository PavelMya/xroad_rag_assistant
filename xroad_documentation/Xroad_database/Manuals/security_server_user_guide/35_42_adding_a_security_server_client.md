### 4.2 Adding a Security Server Client

**Access rights:** [Registration Officer](#xroad-registration-officer)

Follow these steps.

1.  In the **CLIENTS** view, click **ADD CLIENT**.

2.  In the wizard that opens

    1. Client details page: Select an existing client from the Global list by pressing **SELECT CLIENT** or specify the details of the Client to be added manually. Also renaming existing or adding name for new subsystem is possible by editing value in Subsystem name field. Click **NEXT**

    2. Token page: Select the token where you want to add the SIGN key for the new Client. Click **NEXT**

    3. Sign key page: Define a label (optional) for the newly created SIGN key and click **NEXT**

    4. CSR details page: Select the Certification Authority (CA) that will issue the certificate in **Certification Service** field and format of the certificate signing request according to the CA's requirements in the **CSR Format** field. Click **NEXT**.

    5. Generate CSR page: Fill in empty CSR fields as needed (like **Organization Name (O)** and **Subject Alternative Name (SAN)**) that are based on the certificate profile that the chosen CA uses, and click **NEXT**

       1. If the CA supports it, an ACME certificate order can be made with the generated CSR by checking the "**Order certificate from ACME Server with the generated CSR and import the returned certificate to the token.**" checkbox.

    6. Finish page: click **SUBMIT** and the new client will be added to the Clients list and the new key and CSR (or certificate in case of ACME) will appear in the Keys and Certificates view.

The new client is added to the list of Security Server clients in the "Saved" state.