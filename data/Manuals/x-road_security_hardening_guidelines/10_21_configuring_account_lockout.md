### 2.1 Configuring account lockout

Configuring an account lockout policy in your Admin UI authentication will provide an extra layer of defence against password guessing attacks, such as brute force attacks. 
After configuring the account lockout, when trying to log in to the Admin UI with a locked account, the login screen will display a generic login error without disclosing the reason or any other login information.

The PAM service to configure the account lockout to is `xroad`.