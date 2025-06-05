### 2.2 Format of Configuration Anchor

Configuration anchor is used to distribute information about configuration sources to configuration clients. Because configuration anchor is used to verify authenticity of the downloaded configuration, it must be protected against modification. Example means are digitally signing the file or distributing the fingerprint of the file to the client in person.

The configuration anchor is stored in an XML file containing a *configurationAnchor* element defined in Annex E . It contains the following fields:

- *generatedAt* – date when the anchor was generated. Can be used to check whether correct version of the anchor is used;
- *instanceIdentifier* – identifies the X-Road instance that provides configuration to this configuration source;
- *source* – describes a single configuration source. The *source* element contains the following fields:
    - *downloadURL* – HTTP URL that can be used to download signed configuration (see Section [2.3](#23-format-of-signed-configuration) for format of the downloaded file);
    - *verificationCert* – public key that can be used to verify the signed configuration, presented as X.509 [X509] certificate
      The certificate is only used as a container for the public key. The configuration client should not make any assumptions about other fields of the certificate.

Annex A.2 contains an example configuration anchor file.