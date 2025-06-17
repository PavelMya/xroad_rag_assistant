### 3.3 Configuration

To perform the initial configuration, open the address

    https://SECURITYSERVER:4000/

in a Web browser (**reference data: 1.8; 1.6**). To log in, use the account name chosen during the installation (**reference data: 1.3).**

Upon first log-in, the system asks for the following information.

* The global configuration anchor file (**reference data: 2.1**).

    **Please verify anchor hash value with the published value.**

If the configuration is successfully downloaded, the system asks for the following information.

* The Security Server owner’s member class (**reference data: 2.2**).
* The Security Server owner’s member code (**reference data: 2.3**).

  If the member class and member code are correctly entered, the system displays the Security Server owner’s name as registered in the X-Road center.

* Security Server code (**reference data: 2.4**), which is chosen by the Security Server administrator and which has to be unique across all the Security Servers belonging to the same X-Road member.
* Software token’s PIN (**reference data: 2.5**). The PIN will be used to protect the keys stored in the software token. The PIN must be stored in a secure place, because it will be no longer possible to use or recover the private keys in the token once the PIN has been lost.