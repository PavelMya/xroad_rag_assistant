#### 2.3.1 Installing Java 21

Java 21 is a prerequisite for running the Security Server and should be installed prior installing/updating Security Server, however it is not included in default repositories for RHEL 7.
Sample installation steps are provided below.

* Check the current java version:

        java -version

If the current Java version is 21, following steps should be skipped. If not, install Java 21 (OpenJDK):

        sudo yum install openjdk-21-jre-headless

After the installation, verify the current java version:
    
        java -version

The output should contain Java version 21. If it does not, set the default Java version to 21 using *alternatives*:

        sudo alternatives --config java

### 2.4 Preparing OS

* Set the operating system locale. Add following line to the `/etc/environment` file.

        LC_ALL=en_US.UTF-8

* Install `yum-utils`, a collection of utilities that integrate with yum to extend its native features.

        sudo yum install yum-utils