### 4.2 URI Sanitation

The REST URIs are composed of different parts (e.g. INSTANCE/CLASS/MEMBER/SUBSYSTEM) and some of them may contain
characters that can not be used in URIs directly. The URI syntax is described in \[[RFC3986](#Ref_RFC3986)\]. Because of
this the consumer information system needs to represent the parts using UTF-8 and encode the parts separately using
\[[PERCENT-ENCODING](#Ref_PERCENTENC)\]. The path separator "/" is used to delimit the parts and must not be encoded,
unless the part actually contains the character "/" (not recommended).

**Examples**

Invalid:

```
INSTANCE%2FCLASS%2FMEMBER%2FSUBSYSTEM%2FBARSERVICE
```

Valid:

```
INSTANCE/CLASS/MEMBER/SUBSYSTEM/BAR%2FSERVICE  (where the service code is "BAR/SERVICE")
```

On the Security Server side the incoming request URIs MUST be strictly validated. Input strings from the user can't be
trusted. Lengths of the strings need to be checked and maximum length or the request URI needs to be limited. Although
the URI standard does not specify a maximum size of the URL, most clients enforce an arbitrary limit of 2000 characters.
The Security Server implementation MAY do this as well. Sending data that is difficult to express in a hierarchical
manner, and especially data that is larger than this 2000 character limit, should be transmitted in the body of the
request.

The REST URI parsing scenario is particularly vulnerable to \[[HPPP](#Ref_HPPP)\] (HTTP Parameter Pollution) and
\[[SSRF](#Ref_SSRF)\] (Server-Side Request Forgery) attacks. The Security Server SHOULD explicitly be prepared for them.