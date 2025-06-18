### 4.5 Different versions of xroad-\* packages after successful upgrade

Sometimes, after using `sudo apt-get upgrade` command, some of the packages are not upgraded. In the following example `xroad-securityserver` package version is still 6.8.3 although other packages are upgraded to 6.8.5:

    # sudo dpkg -l | grep xroad-
    ii xroad-addon-messagelog 6.8.5.20160929134539gitfe60f90
    ii xroad-addon-metaservices 6.8.5.20160929134539gitfe60f90
    ii xroad-addon-wsdlvalidator 6.8.5.20160929134539gitfe60f90
    ii xroad-common 6.8.5.20160929134539gitfe60f90
    ii xroad-jetty9 6.8.5.20160929134539gitfe60f90
    ii xroad-proxy 6.8.5.20160929134539gitfe60f90
    ii xroad-securityserver 6.8.3-3-201605131138

`apt-get upgrade` command doesn’t install new packages - in this particular case new packages `xroad-monitor` and `xroad-addon-proxymonitor` installation is needed for upgrade of `xroad-securityserver` package.

To be sure that packages are installed correctly please use `sudo apt upgrade` or `sudo apt full-upgrade` commands.