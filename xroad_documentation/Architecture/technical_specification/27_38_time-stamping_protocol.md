### 3.8 Time-Stamping Protocol

The Time-stamping protocol (see \[[TSP](#Ref_TSP)\]) is used by security servers to ensure long-term proof value of the exchanged messages. The security servers log all the messages and their signatures. These logs are periodically time-stamped to create long-term proof.

Time-stamping protocol is a synchronous protocol that is provided by the time-stamp authority. However, the security servers use the time-stamping protocol in an asynchronous manner. Security servers log all the messages that are exchanged with other security servers. These messages are time-stamped asynchronously using batch time-stamping (see \[[BATCH-TS](#Ref_BATCH-TS)\]). This is done to decouple availability of the message exchange from availability of the time-stamping authority, to decrease the latency of message exchange, and to reduce load on the time-stamping authority.

Because time-stamping is used in an asynchronous manner, temporary unavailability of the time-stamping service does not directly affect the X-Road message exchange. However, if the security servers fail to time-stamp the accumulated messages for certain time period then it may become difficult to prove the exact time of the message exchanges. To minimize this risk the security servers will stop forwarding messages if the time-stamping has been failing for some time. The maximum allowed time period between logging of a message and acquiring a time stamp for that message is defined by the owner of the central server and can very between different instances of X-Road.

### 3.9 Security Server User Interface

The security server user interface is used by the security server administrator to configure and manage the security server.

### 3.10 Central Server User Interface

The central server user interface is used by the central server administrator to configure and manage the central server.