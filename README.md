# verby
A standalone HTTP verb scanner for test purposes only. The main goal is to verify the allowed verbs based on the  
[OWASP HTTP verb tampering]('https://www.owasp.org/index.php/Testing_for_HTTP_Verb_Tampering_(OTG-INPVAL-003)') test.

The searched verbs are:

 - `HEAD`
 - `OPTIONS`
 - `GET`
 - `PUT`
 - `POST`
 - `DELETE`
 - `TRACE`
 - `CONNECT`
 - `OPTIONS`
 - `PROPFIND`


## How to run

```
    python verby.py
```