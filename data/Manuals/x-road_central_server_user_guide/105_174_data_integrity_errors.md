### 17.4 Data Integrity errors

An error response from the REST API can include data integrity errors if incorrect data was provided with the request.
When

Example request and response of adding a new member when member already exist:
```
POST https://cs:4000/api/v1/members

Request body:
{
    "member_name": "Member",
    "member_id": {
        "member_class": "ORG",
        "member_code": "MemberCode"
    }
}

Response body:
{
    "status": 409,
    "error": {
        "code": "member_exists",
        "metadata": [
            "CS/ORG/MemberCode"
        ]
    }
}
```

Possible data integrity error codes and messages declared in [Central Server ErrorMessage](https://github.com/nordic-institute/X-Road/blob/develop/src/central-server/admin-service/core-api/src/main/java/org/niis/xroad/cs/admin/api/exception/ErrorMessage.java)