### 3.5 Download Signed Document

The service for downloading signed documents can be used by the information systems to download signed containers from the security server's message log. In addition, the service provides a convenience method for downloading global configuration that can be used to verify the signed containers.

The protocol is a synchronous RPC-style protocol that is initiated by the IS. The service is implemented as HTTP(S) GET requests. See \[[UG-SIGDOC](#Ref_UG-SIGDOC)\] for further details.

The Download Signed Document protocol is used by IS for downloading data stored in the security server and therefore the availability, throughput and latency of its implementing components are not critical to the functioning of the X-Road.