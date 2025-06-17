### 21.1 Updating Proxy Service's memory allocation command line arguments

In case of proxy service, the memory allocation command line arguments can be updated by using  helper script `proxy_memory_helper.sh` located in `/usr/share/xroad/scripts/` directory. The script updates the `XROAD_PROXY_PARAMS` property in `/etc/xroad/services/local.properties` file.

Usage examples:

* Get information about total memory, used memory, current configuration and suggested configuration for proxy service:

    ```bash
    proxy_memory_helper.sh
    #alternatively
    #proxy_memory_helper.sh status
    ```

* Get/Apply recommended memory allocation config based on total memory:

    ```bash
    #Prints the recommended memory allocation configuration
    proxy_memory_helper.sh get-recommended
    #Applies the recommended memory allocation configuration
    proxy_memory_helper.sh apply-recommended
    ```
  
* Get/Apply default memory allocation config based on total memory:

    ```bash
    #Prints the default memory allocation configuration
    proxy_memory_helper.sh get-default
    #Applies the default memory allocation configuration
    proxy_memory_helper.sh apply-default
    ```
    
* Apply custom memory allocation config based on total memory, first value is for initial heap size and second value is for maximum heap size:

    ```bash
    proxy_memory_helper.sh apply 256m 4g
    ```

* All available commands can be listed with:

    ```bash
    proxy_memory_helper.sh help
    ```  

  Value format is the same as for Java's `-Xms` and `-Xmx` options. The script will update the `XROAD_PROXY_PARAMS` property in `/etc/xroad/services/local.properties` file.

  After running the script, the changes will take effect only after restarting the `xroad-proxy` service.

    ```bash
    sudo systemctl restart xroad-proxy
    ```

  Note that only -Xms, -Xmx, -XX:InitialHeapSize and -XX:MaxHeapSize options will be overwritten. Instead, any other options present in the XROAD_PROXY_PARAMS property will be preserved.

## 22 Additional Security Hardening

For the guidelines on security hardening, please refer to [UG-SEC](ug-sec_x_road_security_hardening.md).