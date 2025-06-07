### 8.2 Messaging Validation 

When input contains XML, it must be validated against its schema before using it. XML injection attacks are mitigated by ensuring that XML input follows the rules specified in the schema. Down-stream errors that might be caused from invalid XML input are mitigated by validating the XML at the earliest point where it crosses a trust boundary.