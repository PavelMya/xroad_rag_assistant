### 2.7 Versioning

The current version of the configuration is 5.

Configuration source MAY support several versions of the configuration. The configuration client SHOULD signal the version it supports by appending a "version" query parameter in the download URI specified in the configuration anchor. The version number is an integer which is incremented when a backwards-incompatible change is made to the PRIVATE-PARAMETERS or SHARED-PARAMETERS configuration part.

For backwards compatibility, the configuration source MAY return a default version of the configuration if the version query parameter is not present. The configuration source MUST respond with HTTP error code 404 (Not Found) if the client requests a version that is not available.