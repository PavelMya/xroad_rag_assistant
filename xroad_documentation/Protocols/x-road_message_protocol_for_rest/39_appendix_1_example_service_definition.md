## Appendix 1 Example Service Definition

```yaml
openapi: 3.0.0
info:
  description: >-
    This is a sample server Petstore server.
  version: 1.0.0
  title: Petstore
  contact:
    email: info@niis.org
  license:
    name: Apache 2.0
    url: 'http://www.apache.org/licenses/LICENSE-2.0.html'
tags:
  - name: pet
    description: Everything about your Pets
    externalDocs:
      description: Find out more
      url: 'https://niis.org'
  - name: store
    description: Access to Petstore orders
  - name: user
    description: Operations about user
    externalDocs:
      description: Find out more about our store
      url: 'https://niis.org'
paths:
  /pets:
    get:
      tags:
        - pet
      summary: Get pets from store
      description: Search pets
      operationId: getPets
      parameters:
        - name: term
          in: query
          description: search term
          required: false
          schema:
            type: string
      responses:
        '200':
          description: successful operation
          content:
            application/xml:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Pet'
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Pet'
        '400':
          description: Invalid ID supplied
        '404':
          description: Pet not found
      security:
        - api_key: [ ]
    post:
      tags:
        - pet
      summary: Add a new pet to the store
      description: ''
      operationId: addPet
      responses:
        '201':
          description: pet created
        '405':
          description: Invalid input
      security:
        - petstore_auth:
            - 'write:pets'
            - 'read:pets'
      requestBody:
        $ref: '#/components/requestBodies/Pet'
  '/pets/{petId}':
    get:
      tags:
        - pet
      summary: Find pet by ID
      description: Returns a single pet
      operationId: getPetById
      parameters:
        - name: petId
          in: path
          description: ID of pet to return
          required: true
          schema:
            type: integer
            format: int64
      responses:
        '200':
          description: successful operation
          content:
            application/xml:
              schema:
                $ref: '#/components/schemas/Pet'
            application/json:
              schema:
                $ref: '#/components/schemas/Pet'
        '400':
          description: Invalid ID supplied
        '404':
          description: Pet not found
      security:
        - api_key: [ ]
    put:
      tags:
        - pet
      summary: Update an existing pet
      description: ''
      operationId: updatePet
      parameters:
        - name: petId
          in: path
          description: ID of pet to return
          required: true
          schema:
            type: integer
            format: int64
      responses:
        '200':
          description: Pet updated
        '400':
          description: Invalid ID supplied
        '404':
          description: Pet not found
        '405':
          description: Validation exception
      security:
        - petstore_auth:
            - 'write:pets'
            - 'read:pets'
      requestBody:
        $ref: '#/components/requestBodies/Pet'
    delete:
      tags:
        - pet
      summary: Deletes a pet
      description: ''
      operationId: deletePet
      parameters:
        - name: api_key
          in: header
          required: false
          schema:
            type: string
        - name: petId
          in: path
          description: Pet id to delete
          required: true
          schema:
            type: integer
            format: int64
      responses:
        '200':
          description: Pet deleted
        '400':
          description: Invalid ID supplied
        '404':
          description: Pet not found
      security:
        - petstore_auth:
            - 'write:pets'
            - 'read:pets'
  '/pets/{petId}/images':
    post:
      tags:
        - pet
      summary: Uploads an image
      description: ''
      operationId: uploadFile
      parameters:
        - name: petId
          in: path
          description: ID of pet to update
          required: true
          schema:
            type: integer
            format: int64
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiResponse'
      security:
        - petstore_auth:
            - 'write:pets'
            - 'read:pets'
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                additionalMetadata:
                  description: Additional data to pass to server
                  type: string
                file:
                  description: file to upload
                  type: string
                  format: binary
  /store/inventories:
    get:
      tags:
        - store
      summary: Returns pet inventories by status
      description: Returns a map of status codes to quantities
      operationId: getInventory
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                type: object
                additionalProperties:
                  type: integer
                  format: int32
      security:
        - api_key: [ ]
  /store/orders:
    post:
      tags:
        - store
      summary: Place an order for a pet
      description: ''
      operationId: placeOrder
      responses:
        '200':
          description: successful operation
          content:
            application/xml:
              schema:
                $ref: '#/components/schemas/Order'
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
        '400':
          description: Invalid Order
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Order'
        description: order placed for purchasing the pet
        required: true
  '/store/orders/{orderId}':
    get:
      tags:
        - store
      summary: Find purchase order by ID
      description: >-
        For valid response try integer IDs with value >= 1 and -
        For valid response try integer IDs with positive integer value.      
        Negative or non-integer values will generate API errors
      operationId: deleteOrder
      parameters:
        - name: orderId
          in: path
          description: ID of the order that needs to be deleted
          required: true
          schema:
            type: integer
            format: int64
            minimum: 1
      responses:
        '200':
          description: Purchase order deleted
        '400':
          description: Invalid ID supplied
        '404':
          description: Order not found
  /users:
    post:
      tags:
        - user
      summary: Create user
      description: This can only be done by the logged in user.
      operationId: createUser
      responses:
        default:
          description: successful operation
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
        description: Created user object
        required: true
  /users/login:
    get:
      tags:
        - user
      summary: Logs user into the system
      description: ''
      operationId: loginUser
      parameters:
        - name: username
          in: query
          description: The user name for login
          required: true
          schema:
            type: string
        - name: password
          in: query
          description: The password for login in clear text
          required: true
          schema:
            type: string
      responses:
        '200':
          description: successful operation
          headers:
            X-Rate-Limit:
              description: calls per hour allowed by the user
              schema:
                type: integer
                format: int32
            X-Expires-After:
              description: date in UTC when token expires
              schema:
                type: string
                format: date-time
          content:
            application/xml:
              schema:
                type: string
            application/json:
              schema:
                type: string
        '400':
          description: Invalid username/password supplied
  /users/logout:
    get:
      tags:
        - user
      summary: Logs out current logged in user session
      description: ''
      operationId: logoutUser
      responses:
        default:
          description: successful operation
  '/users/{username}':
    get:
      tags:
        - user
      summary: Get user by user name
      description: ''
      operationId: getUserByName
      parameters:
        - name: username
          in: path
          description: 'The name that needs to be fetched. Use user1 for testing. '
          required: true
          schema:
            type: string
      responses:
        '200':
          description: successful operation
          content:
            application/xml:
              schema:
                $ref: '#/components/schemas/User'
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '400':
          description: Invalid username supplied
        '404':
          description: User not found
    put:
      tags:
        - user
      summary: Updated user
      description: This can only be done by the logged in user.
      operationId: updateUser
      parameters:
        - name: username
          in: path
          description: name that need to be updated
          required: true
          schema:
            type: string
      responses:
        '200':
          description: User updated
        '400':
          description: Invalid user supplied
        '404':
          description: User not found
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
        description: Updated user object
        required: true
    delete:
      tags:
        - user
      summary: Delete user
      description: This can only be done by the logged in user.
      operationId: deleteUser
      parameters:
        - name: username
          in: path
          description: The name that needs to be deleted
          required: true
          schema:
            type: string
      responses:
        '200':
          description: User deleted
        '400':
          description: Invalid username supplied
        '404':
          description: User not found
externalDocs:
  description: Find out more
  url: 'https://niis.org'
servers:
  - url: 'https://petstore.niis.org/v2'
  - url: 'http://petstore.niis.org/v2'
components:
  requestBodies:
    UserArray:
      content:
        application/json:
          schema:
            type: array
            items:
              $ref: '#/components/schemas/User'
      description: List of user object
      required: true
    Pet:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Pet'
        application/xml:
          schema:
            $ref: '#/components/schemas/Pet'
      description: Pet object that needs to be added to the store
      required: true
  securitySchemes:
    petstore_auth:
      type: oauth2
      flows:
        implicit:
          authorizationUrl: 'http://petstore.niis.org/oauth/dialog'
          scopes:
            'write:pets': modify pets in your account
            'read:pets': read your pets
    api_key:
      type: apiKey
      name: api_key
      in: header
  schemas:
    Order:
      type: object
      properties:
        id:
          type: integer
          format: int64
        petId:
          type: integer
          format: int64
        quantity:
          type: integer
          format: int32
        shipDate:
          type: string
          format: date-time
        status:
          type: string
          description: Order Status
          enum:
            - placed
            - approved
            - delivered
        complete:
          type: boolean
          default: false
      xml:
        name: Order
    Category:
      type: object
      properties:
        id:
          type: integer
          format: int64
        name:
          type: string
      xml:
        name: Category
    User:
      type: object
      properties:
        id:
          type: integer
          format: int64
        username:
          type: string
        firstName:
          type: string
        lastName:
          type: string
        email:
          type: string
        password:
          type: string
        phone:
          type: string
        userStatus:
          type: integer
          format: int32
          description: User Status
      xml:
        name: User
    Tag:
      type: object
      properties:
        id:
          type: integer
          format: int64
        name:
          type: string
      xml:
        name: Tag
    Pet:
      type: object
      required:
        - name
        - photoUrls
      properties:
        id:
          type: integer
          format: int64
        category:
          $ref: '#/components/schemas/Category'
        name:
          type: string
          example: doggie
        photoUrls:
          type: array
          xml:
            name: photoUrl
            wrapped: true
          items:
            type: string
        tags:
          type: array
          xml:
            name: tag
            wrapped: true
          items:
            $ref: '#/components/schemas/Tag'
        status:
          type: string
          description: pet status in the store
          enum:
            - available
            - pending
            - sold
      xml:
        name: Pet
    ApiResponse:
      type: object
      properties:
        code:
          type: integer
          format: int32
        type:
          type: string
        message:
          type: string
```