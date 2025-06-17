### 17.5 Warning responses

Error response from the Management API can include additional warnings that you can ignore if seen necessary. The warnings can be ignored by your decision, by executing the same operation with `ignore_warnings` boolean parameter set to `true`. *Always consider the warning before making the decision to ignore it.*

An example case:
1. Client executes a REST request, without `ignore_warnings` parameter, to backend.
2. Backend notices warnings and responds with error message that contains the warnings. Nothing is updated at this point.
3. Client determines if warnings can be ignored.
4. If the warnings can be ignored, client resends the REST request, but with `ignore_warnings` parameter set to `true`.
5. Backend ignores the warnings and executes the operation.

Error response with warnings always contains the error code `warnings_detected`.

Like errors, warnings contain an identifier (code) and possibly some metadata.

Warning example when trying to upload backup file which already exist produces non-fatal validation warnings:
```
POST https://cs:4000/api/v1/backups/upload?ignore_warnings=false

Response:
{
  "status": 400,
  "error": {
    "code": "warnings_detected"
  },
  "warnings": [
    {
      "code": "warning_file_already_exists",
      "metadata": [
        "backup.gpg"
      ]
    }
  ]
}
```

Note that when you are using the admin UI and you encounter warnings, you will always be provided with a popup window with a `CONTINUE` button in it. When you click the `CONTINUE` button in the popup, the request is sent again but this time warnings will be ignored.