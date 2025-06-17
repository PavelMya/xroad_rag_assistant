### 2.1 Usage

1. Install the package
  * Ubuntu: apt install xroad-autologin
  * RedHat: yum install xroad-autologin

2. If storing the PIN code on the server in plaintext is acceptable, create file `/etc/xroad/autologin` that contains the PIN code. 
  * File should be readable by user `xroad`
  * If `/etc/xroad/autologin` does not exists, and you have not implemented `custom-fetch-pin.sh`, the service will not start
3. If you do not want to store PIN code in plaintext, implement bash script 
`/usr/share/xroad/autologin/custom-fetch-pin.sh`
  * The script needs to output the PIN code to stdout
  * Script should be readable and executable by user `xroad`
  * Script should exit with exit code
    * 0 if it was able to fetch PIN code successfully
    * 127 if it was not able to fetch PIN code, but this is not an actual error that should cause the service to fail (default implementation uses this if `/etc/xroad/autologin` does not exist)
    * other exit codes in error situations that should cause the service to fail
  ```bash
  #!/bin/bash
  PIN_CODE=$(curl https://some-address)
  echo "${PIN_CODE}"
  exit 0
  ```