## Annex B WSDL File for Management Services

```xml


  
    
    
      
        
          Globally unique identifier in the
            X-Road system. Identifier consists of object type
            specifier and list of hierarchical codes
            (starting with code that identifiers the X-Road
            instance).
          
        
        
          
          
          
          
          
          
          
        
        
      
      
        
          Enumeration for X-Road identifier
            types that can be used in requests.
          
        
        
          
          
          
          
        
      
      
        
          Identifies the X-Road instance.
            This field is applicable to all identifier
            types.
          
        
      
      
        
          Type of the member (company,
            government institution, private person, etc.)
          
        
      
      
        
          Code that uniquely identifies a
            member of given member type.
          
        
      
      
        
          Code that uniquely identifies a
            subsystem of given X-Road member.
          
        
      
      
        
          Code that uniquely identifies a
            service offered by given X-Road member or
            subsystem.
          
        
      
      
        
          Version of the service.
          
        
      
      
        
          Code that uniquely identifies
            Security Server offered by a given X-Road member
            or subsystem.
          
        
      
      
      
        
          
            
              
              
              
              
            
          
        
      
      
        
          
            
              
              
              
              
              
              
            
          
        
      
      
        
          
            
              
              
              
              
            
          
        
      
    
    
    
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        
          
            
              Identity of the Security Server the
                authentication certificate will be associated with.
              
            
          
          
            
              Address of the Security Server the
                authentication certificate will be associated with.
              
            
          
          
            
              
                Contents (in DER encoding) of
                the authentication certificate that will
                be added to the list of certificates
                authenticating the Security Server.
              
            
          
          
        
      
      
        
          
            
              Identity of the Security Server the
                authentication certificate will be deleted from.
              
            
          
          
            
              Contents (in DER encoding) of
                the authentication certificate that will
                be deleted from the list of certificates
                authenticating the Security Server.
              
            
          
          
        
      
      
        
          
            
              Identifier of the security
                server where the client is added to or removed
                from (depending on the request type).
              
            
          
          
            
              Identifier of the client
                associated with the Security Server. When the
                request is for registering client, the client is
                added to the Security Server. When the request
                is for deleting client, the client is removed
                from the clients' list of the Security Server.
              
            
          
          
        
      
      
        
          
            
              Identifier of the security
                server where the client is added to or removed
                from (depending on the request type).
              
            
          
          
            
              Identifier of the client
                associated with the Security Server. When the
                request is for registering client, the client is
                added to the Security Server. When the request
                is for deleting client, the client is removed
                from the clients' list of the Security Server.
              
            
          
          
            
              Optional new name for client subsystem.
            
          
          
        
      
      
        
          
            
              Identifier of the security
                server where the client is added to or removed
                from (depending on the request type).
              
            
          
          
            
              Identifier of the client
                associated with the Security Server. When the
                request is for registering client, the client is
                added to the Security Server. When the request
                is for deleting client, the client is removed
                from the clients' list of the Security Server.
              
            
          
          
            
              New name of client subsystem.
            
          
          
        
      
      
        
          
            
              Identifier of the security server for which the address will be changed.
            
          
          
            
              New address of the Security Server
            
          
          
        
      
      
        
          
            
              Identifier of the security server which will be put into maintenance mode.
            
          
          
            
              Optional message for maintenance mode
            
          
          
        
      
      
        
          
            
              Identifier of the security server which will be taken out of maintenance mode.
            
          
          
        
      
      
        
          For responses only, unique identifier
            of the request that is stored in the Central Server database.
          
        
        
      
    
  
  
    
    
    
    
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
  
  
    
      
      
    
    
      
      
    
    
      
      
    
    
      
      
    
    
      
      
    
    
      
      
    
    
      
      
    
    
      
      
    
    
      
      
    
    
      
      
    
  
  
    
    
      
      
        
        
        
        
        
      
      
        
        
        
        
        
        
      
    
    
      
      
        
        
        
        
        
      
      
        
        
        
        
        
        
      
    
    
      
      
        
        
        
        
        
      
      
        
        
        
        
        
        
      
    
    
      
      
        
        
        
        
        
      
      
        
        
        
        
        
        
      
    
    
      
      
        
        
        
        
        
      
      
        
        
        
        
        
        
      
    
    
      
      
        
        
        
        
        
      
      
        
        
        
        
        
        
      
    
    
      
      
        
        
        
        
        
      
      
        
        
        
        
        
        
      
    
    
      
      
        
        
        
        
        
      
      
        
        
        
        
        
        
      
    
    
      
      
        
        
        
        
        
      
      
        
        
        
        
        
        
      
    
    
      
      
        
        
        
        
        
      
      
        
        
        
        
        
        
      
    
  
  
    
      
    
  

```