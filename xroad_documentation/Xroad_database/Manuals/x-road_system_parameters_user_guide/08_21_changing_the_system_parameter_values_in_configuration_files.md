### 2.1 Changing the System Parameter Values in Configuration Files

The configuration files are INI files \[[INI](#Ref_INI)\], where each section contains parameters for a particular server component.

In order to override the default values of system parameters, create or edit the file

	/etc/xroad/conf.d/local.ini

Each system parameter affects a specific server component. To change the value of a system parameter, a section for the affected component must be created in the INI file. The name-value pairs of the system parameters for that component are written under the section, one pair per line.

The following format is used for the sections:

	[ServerComponent]
	SystemParameterName1=Value1
	SystemParameterName2=Value2

For example, to configure the parameter *client-http-port* for the *proxy* component, the following lines must be added to the configuration file:

	[proxy]
	client-http-port=1234

Multiple parameters can be configured under the same section:

	[proxy]
	client-http-port=1234
	server-listen-port=20000

**NB! Changing the parameter values in the configuration files requires restarting of the server.**

**WARNING! The value of the parameter is not validated, thus care must be taken when changing the value. For example, setting the port number to a non-numeric value in the configuration will cause the system to crash.**