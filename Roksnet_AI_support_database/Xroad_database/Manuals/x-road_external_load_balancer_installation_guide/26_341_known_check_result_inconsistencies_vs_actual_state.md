#### 3.4.1 Known check result inconsistencies vs. actual state
There is a known but rarely and not naturally occurring issue where the health check will report an OK condition for a
limited time but sending some messages might not be possible. This happens when an admin user logs out of the keys.

The health check will detect if the tokens (the key containers) have not been signed into after `xroad-signer` startup.
It will however, not detect immediately when the tokens are manually logged out of. The keys are cached by the `xroad-proxy`
process for a short while. As long as the authentication key is still cached, the health check will return OK, even though
the necessary signing context values for sending a message might no longer be cached. This means messages might fail to be sent
even if the health check returns OK. As the authentication key expires from the cache (after a maximum of 5 minutes), the
health check will start returning failures. This is a feature of caching and not a bug per se. In addition, logging out
of a Security Server's keys should not occur by accident so it should not be a surprise that the node cannot send messages
after not having access to it's keys.