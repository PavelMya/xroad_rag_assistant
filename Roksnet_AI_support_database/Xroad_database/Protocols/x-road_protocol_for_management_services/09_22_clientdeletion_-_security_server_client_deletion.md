### 2.2 *clientDeletion* - Security Server Client Deletion

The *clientDeletion* service is invoked by the Security Server when a client is unregistered.

The body of the client deletion message (request or response) contains following fields:

* **client** – identifier of the subsystem to be removed from the Security Server;

* **server** – identifier of the Security Server where the client is removed;

* **requestId** – for responses only, unique identifier of the request that is stored in the Central Server database \[[DM-CS](#Ref_DM-CS)\].

The XML Schema fragment of the client deletion request body shown below.

```xml

    
        
        
        
    

```

The response echoes back the client and the server fields of the request and adds the field *requestId*.

An example of the client deletion request and response is given in [Annex A.2](#a2-clientdeletion).