## 2 Overview

The X-Road security servers periodically download global configuration
distributed by the configuration providers. The global configuration is
used to verify the parties communicating over the X-Road and to check
the validity of various data items, such as authentication certificates,
OCSP responses and timestamps.

The information needed by the security servers for downloading and
verifying global configuration is contained in configuration anchors.
The configuration anchors are distributed by the internal configuration
providers to the security server owners via out of band means.

The configuration providers ensure the integrity of the distributed
configuration by signing the configuration directory.