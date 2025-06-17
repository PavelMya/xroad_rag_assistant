## 4 Central Server System Parameters

The system parameters described in this chapter are used by the X-Road central server, except for the parameters *ocspFreshnessSeconds* and *timeStampingIntervalSeconds.*

The values of *ocspFreshnessSeconds* and *timeStampingIntervalSeconds* are distributed to the security servers via the global configuration. These parameters determine the interval of calling OCSP responder services and time-stamping services (respectively) by the security servers.

### 4.1 System Parameters in the Configuration File

For instructions on how to change the parameter values, see section [Changing the System Parameter Values in Configuration Files](#changing-the-system-parameter-values-in-configuration-files).