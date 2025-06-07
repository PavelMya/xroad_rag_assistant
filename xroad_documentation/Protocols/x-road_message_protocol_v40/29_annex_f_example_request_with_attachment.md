## Annex F Example Request with Attachment

```xml
.. other transport headers ...
Content-Type: multipart/related; type="text/xml"; start=""; boundary="MIME_boundary"
MIME-Version: 1.0

--MIME_boundary
Content-Type: text/xml; charset=UTF-8
Content-Transfer-Encoding: 8bit
Content-ID: 



    
        
            EE
            GOV
            MEMBER1
            SUBSYSTEM1
        
        
            EE
            GOV
            MEMBER2
            SUBSYSTEM2
            exampleService
            v1
        
        4894e35d-bf0f-44a6-867a-8e51f1daa7e0
        EE12345678901
        12345
        4.0
    
    
        
            foo
            cid:data.bin
        
    


--MIME_boundary
Content-Type: application/octet-stream; name=data.bin
Content-Transfer-Encoding: base64
Content-ID: 
Content-Disposition: attachment; name="data.bin"; filename="data.bin"

VGhpcyBpcyBhdHRhY2htZW50Lg0K
--MIME_boundary--
```