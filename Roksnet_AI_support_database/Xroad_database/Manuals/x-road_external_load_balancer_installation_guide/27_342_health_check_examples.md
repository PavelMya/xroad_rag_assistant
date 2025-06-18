#### 3.4.2 Health check examples

Before testing with an actual load balancer, you can test the health check service with `curl`, for example.

Below is an example response from the Health check service when everything is up and running and messages should go through
this node:
```bash
$ curl -i localhost:5588
   HTTP/1.1 200 OK
   Content-Length: 0
```

And a health check service response on the same node when the service `xroad-signer` is not running:
```bash
$ curl -i localhost:5588
HTTP/1.1 500 Server Error
Transfer-Encoding: chunked

Fetching health check response timed out for: Authentication key OCSP status
```


Continue to [chapter 6](#6-verifying-the-setup) to verify the setup.