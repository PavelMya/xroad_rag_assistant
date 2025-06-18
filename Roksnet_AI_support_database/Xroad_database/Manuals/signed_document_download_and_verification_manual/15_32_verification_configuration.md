### 3.2 Verification Configuration

The asicverifier tool requires the proper verification configuration containing certificates needed by the verification process. The verification configuration can be downloaded from the same security server by making a HTTP GET request to the URL:

    http://SECURITYSERVER/verificationconf

where `SECURITYSERVER` is the actual address of the security server.

The *verificationconf* service has no parameters and responds with a ZIP archive (content-type `application/zip`, filename `verificationconf.zip`). This archive needs to be extracted and the location of it's contents used as an argument to the asicverifier tool.

A convenient way to download the verification configuration is with the web browser or use of the curl tool:

    curl -J -O http://sec1.gov/verificationconf