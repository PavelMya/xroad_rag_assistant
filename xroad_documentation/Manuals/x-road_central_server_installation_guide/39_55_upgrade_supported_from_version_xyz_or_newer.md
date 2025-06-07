### 5.5 Upgrade supported from version X.Y.Z or newer

The following error message may come up during the Central Server upgrade.

`Upgrade supported from version X.Y.Z or newer`

Upgrading the packages from the current version to the target version is not supported directly. The fix is to upgrade the Central Server to the target version step by step.

For example, the following Central Server packages are currently installed.

```bash
root@test-cs:~# dpkg -l | grep xroad
ii  xroad-autologin                    7.3.0-1.ubuntu22.04 all          Automatic token pin code entry
ii  xroad-base                         7.3.0-1.ubuntu22.04 amd64        X-Road base components
ii  xroad-center                       7.3.0-1.ubuntu22.04 all          X-Road central server
ii  xroad-center-management-service    7.3.0-1.ubuntu22.04 all          X-Road Central Server Management Service
ii  xroad-center-registration-service  7.3.0-1.ubuntu22.04 all          X-Road Central Server Registration Service
ii  xroad-centralserver                7.3.0-1.ubuntu22.04 all          X-Road central server
ii  xroad-centralserver-monitoring     7.3.0-1.ubuntu22.04 all          Monitoring client configuration for X-Road central
ii  xroad-confclient                   7.3.0-1.ubuntu22.04 amd64        X-Road configuration client components
ii  xroad-database-remote              7.3.0-1.ubuntu22.04 all          Meta-package for X-Road remote database dependencies
rc  xroad-jetty9                       7.3.0-1.ubuntu22.04 all          Jetty9 for X-Road purposes
ii  xroad-nginx                        7.3.0-1.ubuntu22.04 amd64        X-Road nginx component
ii  xroad-signer                       7.3.0-1.ubuntu22.04 amd64        X-Road signer component
```

The following packages are available in the repository.

```bash
root@test-cs:~# apt-cache madison xroad-centralserver
xroad-centralserver | 7.3.0-1.ubuntu20.04 | https://artifactory.niis.org/xroad-release-deb focal-current/main amd64 Packages
xroad-centralserver | 7.1.2-1.ubuntu20.04 | https://artifactory.niis.org/xroad-release-deb focal-current/main amd64 Packages
```

Now trying to upgrade the Central Server packages directly will produce the following error.

```bash
root@test-cs:~# apt upgrade xroad-centralserver
...
Preparing to unpack .../xroad-centralserver_7.3.0-1.ubuntu20.04_all.deb ...
ERROR: Upgrade supported from version 7.1.2 or newer
```

The fix is to upgrade the Central Server in two separate steps. First, upgrade to 7.1.x with the following command.

```bash
apt install xroad-base=7.1.2-1.ubuntu20.04 xroad-center=7.1.2-1.20.04 xroad-centralserver=7.1.2-1.ubuntu20.04 xroad-centralserver-monitoring=7.1.2-1.ubuntu20.04 xroad-confclient=7.1.2-1.ubuntu20.04 xroad-database-local=7.1.2-1.ubuntu20.04 xroad-jetty9=7.1.2-1.ubuntu20.04 xroad-nginx=7.1.2-1.ubuntu20.04 xroad-signer=7.1.2-1.ubuntu20.04
```

An alternative approach to the previous command is to temporarily configure the server to use a repository that contains only the specific version of X-Road software we want to upgrade to. For example, configure the repository as `deb https://artifactory.niis.org/xroad-release-deb focal-7.1.2 main` and then use the `apt update` and `apt upgrade xroad-centralserver` commands.

Finally, we can upgrade to our target version 7.3.x as follows.

```bash
apt upgrade xroad-centralserver
```