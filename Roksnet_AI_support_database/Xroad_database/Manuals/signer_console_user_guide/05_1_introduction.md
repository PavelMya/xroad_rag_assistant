## 1 Introduction

The purpose of this document is to explain how to manage keys and certificates in signer from the command line using the signer console utility.

*Signer* is an X-Road component whose primary purpose is to process signing requests and produce signatures. Signer manages software and hardware (smart cards, HSMs) tokens and their keys and handles certificates associated with the keys.

*Signer console* is a command line utility for interacting with Signer. The utility provides commands for various operations and can execute a single command or be started as an interactive text-based shell.

### 1.1 References

1.  \[SPEC-AL\] X-Road: Audit log events. Document ID: [SPEC-AL](../Architecture/spec-al_x-road_audit_log_events.md)

2.  \[JSON\] Introducing JSON,

## 2 Using the Signer console

### 2.1 Signer console options

Signer console accepts the following options:
- `-h` or `-help` displays list of supported commands
- `-v` or `-verbose` displays more detailed execution output

### 2.2 Starting as interactive shell

To start the signer console as an interactive shell, type 
```bash
sudo -u xroad -i signer-console []
```

### 2.3 Executing single commands

To execute a single command, type
```bash
sudo -u xroad -i signer-console []  []
```

### 2.4 Available commands

This section gives an overview of all available commands in signer console.

A command may have one or more arguments, and may or may not produce any output. If command has arguments, they are always mandatory.

#### 2.4.1 list-tokens

**Description:** Lists all tokens.

**Arguments:** (none)

**Output:** List of all tokens, each line representing the following token information:
```
 (, , , )
```

#### 2.4.2 list-keys

**Description:** Lists all keys on all tokens.

**Arguments:** (none)

**Output:** List of keys on all tokens, each line representing the following key information:
```
 (, )
```

#### 2.4.3 list-certs

**Description:** Lists all certificates and certificate requests on all keys.

**Arguments:** (none)

**Output:** List of certificates and certificate requests on all keys, each line representing the following 
```
 (, )
```

#### 2.4.4 set-token-friendly-name

**Description:** Sets friendly name to the specified token.

**Arguments:**
* ***token id***: the identifier of the token. Use *[list-tokens](#241-list-tokens)* to look up token id-s.
* ***friendly name***: the name to set.

**Output:** (none)

#### 2.4.5 set-key-friendly-name

**Description:** Sets friendly name to the specified key.

**Arguments:**
* ***key id***: the identifier of the key. Use *[list-keys](#242-list-keys)* to look up key id-s.
* ***friendly name***: the name to set.

**Output:** (none)

#### 2.4.6 get-member-certs

**Description:** Returns certificates of a member.

**Arguments:**
* ***member id***: the identifier of the member, entered as `\"  \"`

**Output:** List of certificates of the specified member.

#### 2.4.7 activate-certificate

**Description:** Activates the specified certificate.

**Arguments:**
* ***certificate id***: the identifier of the certificate. Use *[list-certs](#243-list-certs)* to look up certificate identifiers.

**Output:** (none)

#### 2.4.8 deactivate-certificate

**Description:** Deactivates the specified certificate.

**Arguments:**
* ***certificate id***: the identifier of the certificate. Use *[list-certs](#243-list-certs)* to look up certificate identifiers.

**Output:** (none)

#### 2.4.9 delete-key

**Description:** Deletes the specified key and all associated certificates and certificate requests.

**Arguments:**
* ***key id***: the identifier of the key. Use *[list-keys](#242-list-keys)* to look up key id-s.

**Output:** (none)

#### 2.4.10 delete-certificate

**Description:** Deletes the specified certificate from Signer.

**Arguments:**
* ***certificate id***: the identifier of the certificate. Use *[list-certs](#243-list-certs)* to look up certificate identifiers.

**Output:** (none)

#### 2.4.11 delete-certificate-request

**Description:** Lists all tokens.

**Arguments:**
* ***certificate request id***: the identifier of the certificate request. Use *[list-certs](#243-list-certs)* to look up certificate request identifiers.

**Output:** (none)