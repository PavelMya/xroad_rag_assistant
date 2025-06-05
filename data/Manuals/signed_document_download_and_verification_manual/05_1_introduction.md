## 1 Introduction

Messages exchanged between the X-Road security servers are signed and encrypted. For every regular request and response, the security server produces a signed document. The signatures are time-stamped either synchronously, immediately after the message has been processed by the security server, or asynchronously in periodic batches for a better performance.

This document describes the retrieving and verification process of the signed and time-stamped document [PR-SIGDOC].