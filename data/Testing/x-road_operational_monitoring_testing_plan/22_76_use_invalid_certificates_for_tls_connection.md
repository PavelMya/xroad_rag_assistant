### 7.6 Use Invalid Certificates for TLS Connection
Test case for verifying that the secure connection between the security server and the external operational monitoring daemon fails in case invalid certificates are configured for the TLS connection.

**Preconditions:**
* A secure connection has been configured between security server *xtee10.ci.kit* and external monitoring daemon *xtee11.ci.kit*. Note that the correct operational monitoring TLS certificate should be kept in security server *xtee10.ci.kit* for use after scenarios 1, 2 and 3 have been carried out.

**Test scenarios:**
1. Configure an invalid operational monitoring daemon TLS certificate in security server *xtee10.ci.kit*.
  * Replace the value of the parameter `tls-certificate` in the `[op-monitor]` section of the file `/etc/xroad/conf.d/local.ini` with a path to an invalid certificate. The example invalid certificate can be found in the source repository of the project at `src/systemtest/op-monitoring/misc/invalid_certificate.crt`.
  * Restart the proxy (`sudo service xroad-proxy restart`).
  * Send a health data request to security server *xtee10.ci.kit*. The example request can be found in the source repository of the project at `src/systemtest/op-monitoring/requests/health_data_ss2.query`.

  **Expected output:**
  * A SOAP fault is received as a health data query response (faultstring: java.security.cert.CertificateException: Operational monitoring daemon certificate not loaded, cannot verify server).
  * After restarting the proxy the following error is logged once in the proxy log in security server *xtee10.ci.kit*:
    * Could not load operational monitoring daemon certificate '&lt;file path&gt;'.
  * The following error messages are logged in the proxy log in security server *xtee10.ci.kit*:
    * Request processing error;
    * Sending operational monitoring data failed;
    * Operational monitoring daemon certificate not loaded, cannot verify server.
  * The following warning is logged in the monitoring daemon log in monitoring daemon *xtee11.ci.kit*:
    * Received fatal alert: certificate_unknown.

2. Configure an incorrect operational monitoring daemon TLS certificate in security server *xtee10.ci.kit*.
  * Generate the monitoring daemon certificate in security server *xtee9.ci.kit* (use the command `generate-opmonitor-certificate`).
  * In security server *xtee10.ci.kit*, replace the value of the parameter `tls-certificate` in the `[op-monitor]` section of the file `/etc/xroad/conf.d/local.ini` with a path to the monitoring daemon certificate of security server *xtee9.ci.kit* generated in the previous step.
  * Restart the proxy (`sudo service xroad-proxy restart`).
  * Send a health data request to security server *xtee10.ci.kit*.

  **Expected output:**
  * A SOAP fault is received as a health data query response (faultstring: java.security.cert.CertificateException: Server TLS certificate does not match expected operational monitoring daemon certificate).
  * The following error messages are logged in the proxy log in security server *xtee10.ci.kit*:
    * Request processing error;
    * Sending operational monitoring data failed;
    * Server TLS certificate does not match expected operational monitoring daemon certificate.
  * The following warning is logged in the monitoring daemon log in monitoring daemon *xtee11.ci.kit*:
    * Received fatal alert: certificate_unknown.

3. Configure a non-existent operational monitoring daemon TLS certificate in security server *xtee10.ci.kit*.
  * In security server *xtee10.ci.kit*, replace the value of the parameter `tls-certificate` in the `[op-monitor]` section of the file `/etc/xroad/conf.d/local.ini` with a path to a non-existent file.
  * Restart the proxy (`sudo service xroad-proxy restart`).
  * Send a health data request to security server *xtee10.ci.kit*.

  **Expected output:**
  * A SOAP fault is received as a health data query response (faultstring: java.security.cert.CertificateException: Operational monitoring daemon certificate not loaded, cannot verify server).
  * After restarting the proxy the following error is logged once in the proxy log in security server *xtee10.ci.kit*:
    * Could not load operational monitoring daemon certificate '&lt;file path&gt;' (No such file or directory)
  * The following error messages are logged in the proxy log in security server *xtee10.ci.kit*:
    * Request processing error;
    * Sending operational monitoring data failed;
    * Operational monitoring daemon certificate not loaded, cannot verify server.
  * The following warning is logged in the monitoring daemon log in monitoring daemon *xtee11.ci.kit*:
    * Received fatal alert: certificate_unknown.

  *After this test, restore the communication between the security server and the operational monitoring daemon (to achieve the precondition of this test case).*
    * Configure the correct operational monitoring daemon TLS certificate in security server *xtee10.ci.kit*
    * Restart the proxy (`sudo service xroad-proxy restart`).

4. Configure an invalid security server TLS certificate in operational monitoring daemon *xtee11.ci.kit*.
  * Replace the value of the parameter `client-tls-certificate` in the `[op-monitor]` section of the file `/etc/xroad/conf.d/local.ini` with a path to an invalid certificate. The example invalid certificate can be found in the source repository of the project at `src/systemtest/op-monitoring/misc/invalid_certificate.crt`.
  * Restart the monitoring daemon (`sudo service xroad-opmonitor restart`).
  * Send a health data request to security server *xtee10.ci.kit*.

  **Expected output:**
  * A SOAP fault is received as a health data query response (faultstring: Remote host closed connection during handshake).
  * The following error messages are logged in the proxy log in security server *xtee10.ci.kit*:
    * Request processing error;
    * Sending operational monitoring data failed;
    * Remote host closed connection during handshake.
  * After restarting the monitoring daemon the following error is logged once in the monitoring daemon log in monitoring daemon *xtee11.ci.kit*:
    * Could not load client certificate '&lt;file path&gt;'

5. Configure an incorrect security server TLS certificate in operational monitoring daemon *xtee11.ci.kit*.
  * In security server *xtee9.ci.kit*, the security server internal certificate can be found in `/etc/xroad/ssl/internal.crt`.
  * In monitoring daemon *xtee11.ci.kit*, replace the value of the parameter `client-tls-certificate` in the `[op-monitor]` section of the file `/etc/xroad/conf.d/local.ini` with the path to the security server certificate of security server *xtee9.ci.kit* refered to in the previous step.
  * Restart the monitoring daemon (`sudo service xroad-opmonitor restart`).
  * Send a health data request to security server *xtee10.ci.kit*.

  **Expected output:**
  * A SOAP fault is received as a health data query response (faultstring: Remote host closed connection during handshake).
  * The following error messages are logged in the proxy log in security server *xtee10.ci.kit*:
    * Request processing error;
    * Sending operational monitoring data failed;
    * Remote host closed connection during handshake.
  * The following warning is logged in the monitoring daemon log in monitoring daemon *xtee11.ci.kit*:
    * General SSLEngine problem.

6. Configure a non-existent security server TLS certificate in operational monitoring daemon *xtee11.ci.kit*.
  *  In monitoring daemon *xtee11.ci.kit*, replace the value of the parameter `client-tls-certificate` in the `[op-monitor]` section of the file `/etc/xroad/conf.d/local.ini` with a path to a non-existent file.
  * Restart the monitoring daemon (`sudo service xroad-opmonitor restart`).
  * Send a health data request to security server *xtee10.ci.kit*.

  **Expected output:**
  * A SOAP fault is received as a health data query response (faultstring: Remote host closed connection during handshake).
  * The following error messages are logged in the proxy log in security server *xtee10.ci.kit*:
    * Request processing error;
    * Sending operational monitoring data failed;
    * Remote host closed connection during handshake.
  * After restarting the monitoring daemon the following error is logged once in the monitoring daemon log in monitoring daemon *xtee11.ci.kit*:
    * Could not load client certificate '&lt;file path&gt;' (No such file or directory)