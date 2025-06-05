### 2.5 Setup Package Repository

Add X-Road package repository (**reference data: 1.1**) and Extra Packages for Enterprise Linux (EPEL) repository:

  ```bash
  RHEL_MAJOR_VERSION=$(source /etc/os-release;echo ${VERSION_ID%.*})
  sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-${RHEL_MAJOR_VERSION}.noarch.rpm
  sudo yum-config-manager --add-repo https://artifactory.niis.org/xroad-release-rpm/rhel/${RHEL_MAJOR_VERSION}/current
  ```

The following packages are fetched from EPEL: `crudini`, and `rlwrap`.

Add the X-Road repository’s signing key to the list of trusted keys (**reference data: 1.2**):

  ```bash
  sudo rpm --import https://artifactory.niis.org/api/gpg/key/public
  ```