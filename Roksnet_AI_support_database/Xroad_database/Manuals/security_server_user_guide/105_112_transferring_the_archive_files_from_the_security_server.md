### 11.2 Transferring the Archive Files from the Security Server

In order to save hard disk space, it is recommended to transfer archive files periodically from the Security Server (manually or automatically) to an external location.

The message log package provides a helper script `/usr/share/xroad/scripts/archive-http-transporter.sh` for transferring archive files. This script uses the HTTP/HTTPS protocol (the POST method, the form name is file) to transfer archive files to an archiving server.

Usage of the script:

| Options:          | &nbsp;                                                                                                                                 |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `-d, --dir DIR`   | Archive directory. Defaults to '/var/lib/xroad'                                                                                        |
| `-r, --remove`    | Remove successfully transported files form the archive directory.                                                                      |
| `-k, --key KEY`   | Private key file name in PEM format (TLS). Defaults to '/etc/xroad/ssl/internal.key'                                                   |
| `-c, --cert CERT` | Client certificate file in PEM format (TLS). Defaults to '/etc/xroad/ssl/internal.crt'                                                 |
| `-cacert FILE`    | CA certificate file to verify the peer (TLS). The file may contain multiple CA certificates. The certificate(s) must be in PEM format. |
| `-h, --help`      | This help text.                                                                                                                        |

The archive file has been successfully transferred when the archiving server returns the HTTP status code `200`.

Override the configuration parameter archive-transfer-command (create or edit the file `etc/xroad/conf.d/local.ini`) to set up a transferring script. For example:

    [message-log]
    archive-transfer-command=/usr/share/xroad/scripts/archive-http-transporter.sh -r http://my-archiving-server/cgi-bin/upload

The message log package contains the CGI script `/usr/share/doc/xroad-addon-messagelog/archive-server/demo-upload.pl` for a demo archiving server for the purpose of testing or development.