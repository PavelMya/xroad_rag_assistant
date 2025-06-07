### 17.3 Controlling Access to Monitoring 

Both environmental and operational monitoring queries are allowed from

  * a client that is the owner of the Security Server
  * a central monitoring client (if any have been configured)
  
In addition, a regular client is allowed to query its own operational monitoring records - records that are associated with the client sending the query.

The central monitoring client is configured via Central Server administrator user interface. Attempts to query monitoring data from other clients results in an AccessDenied system response.