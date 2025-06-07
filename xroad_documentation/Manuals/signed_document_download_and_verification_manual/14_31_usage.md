### 3.1 Usage

The asicverifier utility is run as follows:

    java -jar asicverifier.jar ( --version |   )

where `` is the path to the signed document being verified and `` is the path to the verification configuration for this container (see Section 3.2 ). You can check the version of the asicverifier tool with the `--version` option.

If verification is successful the output will be similar to:

    Loading configuration from18 verificationconf/... 
    Verifying ASiC container "abc12345-request-1ab2c3d4f5.asice" ... 
    Verification successful. 
    Signer 
        Certificate: 
            Subject: CN=CLIENT1, O=COM, C=EE 
            Issuer: C=EE, O=EJBCA Sample, CN=AdminCA1 
            Serial number: 897779140320284054 
            Valid from: Mon May 04 14:30:38 EEST 2015 
            Valid until: Wed May 03 14:30:38 EEST 2017 
        ID: MEMBER:EE/COM/CLIENT1 
    OCSP response 
        Signed by: 
            Subject: C=EE, O=EJBCA Sample, CN=AdminCA1 
            Issuer: C=EE, O=EJBCA Sample, CN=AdminCA1 
            Serial number: 6005434255669835317 
            Valid from: Thu Jun 14 13:04:29 EEST 2012 
            Valid until: Sun Jun 12 13:04:29 EEST 2022 
        Produced at: Fri Jun 05 08:47:11 EEST 2015 
    Timestamp 
        Signed by: 
            Subject: CN=timestamp1, O=Internet Widgits Pty Ltd, C=EE 
            Issuer: CN=timestamp1, O=Internet Widgits Pty Ltd, C=EE 
            Serial number: 12319570547049363959 
            Valid from: Sun Nov 30 22:13:44 EET 2014 
            Valid until: Wed Nov 27 22:13:44 EET 2024 
        Date: Fri Jun 05 09:31:37 EEST 2015 
    
    
    Would you like to extract the signed files? (y/n) y 
    Created file message.xml 
    Files successfully extracted.

As can be seen from the example above, the asicverifier tool will optionally extract the signed files to the working directory. In the case of REST message, the request/response line and headers are in `message.xml` and the REST body (if logged) is present in a file `attachment1`.

Should the verification fail, the reason for failure will be presented to the user in an error message. For example:

    Loading configuration from verificationconf/... 
    Verifying ASiC container "abc12345-request-1ab2c3d4f5.asice" ... 
    Verification failed: Certificate is not issued by approved certification service provider.
    
    Would you like to extract the signed files? (y/n) y
    Created file message.xml
    Files successfully extracted.

In case of verification failure, the asicverifier tool will optionally extract the signed files to the working directory.

Notice that when `messagelog.message-body-logging` property is set to `false`, the verification always fails with the error message:

    Verification failed: Signature is not valid