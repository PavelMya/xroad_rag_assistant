### 3.4 Changing the Security Server Owner

**Access rights:** [Registration Officer](#xroad-registration-officer)

To change the Security Server owner, two registered Owner members must be available. If a registered member is already available, jump directly to step 3.

To add a new member and change it to Owner member, the following actions must be completed.

1.  Add a new Owner member to the Security Server

    1.1 On the **CLIENTS** view, select **ADD MEMBER**.

    1.2 In the opening wizard, Select the new Owner member from the list of Security Server clients

    1.3 Add the selected member

    Note: Signing Key and Certificate must be configured for the new Owner member. If needed, the wizard will automatically show the dedicated steps for Key and Certificate configuration to collect the needed information.

2.  Register the new member

    2.1 On the **CLIENTS** view, locate the new member in the Clients list and click **Register** in the corresponding row

    2.2 In the opening dialog, click **Register**. A registeration request is sent to the X-Road Governing Authority

    Note: Once the request is approved, the new member appears as "Registered" - it can be set as Owner member.

3.  Request a change of the Security Server owner

    3.1 On the **CLIENTS** view, locate the new member and click its name to open the member's detail view

    3.2 In the detail view, click **MAKE OWNER**

    1.3 In the opening dialog, click **MAKE OWNER**. An owner change request is sent to the X-Road Governing Authority

Once the owner change request is approved, the new member will be automatically shown as the Security Server Owner member.

- A new member must be added to the Security Server (see [4.2](#42-adding-a-security-server-client)). If needed, specify the token on which the member is configured

- If not yet available, a Signing Key and Certificate must be configured for the new member (see [4.4](#44-configuring-a-signing-key-and-certificate-for-a-security-server-client)).

- The new member must be registered in the X-Road Governing Authority (see [4.5](#45-registering-a-security-server-client-in-the-x-road-governing-authority)).

- The Security Server owner change request must be submitted from the Security Server. To submit an owner change request follow these steps.

  1. In the **Member Detail view** click **MAKE OWNER**.

  2. Click **MAKE OWNER** to submit a change request.

- The change request is sent to the X-Road governing authority according to the organizational procedures of the X-Road instance.

- Once the owner change request is approved by the X-Road governing authority, the member will automatically become the Owner Member.

- New Authentication Key and Certificate should be configured for the new Security Server owner (see [3.2](#32-configuring-the-authentication-key-and-certificate-for-the-security-server)).