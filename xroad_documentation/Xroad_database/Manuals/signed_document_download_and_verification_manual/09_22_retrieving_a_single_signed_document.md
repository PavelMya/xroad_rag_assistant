### 2.2 Retrieving a Single Signed Document

Should the user only desire the request or response then additional mutually exclusive parameters are available:

* `requestOnly` – only include signed documents for request messages (response filename  is `queryId-request.zip[.gpg]`);
* `responseOnly` – only include signed documents for response messages (response filename is `queryId-response.zip[.gpg]`).

The aforementioned parameters make the service return a (possibly encrypted) ZIP archive, which may contain either one or more signed documents (depending if the provided `queryId` is unique). If only a single signed document is expected then the request can be further be constrained by adding the following parameter:

* `unique` – specifies that the only a single signed document is expected in the response, must be used in combination with either `requestOnly` or `responseOnly` parameter.

If this parameter is used and, indeed, the query identifier is unique, then the security server responds with a single signed document (content-type `application/vnd.etsi.asic-e+zip`, or `application/octet-stream` if the archive is encrypted) which represents the corresponding message.