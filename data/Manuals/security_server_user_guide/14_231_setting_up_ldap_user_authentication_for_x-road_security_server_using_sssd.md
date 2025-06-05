#### 2.3.1 Setting up LDAP User Authentication for X-Road Security Server using SSSD

To configure LDAP user authentication on the X-Road Security Server using SSSD, follow these steps:

1. **Install the SSSD Package**:
   - On Ubuntu systems, use the following command:
      ```shell
      sudo apt-get -y install sssd sssd-ldap
      ```
    - On RHEL systems, use the following command:
      ```shell
      sudo yum install -y sssd sssd-ldap
      ```

2. **Configure SSSD**:
    - Create and edit the `/etc/sssd/sssd.conf` file to set up the connection to your LDAP server with the following configurations:
        - `[sssd]`
        - `services = nss, pam`
        - `domains = LDAP`
        - `[domain/LDAP]`
        - `id_provider = ldap`
        - `auth_provider = ldap`
        - `chpass_provider = ldap`
        - `ldap_uri = ldap://<LDAP_SERVER_IP_OR_DNS>/`
        - `ldap_search_base = dc=example,dc=com`
        - `ldap_default_bind_dn = cn=admin,dc=example,dc=com`
        - `ldap_default_authtok_type = password`
        - `ldap_default_authtok = <BIND_PASSWORD>`
        - Ensure that the file permissions are secure:
          ```shell
          sudo chmod 600 /etc/sssd/sssd.conf
          ```
    - Replace placeholders like `<LDAP_SERVER_IP_OR_DNS>`, `<BIND_PASSWORD>`, authentication parameters, etc., with actual values specific to your LDAP setup.

3. **Modify NSS Configuration**:
    - Update the `/etc/nsswitch.conf` file to include SSSD as a source for user and group information:
      ```conf
      passwd:         sss files
      group:          sss files
      shadow:         sss files
      ```
   Note: This step is typically automated by the installation process.

4. **Map LDAP Groups to X-Road Roles** (Optional):
    - If LDAP groups do not align with X-Road's requirements, you can map them accordingly in the `/etc/xroad/conf.d/local.ini` file:
      ```ini
      [proxy-ui-api.complementary-user-role-mappings]
      XROAD_SECURITY_OFFICER=ldap_group1,ldap_group2
      XROAD_SERVICE_ADMINISTRATOR=ldap_group3,ldap_group4
      ```
    - Replace `ldap_group1`, `ldap_group2`, etc., with actual LDAP group names that correspond to X-Road roles.

5. **Enable and Start SSSD Service**:
    - Enable and start the SSSD service to apply the changes:
      ```shell
      sudo systemctl enable sssd
      sudo systemctl start sssd
      ```

6. **Restart X-Road Services**:
    - Restart the `xroad-proxy-ui` service to apply the changes:
      ```shell
      sudo systemctl restart xroad-proxy-ui
      ```