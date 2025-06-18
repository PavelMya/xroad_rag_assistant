## 10 Time-Stamping

Also related to the security principle of non-repudiation (and integrity), a time-stamping authority enforces use of a time-stamping protocol by Security Servers to ensure long-term proof value of exchanged messages. The issued time stamps certify the existence of the messages at a certain point of time and the Security Servers log all of the messages and their signatures. These logs are periodically time-stamped to create long-term proof.

X-Road uses batch time-stamping (refer to \[[BATCH-TS](#Ref_BATCH-TS)\]). This reduces the load of the time-stamping service. The load does not depend on the number of messages exchanged over the X-Road, rather it depends on the number of Security Servers in the system.

X-Road supports creating time-stamps synchronously for each message too. Using synchronous time-stamping may be a security policy requirement to guarantee the time-stamp at the time of logging the message. However, batch time-stamping is the default for performance and availability reasons.

The time-stamping feature is directly related to message logging. If the message log add-on is disabled, no time-stamping will occur. However, disabling only message body logging does not affect time-stamping.

## 11 Updatability

X-Road is designed to enable reliable installation of software updates including security updates. X-Road software packages are signed so that their origins are traceable.