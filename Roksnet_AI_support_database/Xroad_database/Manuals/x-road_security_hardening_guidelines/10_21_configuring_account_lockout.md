### 2.1 Configuring account lockout

Configuring an account lockout policy in your Admin UI authentication will provide an extra layer of defence against password guessing attacks, such as brute force attacks. 
After configuring the account lockout, when trying to log in to the Admin UI with a locked account, the login screen will display a generic login error without disclosing the reason or any other login information.

The PAM service to configure the account lockout to is `xroad`.

#### 2.1.1 Considerations and risks

After enabling the account lockout for the X-Road component, you should be aware that a user can lock out any other user's account if they know the correct username.