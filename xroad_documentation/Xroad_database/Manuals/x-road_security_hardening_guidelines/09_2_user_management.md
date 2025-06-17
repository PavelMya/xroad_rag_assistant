## 2. User management

X-Road uses the Linux Pluggable Authentication Modules (PAM) to authenticate users. This makes it easy to configure the account management to your liking. 
The example PAM configurations provided in this guide may or may not work on your system depending on your system and existing PAM configurations. 
Note that editing the PAM configurations will take effect immediately without the need to restart anything.

For configuring the following security policies for the X-Road components Admin UI in production, please refer to [The Linux-PAM System Administrator's Guide](https://fossies.org/linux/Linux-PAM-docs/doc/sag/Linux-PAM_SAG.pdf) for the full documentation on how to configure PAM.