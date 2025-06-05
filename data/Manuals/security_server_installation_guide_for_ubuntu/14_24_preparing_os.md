### 2.4 Preparing OS

* Add an X-Road system administrator user (**reference data: 1.3**) whom all roles in the user interface are granted to. Add a new user with the command

        sudo adduser <username>

    User roles are discussed in detail in X-Road Security Server User Guide \[[UG-SS](#Ref_UG-SS)\]. Do not use the user name `xroad`, it is reserved for the X-Road system user.

* Set the operating system locale. Add following line to the `/etc/environment` file.

        LC_ALL=en_US.UTF-8

* Ensure that the packages `locales` and `software-properties-common` are present

        sudo apt-get install locales software-properties-common

* Ensure that the locale is available

        sudo locale-gen en_US.UTF-8