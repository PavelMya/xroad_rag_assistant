### 2.4 Preparing OS

- Add an X-Road system administrator user (reference data: 1.3) whom all roles in the user interface are granted to. 

  Add the new user with the command: `sudo adduser username`.

  User roles are discussed in detail in the X-Road Security Server User Guide [UG-SS](#Ref_UG-SS). Do not use the user name `xroad`, it is reserved for the X-Road system user.

- Ensure that the packages `locales` and `software-properties-common` are present
  
  `sudo apt install locales software-properties-common`

- Set the operating system locale.

  Add the following line to the file `/etc/environment`: `LC_ALL=en_US.UTF-8`  
  Ensure that the locale is generated: `sudo locale-gen en_US.UTF-8`