### C.4 High Availability Setup

In production systems it's rarely acceptable to have a single point of failure. Security Server supports provider side high availability setup via so called internal load balancing mechanism. The setup works so that the same member / member class / member code / subsystem / service code is configured on multiple Security Servers and X-Road will then route the request to the server that responds the fastest. Note that this deployment option does not provide performance benefits, just redundancy.

![Security Server high-availability setup](img/ig-ss_high_availability.svg)