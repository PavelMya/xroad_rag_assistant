#### 4.2.3 Configuring the Management Services in the Management Services’ Security Server

Access rights: Security server’s Service Administrator

The data necessary for configuring the management services in the Security Server can be found at the Central Server Settings tab -> System Settings -> Management Services section.

To configure management services in the management services’ Security Server, follow these steps.

1. In the Clients tab of the Security Server, select the client who will provide the management services. On the details view click Services sub-tab.
2. Click Add WSDL, enter the management services WSDL address in the window that opens and click Add.
3. Expand the WSDL, by clicking the > icon, select a service by click Service Code.
4. In the window that opens, enter the management services address. If necessary, edit other service parameters. Check the Apply to All in WSDL checkbox and click Save. Ensure that the parameters of all the management services have changed.
5. Activate the management service’s WSDL by selecting the row of the WSDL and clicking Enable.
6. Navigate to the Service Clients tab.
7. Click Add subject and search for the global group security-server-owners. Select the group and click Next.
8. In the window that opens, check management services checkboxes (authCertDeletion, clientDeletion, clientReg, ownerChange) and click Add Selected to add the security-server-owners group’s access rights list.