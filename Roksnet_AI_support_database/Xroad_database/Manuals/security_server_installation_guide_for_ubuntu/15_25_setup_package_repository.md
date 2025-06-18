### 2.5 Setup Package Repository

Add the X-Road repository’s signing key to the list of trusted keys (**reference data: 1.2**):
```bash
curl https://artifactory.niis.org/api/gpg/key/public | sudo apt-key add -
```

Add X-Road package repository (**reference data: 1.1**)
```bash
sudo apt-add-repository -y "deb https://artifactory.niis.org/xroad-release-deb $(lsb_release -sc)-current main"
```

Update package repository metadata:
```bash
sudo apt update
```

If you are installing the default setup with local PostgreSQL database and want to enable the messagelog addon, continue at section 2.8. If you need to customize database properties and e.g. use a remote database or disable the messagelog addon, read on.