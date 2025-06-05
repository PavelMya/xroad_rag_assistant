### 2.4 Preparing OS

* Set the operating system locale. Add following line to the `/etc/environment` file.

        LC_ALL=en_US.UTF-8

* Install `yum-utils`, a collection of utilities that integrate with yum to extend its native features.

        sudo yum install yum-utils