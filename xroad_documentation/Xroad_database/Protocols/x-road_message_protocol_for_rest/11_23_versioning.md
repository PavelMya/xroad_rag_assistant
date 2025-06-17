### 2.3 Versioning

The X-Road Message Protocol for REST uses \[[SEMANTIC-VERSIONING](#Ref_SEMVER)\] rules. After the initial development
phase (0.x) there MUST be a strongly justified reason for amending or updating the protocol. Especially new major
versions of the protocol SHOULD be extremely rare.

The protocol version identifier comes from the major version of the protocol and is a mandatory part of the request URL.
The initial released version of the protocol will have the identifier r1. When the protocol needs to be updated, the
most important consideration is backwards compatibility.

**A)** If the change can be introduced in a backwards compatible manner (i.e. the clients not aware of the change are
still able to communicate using the protocol) the major protocol version and the protocol version identifier remain the
same. Depending on the scope of the change, the minor or patch version is incremented e.g. 1.0.0 → 1.1.0.

**B)** If the change requires breaking the backwards compatibility the major protocol version and the
protocol version identifier are incremented e.g. 1.2.3 → 2.0.0. The old protocol will be supported
for at least a year after releasing the new version.