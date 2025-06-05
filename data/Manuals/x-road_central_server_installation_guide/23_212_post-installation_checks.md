### 2.12 Post-Installation Checks

The installation is successful if the system services are started and the user interface is responding.

-   Ensure from the command line that relevant X-Road services are in the `running` state (example output follows). Notice that it is normal for the xroad-confclient to be in `stopped` state on the Central Server since it operates in one-shot mode.    
    ```bash
    sudo systemctl list-units "xroad*"

    UNIT                                      LOAD   ACTIVE SUB     DESCRIPTION
    xroad-base.service                        loaded active exited  X-Road initialization
    xroad-center-management-service.service   loaded active running X-Road Central Server Management Service
    xroad-center-registration-service.service loaded active running X-Road Central Server Registration Service
    xroad-center.service                      loaded active running X-Road Central Server
    xroad-signer.service                      loaded active running X-Road signer
    ```

-   Ensure that the Central Server user interface at https://SECURITYSERVER:4000/ (**reference data: 1.8; 1.6**) can be opened in a Web browser. To log in, use the account name chosen during the installation (**reference data: 1.3**). While the user interface is still starting up, the Web browser may display the “502 Bad Gateway” error.