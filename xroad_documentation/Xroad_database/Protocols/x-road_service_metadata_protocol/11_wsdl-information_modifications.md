#### WSDL-information modifications

Security server MUST replace endpoint location with value `http://example.org/xroad-endpoint`.
This is done for security reasons, to hide the endpoint addresses which often point
to information systems which should be hidden from the clients, and be accessed only through
the provider security server.

For example service definition

```xml
    
        
            
        
    
```

becomes

```xml
    
        
            
        
    
```

when retrieved through the meta-service.

## Annex A XML Schema for Messages

```xml


    
    
        
            
        
    
    
        
            
            
            
        
    
    

```

## Annex B listMethods, allowedMethods, and getWsdl service descriptions