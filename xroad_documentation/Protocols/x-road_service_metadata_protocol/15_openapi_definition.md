### OpenAPI definition

```yaml
openapi: 3.0.0
info:
  title: X-Road Service Metadata API
  version: '2.7'
servers:
  - url: 'https://{securityserver}/'
paths:
  /listClients:
    get:
      tags:
        - metaservices
      summary: List clients defined in the X-Road instance
      operationId: listClients
      parameters:
        - name: xRoadInstance
          in: query
          schema:
            type: string
      responses:
        '200':
          description: List of clients
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/clientList'
components:
  schemas:
    clientList:
      type: object
      properties:
        member:
          type: array
          items:
            $ref: '#/components/schemas/xroadIdentifier'
    xroadIdentifier:
      type: object
      properties:
        name:
          type: string
        subsystem_name:
          type: string
        id:
          type: object
          properties:
            object_type:
              type: string
              enum:
                - MEMBER
                - SUBSYSTEM
                - SERVER
                - GLOBALGROUP
                - LOCALGROUP
                - SERVICE
            xroad_instance:
              type: string
            member_class:
              type: string
            member_code:
              type: string
            subsystem_code:
              type: string
```

## Annex C Example Messages

### C.1 listClients Response