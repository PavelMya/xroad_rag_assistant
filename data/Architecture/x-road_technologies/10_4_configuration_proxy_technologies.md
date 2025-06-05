## 4 Configuration proxy technologies

[Table 3](#Ref_Technology_matrix_of_the_configuration) presents the list of technologies used in the configuration proxy and the mapping between technologies and configuration proxy components.

<a id="Ref_Technology_matrix_of_the_configuration" class="anchor"></a>
Table 3. Technology matrix of the configuration proxy

| **Technology**           | **Web Server** | **Configuration Processor** | **Signer** | **Configuration Client** |
|--------------------------|:--------------:|:---------------------------:|:----------:|:------------------------:|
| Java 21                  |                |              X              |     X      |            X             |
| Logback                  |                |              X              |     X      |            X             |
| gRPC                     |                |              X              |     X      |                          |
| nginx                    |       X        |                             |            |                          |
| systemd                  |       X        |              X              |     X      |            X             |
| PKCS \#11\[[2](#Ref_2)\] |                |                             |     X      |                          |

<a id="Ref_2" class="anchor"></a>
\[2\] The use of hardware cryptographic devices requires that a PKCS \#11 driver is installed and configured in the system.

See [[ARC-CP]](#ARC-CP) for the configuration proxy details.