# Property mac-key-base64-encoded should be true if the provided mac-keys are encoded in base64.
eab-credentials:
  certificate-authorities:
    'Example Root CA':
      mac-key-base64-encoded: true
      members:
        'EU:COM:1234567-8':
          auth-kid: key_2
          auth-mac-key: YXV0aGVudGljYXRpb25zZWNyZXRtYWNrZXk=
          sign-kid: key_3
          sign-mac-key: c2VjcmV0X21hY19rZXlfZm9yX3NpZ25pbmc=
    'Some Other CA':
      mac-key-base64-encoded: false
      members:
        'EU:GOV:9090909-1':
          kid: kid123
          mac-key: goodlongsecretwordthatisnotshort

# This is a password of the ACME Server account PKCS #12 keystore that is populated automatically by the Security Server.

# Keystore is at /etc/xroad/ssl/acme.p12
account-keystore-password: acmep12Password1234

```

## 25 Migrating to EC Based Authentication and Signing Certificates