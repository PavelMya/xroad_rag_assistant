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