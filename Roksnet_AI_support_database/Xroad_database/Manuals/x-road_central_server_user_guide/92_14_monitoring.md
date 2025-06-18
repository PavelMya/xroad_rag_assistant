## 14. Monitoring

Monitoring is taken to use by installing the monitoring support (see [IG-CS](#13-references) and appointing the central monitoring client as specified below.

Identity of central monitoring client (if any) is configured using Central Server's admin user interface. Configuration is done by updating a specific optional configuration file (see [UC-GCONF](#13-references)) monitoring-params.xml. This configuration file is distributed to all Security Servers through the global configuration distribution process (see [UC-GCONF](#13-references)).

```xml

    
        
            fdev
            GOV
            1710128-9
            LIPPIS
        
    

```

One can configure either one member or a member's subsystem to be the central monitoring client. Permission to execute monitoring queries is strictly limited to that single member or subsystem - defining one subsystem to be a monitoring client does not grant the corresponding member access to querying monitoring data (and vice versa).

To disable central monitoring client altogether, update configuration to one which has no client:

```xml

    
    

```

## 15. Additional configuration options