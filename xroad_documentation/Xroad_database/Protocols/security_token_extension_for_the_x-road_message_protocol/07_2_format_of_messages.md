## 2 Format of messages

This section describes the XML format for expressing the security token. The data
structures and elements defined in this section are in the namespace `http://x-road.eu/xsd/security-token.xsd`. The
schema file can be found at [`http://x-road.eu/xsd/security-token.xsd`](http://x-road.eu/xsd/security-token.xsd).
The XML Schema for this extension is also listed in the section [XML Schema for the extension](#xml-schema-for-the-extension).

Note that at the moment, there is no unifying schema that would combine the message protocol and this extension under
the same namespace. That means there is no single schema that would validate an X-Road message with this extension in use.

### 2.1 Schema header

The following listing shows the header of the schema definition

```xml





```

### 2.2 Added `securityToken` element
A new `securityToken` element was added to deliver the security token information.

```xml

  
    
      
        
      
    
  
  
    Contains a security token
  


```