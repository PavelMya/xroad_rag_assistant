### 2.3 Ensuring User Account Security

Users of the web application are created by creating operating-system-level users. This means that a user can access the web application and the underlying operating system with the same credentials. 
Therefore, if user accounts in the web application were compromised, the attacker could use those credentials to log into the server via SSH if credential-based logging in is not disabled.

To harden the user account security, make sure that users are not allowed to access the server via SSH by default. The users needing SSH access are granted those rights separately.

1. Create a user group in which users are allowed to connect to the server via SSH while all other users are denied.
2. Add users which should have SSH access to newly created group.
3. Add the following line to `/etc/ssh/sshd_config`:
     
        AllowGroups <group_to_allow>

4. Restart the SSH service:

        sudo systemctl restart sshd

It is also recommended to disable SSH password login and allow key-based authentication only. Before this modification, add users' public keys to the server. Edit `/etc/ssh/sshd_config` and add the following lines:

    ChallengeResponseAuthentication no
    PasswordAuthentication no

Restart the SSH service once again:

    sudo systemctl restart sshd

In addition, the users should be prevented from logging in to the system. This can be achieved by issuing the following command on Ubuntu:

    usermod -s /bin/false user

On RHEL, the corresponding command is:

    usermod -s /sbin/nologin user

The system administrator should also implement a monitoring and alerting system regarding anomalous logins.