### 2.6 APPROVED_TSAS

Approved time-stamping authority (TSA). The certificate of the approved CA is used for time-stamping signed messages.

New record creation process starts when an X-Road system administrator receives a certificate from a TSA which is going to be trusted by the X‑Road instance. Having received the certificate, an X-Road system administrator uploads it in the user interface. The record is created when the user adds new approved TSA in the user interface. The record is deleted when for any reason the governing authority of the X-Road instance does not trust the TSA any more. Then an X-Road system administrator deletes the approved TSA in the user interface. The record is modified when the user changes URL or uploads new certificate.