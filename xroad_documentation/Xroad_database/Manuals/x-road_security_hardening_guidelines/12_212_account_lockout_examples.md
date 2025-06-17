#### 2.1.2 Account lockout examples

The example configurations will lock the user's account, preventing login to the Admin UI for 15 minutes (I.e. 900 seconds) after they provide a wrong password in the Admin UI login three (3) consecutive times. This configuration also affects the root account.

**Example on Ubuntu**

Create a new configuration `/etc/pam.d/xroad` with the following content:
```shell
auth        required          pam_tally2.so deny=3 even_deny_root unlock_time=900 file=/var/lib/xroad/tallylog
@include    common-auth    
account     required          pam_tally2.so
@include    common-account
password    required          pam_deny.so    
session     required          pam_deny.so    
```

**Example on RHEL**

On RHEL systems, the `/etc/pam.d/xroad` file ships with the installation package so you need to modify the existing file. Replace the `/etc/pam.d/xroad` contents with the following:
```shell
#%PAM-1.0
auth       required     pam_tally2.so deny=3 even_deny_root unlock_time=900 file=/var/lib/xroad/tallylog
auth       required     pam_unix.so
account    required     pam_tally2.so
account    required     pam_unix.so
password   required     pam_deny.so
password   required     pam_warn.so
session    required     pam_deny.so
```