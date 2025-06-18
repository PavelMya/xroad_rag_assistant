### 4.7 Disabling Client Subsystem Temporarily

Security Server client subsystem in "Registered" state may be disabled temporarily for maintenance purposes.

When client subsystem is disabled in Security Server it first enters "Disabling in progress" state. Once the state change is propagated through the global configuration, client subsystem enters the "Disabled" state.

Client subsystem in "Disabled" state may be enabled again. When it is enabled in the Security Server it first enters "Enabling in progress" state.

Subsystem can use and provide X-Road services only in "Registered" state. Subsystem cannot be used while in "Disabled", "Disabling in progress" or "Enabling in progress" states.