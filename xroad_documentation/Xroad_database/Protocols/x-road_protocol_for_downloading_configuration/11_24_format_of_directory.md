### 2.4 Format of Directory

The first entry in the directory MUST be a header-only entry with the header *Expire-date* that contains date and UTC time in ISO 8601 format [ISO8601]. This header specifies the end of validity time of the directory – after the validity time has passed, the configuration client MUST consider the configuration as invalid and should attempt to download fresh configuration. In addition, the header-only entry SHOULD include the header *Version* which identifies the version of the configuration (section [2.7](#27-versioning)).

The directory contains references to the individual configuration files. In addition to download URI, each directory item contains hash of the file that can be used to verify integrity of the downloaded file.

The directory is a MIME multipart (content type is *multipart/mixed*) where each part represents one configuration file. Each part MUST have the following MIME headers:

- *Content-type* – the value MUST be “*application/octet-stream*”.
- *Content-transfer-encoding –* encoding of the body of the part. The value MUST be “*base64*”.
- *Content-location* – URL that can be used to download the configuration file referenced by this directory item. The URL can be relative (the base is the location of the signed configuration).
- *Hash-algorithm-id –* identifies the hash algorithm used to create the content of the directory item. This specification supports algorithm identifiers listed in XML Signature specification [XMLDSIG], Section 6.2.

Each directory part CAN have the following MIME headers:

- *Content-identifier –* identifies the type of the configuration part. Example types can be private parameters and shared parameters. Section [2.5](#25-list-of-content-identifiers) lists the predefined content identifiers. In addition to these, each X-Road installation is free to add additional content to the configuration.
- *Content-file-name –* additional information about the configuration part. The configuration client CAN use value of this header as a hint about what name to use when saving this configuration part to a file.

The content of a directory part MUST be digest of the configuration part. The digest algorithm is specified in the *Hash-algorithm-id* MIME header. The input to the digest calculation is body of the file that can be downloaded from the URL specified in the *Content-location* MIME header.

Annex A.2 contains an example of a signed directory.