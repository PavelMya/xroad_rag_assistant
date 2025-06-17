### 4.4 HTTP Redirects

The service provider may respond with HTTP redirection. HTTP redirects are responses with a status code of 3xx. There
are several types of redirects and they fall into three categories: permanent, temporary and special redirections.
X-Road does not follow redirects and passes the redirection unmodified to the service consumer. The service consumer may
decide what to do with this response. Generally speaking, the redirects pose a security threat and should not be blindly
followed. The default setting for following redirects is recommended to be off.