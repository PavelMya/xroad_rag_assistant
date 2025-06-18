### 2.1 Identifiers

This section describes XML-based data formats for expressing the identifiers described informally in [Section 1.3](#13-identifying-entities). The data structures and elements defined in this section will be located under namespace `http://x-road.eu/xsd/identifiers`. The complete XML Schema is shown in [Annex A](#annex-a-xml-schema-for-identifiers).

The following listing shows the header of the schema definition.

```xml


```

The `XRoadIdentifierType` complex type serves as the base for all other identifier types (derived by restriction). It contains a union of all fields that can be present in different identifiers. The attribute `objectType` contains the type of the identifier and can be used, for example, to distinguish between X-Road member and subsystem identifiers without resorting to conditions that check for presence of individual fields.

```xml
    
        
            
            
            
            
            
            
        
        
    
```

The enumeration `XRoadObjectType` lists all possible values of the `objectType` attribute.

```xml
    
        
            
            
            
        
    
```

Next, we define elements and attributes used in the `XRoadIdentifierType`.

```xml
    
    
    
    
    
    
    
```

Finally, we define complex types for representing concrete types of identifiers. First, the `XRoadClientIdentifierType` is used to represent identifiers that can be used by the service clients, namely X-Road members and subsystems.

```xml
    
        
            
                
                    
                    
                    
                    
                
            
        
    
```

The `XRoadServiceIdentifierType` can be used to represent identifiers of services.

```xml
    
        
            
                
                    
                    
                    
                    
                    
                    
                
            
        
    
```