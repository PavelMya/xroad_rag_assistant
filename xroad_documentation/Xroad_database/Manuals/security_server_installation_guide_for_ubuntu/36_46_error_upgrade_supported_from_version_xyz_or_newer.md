### 4.6 ERROR: Upgrade supported from version X.Y.Z or newer

The following error message may come up during the Security Server upgrade.

`ERROR: Upgrade supported from version X.Y.Z or newer`

Upgrading the packages from the current version to the target version is not supported directly. The fix is to upgrade the Security Server to the target version step by step.

For example, the following Security Server packages are currently installed.

```bash
root@test-ss:~# dpkg -l | grep xroad
ii  xroad-addon-messagelog          7.1.2-1.ubuntu20.04 all          X-Road AddOn: messagelog
ii  xroad-addon-metaservices        7.1.2-1.ubuntu20.04 all          X-Road AddOn: metaservices
ii  xroad-addon-proxymonitor        7.1.2-1.ubuntu20.04 all          X-Road AddOn: proxy monitoring metaservice
ii  xroad-addon-wsdlvalidator       7.1.2-1.ubuntu20.04 all          X-Road AddOn: wsdlvalidator
ii  xroad-base                      7.1.2-1.ubuntu20.04 amd64        X-Road base components
ii  xroad-confclient                7.1.2-1.ubuntu20.04 amd64        X-Road configuration client components
ii  xroad-database-local            7.1.2-1.ubuntu20.04 all          Meta-package for X-Road local database dependencies
ii  xroad-monitor                   7.1.2-1.ubuntu20.04 all          X-Road monitoring service
ii  xroad-proxy                     7.1.2-1.ubuntu20.04 all          X-Road security server
ii  xroad-proxy-ui-api              7.1.2-1.ubuntu20.04 all          X-Road proxy UI REST API
ii  xroad-securityserver            7.1.2-1.ubuntu20.04 all          X-Road security server
ii  xroad-signer                    7.1.2-1.ubuntu20.04 amd64        X-Road signer component
```

The following packages are available in the repository.

```bash
root@test-ss:~# apt-cache madison xroad-securityserver
xroad-securityserver | 7.3.0-1.ubuntu20.04 | https://artifactory.niis.org/xroad-release-deb focal-current/main amd64 Packages
xroad-securityserver | 7.1.2-1.ubuntu20.04 | https://artifactory.niis.org/xroad-release-deb focal-current/main amd64 Packages
```

Now trying to upgrade the Security Server packages directly will produce the following error.

```bash
root@test-ss:~# apt-get upgrade xroad-securityserver
...
Preparing to unpack .../0-xroad-securityserver_7.3.0-1.ubuntu20.04_all.deb ...
ERROR: Upgrade supported from version 7.1.2 or newer.
```

The fix is to upgrade the Security Server in two separate steps. First, upgrade to 7.1.x with the following command.

```bash
apt install xroad-securityserver=7.1.2-1.ubuntu20.04 xroad-proxy=7.1.2-1.ubuntu20.04 xroad-monitor=7.1.2-1.ubuntu20.04 xroad-addon-metaservices=7.1.2-1.ubuntu20.04 xroad-addon-messagelog=7.1.2-1.ubuntu20.04 xroad-addon-proxymonitor=7.1.2-1.ubuntu20.04 xroad-addon-wsdlvalidator=7.1.2-1.ubuntu20.04 xroad-proxy-ui-api=7.1.2-1.ubuntu20.04 xroad-confclient=7.1.2-1.ubuntu20.04 xroad-signer=7.1.2-1.ubuntu20.04 xroad-database-local=7.1.2-1.ubuntu20.04 xroad-base=7.1.2-1.ubuntu20.04
```

An alternative approach to the previous command is to temporarily configure the server to use a repository that contains only the specific version of X-Road software we want to upgrade to. For example, configure the repository as `deb https://artifactory.niis.org/xroad-release-deb focal-7.1.2 main` and then use the `apt update` and `apt upgrade xroad-centralserver` commands.

Finally, we can upgrade to our target version 7.3.x as follows.

```bash
apt upgrade xroad-securityserver
```

## Annex A Security Server Default Database Properties

`/etc/xroad/db.properties`

```properties