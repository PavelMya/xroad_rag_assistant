### 2.6 Downloading and Verifying the Configuration

A configuration client can download the configuration by making HTTP GET requests to the configuration source. To download and verify the entire configuration, the client can follow these steps.

1. Parse the configuration anchor and read the download URI (pointing to the configuration directory) and the verification certificate.
2. Download the configuration directory from the URI and parse it.
3. Verify the signature of the configuration directory using the public key of the verification certificate. The signature algorithm identifier is specified by the MIME header *Signature-algorithm-id* of the MIME part containing the signature.
4. For each directory part,
    1. download the configuration file from the URL indicated in the *Content-location* MIME header;
    2. verify the integrity of the downloaded file by comparing the hash of the file with the hash contained in the directory (the hash algorithm is specified in MIME header *Hash-algorithm-id*).
5. For each configuration anchor in the private parameters file, download and verify the configuration using this set of rules.