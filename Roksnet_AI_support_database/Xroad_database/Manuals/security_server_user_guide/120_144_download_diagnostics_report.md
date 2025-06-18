### 14.4 Download diagnostics report

It is possible to download a diagnostics report file which can be included as additional information when registering issues for the Security Server.
File includes following information:
- X-Road and Java version
- OS version
- Configuration overrides from local.ini (just property names)
- Authentication certificates (name, status, is it active)
- Global configuration status
- OCSP responders status
- Timestamping status
- Deployment mode (native / container)
- Installed X-Road packages
- Running Java processes
- Is maintenance mode enabled

File is in JSON format and can be downloaded by clicking the **Download diagnostics report** button.