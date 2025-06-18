### 2.4 Time-Stamping Authority

The time-stamping authority issues time stamps that certify the existence of data items at a certain point of time. The time-stamping authority must implement the time-stamping protocol described in Section [3.8](#38-time-stamping-protocol).

X-Road uses batch time-stamping (see \[[BATCH-TS](#Ref_BATCH-TS)\]). This reduces the load of the time-stamping service. The load does not depend on the number of messages exchanged over the X-Road, instead it depends on the number of security servers in the system.