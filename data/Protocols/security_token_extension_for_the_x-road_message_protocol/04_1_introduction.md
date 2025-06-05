## 1 Introduction

This specification describes an extension of the X-Road protocol for sending loosely defined security tokens as X-Road header data.
The X-Road message protocol version 4.0 \[[PR-MESS](#Ref_PR-MESS)\] already supports sending arbitrary SOAP headers end-to-end. This
extension just provides a common, defined way to deliver security tokens with the X-Road protocol using the `securityToken` element. 

The motivation for the extension was the need to provide a common way to transfer JSON Web Tokens \[[JWT-RFC](#Ref_JWT-RFC)\] over X-Road.
Examples using JWT as payload in the security token can be found in the [Examples](#examples) section.