### 2.5 Installation

To install the X-Road Configuration Proxy software, follow these steps.

1.  Add the X-Road repository’s signing key to the list of trusted keys (**reference data: 1.2**):

        curl https://artifactory.niis.org/api/gpg/key/public | sudo apt-key add -

2.  Add X-Road package repository (**reference data: 1.1**)

        sudo apt-add-repository -y "deb https://artifactory.niis.org/xroad-release-deb $(lsb_release -sc)-current main"

3.  Issue the following commands to install the Configuration Proxy packages:

            sudo apt-get update
            sudo apt-get install xroad-confproxy