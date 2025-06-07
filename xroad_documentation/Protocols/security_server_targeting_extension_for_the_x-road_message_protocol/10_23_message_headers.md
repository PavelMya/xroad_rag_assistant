### 2.3 Message headers
 This section describes the additional SOAP headers that are added by this extension.

|Field | Type | Mandatory/Optional | Description |
|-------------|-------------|-------------|-------------|
| securityServer | XRoadSecurityServerIdentifierType | Optional | The security server this message is for |

## 3 XML Schema for the extension
 ```xml


    
    

    
    
        
            Identifies security server
        
    

```

## 4 Examples
Below are examples from a request and response related to the Environmental Monitoring
\[[ARC-ENVMON](#Ref_ARC-ENVMON)\] service `getSecurityServerMetrics` which uses the `securityServer` element protocol extension.