#### 15.2.4 Installing an External Operational Monitoring Daemon

Technically, the operational monitoring daemon can be installed on a separate host from the Security Server. It is possible to configure several Security Servers to use that external operational monitoring daemon, but this setup is correct *only* if the Security Servers are identical clones installed behind a load balancer.

**NOTE:** The setup of clustered Security Servers is not officially supported yet and has been implemented for future compatibility.

**NOTE:** It is **strongly advised** to use HTTPS for requests between a Security Server and the associated external operational monitoring daemon.

For running a separate operational monitoring daemon, the xroad-opmonitor package must be installed. Please refer to \[[IG-SS](#Ref_IG-SS)\] for general instructions on obtaining X-Road packages.

As a result of installation, the following services will be running:

    xroad-confclient
    xroad-signer
    xroad-opmonitor