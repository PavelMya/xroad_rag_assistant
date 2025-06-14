## Annex A Service Descriptions for REST Metadata Services

```yaml
openapi: 3.0.0
info:
  title: X-Road Service Metadata API for REST
  version: '0.3'
servers:
  - url: https://{securityserver}/r1
    variables:
      securityserver:
        default: ''
        description: 'security server address'
paths:
  /{xRoadInstance}/{memberClass}/{memberCode}/{subsystemCode}/listMethods:
    parameters:
      - $ref: '#/components/parameters/xRoadInstance'
      - $ref: '#/components/parameters/memberClass'
      - $ref: '#/components/parameters/memberCode'
      - $ref: '#/components/parameters/subsystemCode'
    get:
      tags:
        - metaservices
      summary: List REST services and endpoints for a service provider
      operationId: listMethods
      parameters:
        - name: serviceId
          in: query
          schema:
            type: string
        - name: X-Road-Client
          in: header
          schema:
            type: string
      responses:
        '200':
          description: List of REST services and endpoints for a service provider
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/restServiceDetailsListType'
  /{xRoadInstance}/{memberClass}/{memberCode}/{subsystemCode}/allowedMethods:
    parameters:
      - $ref: '#/components/parameters/xRoadInstance'
      - $ref: '#/components/parameters/memberClass'
      - $ref: '#/components/parameters/memberCode'
      - $ref: '#/components/parameters/subsystemCode'
    get:
      tags:
        - metaservices
      summary: List of allowed REST services and endpoints for a service provider
      operationId: allowedMethods
      parameters:
        - name: serviceId
          in: query
          schema:
            type: string
        - name: X-Road-Client
          in: header
          schema:
            type: string
      responses:
        '200':
          description: List of allowed REST services and endpoints for a service provider
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/restServiceDetailsListType'
  /{xRoadInstance}/{memberClass}/{memberCode}/{subsystemCode}/getOpenAPI:
    parameters:
      - $ref: "#/components/parameters/xRoadInstance"
      - $ref: "#/components/parameters/memberClass"
      - $ref: "#/components/parameters/memberCode"
      - $ref: "#/components/parameters/subsystemCode"
    get:
      tags:
        - metaservices
      summary: Returns OpenAPI service description for a REST service
      operationId: getOpenAPI
      parameters:
        - name: serviceCode
          in: query
          schema:
            type: string
        - name: X-Road-Client
          in: header
          schema:
            type: string
      responses:
        '200':
          description: OpenAPI description of the specified REST service
          content:
            application/json:
              schema:
                type: string
            text/yaml:
              schema:
                type: string
        '400':
          description: Error in request
        '500':
          description: Internal error
components:
  parameters:
    xRoadInstance:
      name: xRoadInstance
      required: true
      in: path
      schema:
        type: string
    memberClass:
      name: memberClass
      required: true
      in: path
      schema:
        type: string
    memberCode:
      name: memberCode
      required: true
      in: path
      schema:
        type: string
    subsystemCode:
      name: subsystemCode
      required: true
      in: path
      schema:
        type: string
  schemas:
    restServiceDetailsListType:
      type: object
      properties:
        member:
          type: array
          items:
            $ref: '#/components/schemas/xroadRestServiceDetailsType'
    xroadRestServiceDetailsType:
      type: object
      properties:
        objectType:
          type: object
          properties:
            object_type:
              type: string
              enum:
                - MEMBER
                - SUBSYSTEM
                - SERVER
                - GLOBALGROUP
                - SERVICE
                - LOCALGROUP
        serviceType:
          type: string
        xRoadInstance:
          type: string
        memberClass:
          type: string
        memberCode:
          type: string
        subsystemCode:
          type: string
        serviceCode:
          type: string
        serviceVersion:
          type: string
        endpointList:
          type: object
          properties:
            member:
              type: array
              items:
                $ref: '#/components/schemas/endpoint'
    endpoint:
      type: object
      properties:
        method:
          type: string
        path:
          type: string
```

## Annex B Example Messages