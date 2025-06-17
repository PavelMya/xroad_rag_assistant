### 4.1 ERROR: Upgrade supported from version X.Y.Z or newer.

The following error message may come up during the Security Server upgrade.

`ERROR: Upgrade supported from version X.Y.Z or newer.`

Upgrading the packages from the current version to the target version is not supported directly. The fix is to upgrade the Security Server to the target version step by step.

For example, the following Security Server packages are currently installed.

```bash
[root@rh1 ~]# yum list installed | grep xroad
xroad-addon-messagelog.x86_64      7.0.0-1.el7 @artifactory.niis.org_xroad-release-rpm_rhel_7_current 
xroad-addon-metaservices.x86_64    7.0.0-1.el7 @artifactory.niis.org_xroad-release-rpm_rhel_7_current 
xroad-addon-proxymonitor.x86_64    7.0.0-1.el7 @artifactory.niis.org_xroad-release-rpm_rhel_7_current 
xroad-addon-wsdlvalidator.x86_64   7.0.0-1.el7 @artifactory.niis.org_xroad-release-rpm_rhel_7_current 
xroad-base.x86_64                  7.0.0-1.el7 @artifactory.niis.org_xroad-release-rpm_rhel_7_current 
xroad-confclient.x86_64            7.0.0-1.el7 @artifactory.niis.org_xroad-release-rpm_rhel_7_current 
xroad-database-local.noarch        7.0.0-1.el7 @artifactory.niis.org_xroad-release-rpm_rhel_7_current 
xroad-monitor.x86_64               7.0.0-1.el7 @artifactory.niis.org_xroad-release-rpm_rhel_7_current 
xroad-proxy.x86_64                 7.0.0-1.el7 @artifactory.niis.org_xroad-release-rpm_rhel_7_current 
xroad-proxy-ui-api.x86_64          7.0.0-1.el7 @artifactory.niis.org_xroad-release-rpm_rhel_7_current 
xroad-securityserver.noarch        7.0.0-1.el7 @artifactory.niis.org_xroad-release-rpm_rhel_7_current 
xroad-signer.x86_64                7.0.0-1.el7 @artifactory.niis.org_xroad-release-rpm_rhel_7_current 
```

The following packages are available in the repository.

```bash
[root@rh1 ~]# yum --showduplicates list xroad-securityserver
Installed Packages
xroad-securityserver.noarch                                                                        7.0.0-1.el7                                                                         @artifactory.niis.org_xroad-release-rpm_rhel_7_current
Available Packages
xroad-securityserver.noarch                                                                        7.1.0-1.el7                                                                         artifactory.niis.org_xroad-release-rpm_rhel_7_current
xroad-securityserver.noarch                                                                        7.3.0-1.el7                                                                         artifactory.niis.org_xroad-release-rpm_rhel_7_current
```

Now trying to upgrade the Central Server packages directly will produce the following error.

```bash
[root@rh1 ~]# yum upgrade xroad-securityserver
...
ERROR: Upgrade supported from version 7.1.0 or newer.
error: %pre(xroad-securityserver-7.3.0-1.el7.noarch) scriptlet failed, exit status 1
Error in PREIN scriptlet in rpm package xroad-securityserver-7.3.0-1.el7.noarch
```

The fix is to upgrade the Security Server in two separate steps. First, upgrade to 7.1.x with the following command.

```bash
yum install xroad-securityserver-7.1.0-1.el7 xroad-addon-messagelog-7.1.0-1.el7 xroad-addon-metaservices-7.1.0-1.el7 xroad-addon-proxymonitor-7.1.0-1.el7 xroad-addon-wsdlvalidator-7.1.0-1.el7 xroad-base-7.1.0-1.el7 xroad-confclient-7.1.0-1.el7 xroad-database-local-7.1.0-1.el7 xroad-monitor-7.1.0-1.el7 xroad-proxy-7.1.0-1.el7 xroad-proxy-ui-api-7.1.0-1.el7 xroad-securityserver-7.1.0-1.el7 xroad-signer-7.1.0-1.el7
```

An alternative approach to the previous command is to temporarily configure the server to use a repository that contains only the specific version of X-Road software we want to upgrade to. For example, configure the repository as `https://artifactory.niis.org/xroad-release-rpm/rhel/7/7.1.0` and then use the `yum update xroad-securityserver` command.

Finally, we can upgrade to our target version 7.3.x as follows.

```bash
yum update xroad-securityserver
```