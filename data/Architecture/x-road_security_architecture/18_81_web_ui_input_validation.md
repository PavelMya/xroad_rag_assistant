### 8.1 Web UI Input Validation

User input parsing is enforced in the Central Server UI and the Security Server UI, whereby there is removal of leading and trailing whitespaces, verification that that all mandatory fields are filled, and verification that the user input does not exceed 255 characters.

If one or more mandatory fields are not filled, it results in a “Missing parameter: 'X'" error message. If  user input exceeds 255 characters, it results in a “Parameter 'X' input exceeds 255 characters” error message.