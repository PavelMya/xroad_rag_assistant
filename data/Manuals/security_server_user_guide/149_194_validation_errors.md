### 19.4 Validation errors

An error response from the REST API can include validation errors if an unsupported parameter was provided with the request.
When

Example request and response of adding a new subsystem with illegal characters:
```
POST https://ss1:4100/api/v1/clients

Request body:
{
  "client": {
    "member_class": "ORG",
    "member_code": "0/1234",
    "subsystem_code": "Subsystem%Code"
  },
  "ignore_warnings": false
}

Response body:
{
  "error": {
    "code": "validation_failure",
    "validation_errors": {
      "clientAdd.client.memberCode": [
        "NoForwardslashes"
      ],
      "clientAdd.client.subsystemCode": [
        "NoPercents"
      ]
    }
  },
  "status": 400
}
```

In addition to the validation messages declared in [Java Validation API](https://javaee.github.io/javaee-spec/javadocs/javax/validation/constraints/package-summary.html), the following validation errors are possible:

| Error              | Explanation                                                                                                                 |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `NoControlChars`   | The provided string contains [ISO control characters](https://en.wikipedia.org/wiki/Control_character) or zero-width spaces |
| `NoColons`         | The provided string contains colons `:`                                                                                     |
| `NoSemicolons`     | The provided string contains semicolons `;`                                                                                 |
| `NoForwardslashes` | The provided string contains slashes `/`                                                                                    |
| `NoBackslashes`    | The provided string contains backslashes `\`                                                                                |
| `NoPercents`       | The provided string contains percent symbol `%`                                                                             |