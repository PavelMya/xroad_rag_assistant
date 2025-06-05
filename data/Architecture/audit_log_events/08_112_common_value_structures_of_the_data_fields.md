#### 1.1.2 Common Value Structures of the Data Fields

Values of data fields `memberIdentifier`, `clientIdentifier`, `ownerIdentifier`, `providerIdentifier`, and 
`serviceProviderIdentifier` have a common structure:

```json
{
  "xRoadInstance": "...",
  "memberClass": "...",
  "memberCode": "..."
}
```

where `xRoadInstance` is the X-Road instance, `memberClass` is the X-Road member class, and `memberCode` is the X-Road
member code. In case of `clientIdentifier`, `providerIdentifier`, and `serviceProviderIdentifier` an optional field
`subsystemCode` (the X-Road subsystem code) is present in the structure.