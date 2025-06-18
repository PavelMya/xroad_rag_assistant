### B.3 getOpenAPI Response

`curl -H "accept: application/json" -H "X-Road-Client:INSTANCE/CLASS1/MEMBER1/SUBSYSTEM1" "https://SECURITYSERVER:443/r1/INSTANCE/CLASS2/MEMBER2/SUBSYSTEM2/getOpenAPI?serviceCode=listFirms"`

```yaml
openapi: "3.0.0"
info:
  version: 1.0.0
  title: Firm listing
servers:
  - url: https://example.com
paths:
  /firms:
    get:
      summary: List all firms
      operationId: listFirms
      tags:
        - firms
      parameters:
        - name: limit
          in: query
          description: How many items to return at one time (max 100)
          required: false
          schema:
            type: integer
            format: int32
      responses:
        '200':
          description: A paged array of firms
          headers:
            x-next:
              description: A link to the next page of responses
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Firms"
        default:
          description: unexpected error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
components:
  schemas:
    Firm:
      required:
        - id
        - name
        - size
        - country
      properties:
        id:
          type: integer
          format: int64
        name:
          type: string
        tag:
          type: string
    Firms:
      type: array
      items:
        $ref: "#/components/schemas/Firm"
    Error:
      required:
        - code
        - message
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
```