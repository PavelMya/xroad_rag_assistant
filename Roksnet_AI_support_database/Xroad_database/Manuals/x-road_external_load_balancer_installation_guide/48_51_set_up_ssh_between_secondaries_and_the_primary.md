### 5.1 Set up SSH between secondaries and the primary

On the primary, set up a system user that can read `/etc/xroad`. A system user has their password disabled and can not log
in normally.

**Ubuntu:**

```bash
adduser --system --shell /bin/bash --ingroup xroad --home /home/xroad-slave xroad-slave
```
**RHEL:**

```bash
useradd -r -m -g xroad xroad-slave
```

Create an `.ssh` folder and the authorized keys file:
```bash
sudo mkdir -m 755 -p /home/xroad-slave/.ssh && sudo touch /home/xroad-slave/.ssh/authorized_keys
```
**Warning:**  The owner of the file should be `root` and `xroad-slave` should not have write permission to the file.

On the secondary nodes, create an ssh key (`ssh-keygen`) without a passphrase for the `xroad` user and add the public keys in
the `/home/xroad-slave/.ssh/authorized_keys` of the primary node. To finish, from secondary nodes, connect to the primary host
using `ssh` and accept the host key.