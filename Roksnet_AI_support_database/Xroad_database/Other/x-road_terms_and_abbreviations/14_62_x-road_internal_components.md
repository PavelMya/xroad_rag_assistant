### 6.2 X-Road internal components

**Central components** – are central server and configuration proxy.

**Central server** – the component that manages all registrations of a local X-Road instance (security servers, members, subsystems). It is the primary configuration source in an X-Road system. Central server always manages an internal configuration source (i.e. configuration source distributing the internal configuration) and in addition, an external configuration source (i.e. configuration source distributing the external configuration) in case the X-Road system is federation-capable.  

**Configuration proxy** – an intermediary that may optionally be used to mediate configuration originating from the central server to the configuration clients. Configuration proxy manages configuration sources that are used to distribute configuration downloaded from other configuration sources.
  - **Configuration proxy instance** – a process within the configuration proxy that deals with distributing the global configuration files of a specific X-Road instance.

**Security server** – standard software solution for using secure data exchange channel of X-Road and ensuring confidentiality, authenticity and integrity of messages/data exchanged on X-Road.
  
**System configuration** –  consists of data stored in the database, and in the various configuration files held in the file system of an X-Road component.