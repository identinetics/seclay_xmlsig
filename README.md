# Request/Response Exchange via POST/POST exchanges

## Purpose

Request an XML infoset to be signed by a signing service not directly accessible from the client.
The connection to the signing service is via front-channel, that is via the browser.

Rationale: the signing service is local to the user, the client application is remote.

## Flow: 

Test setup: client_service listens on port 8080, signature_service on 3495, both on localhost

1. Client (browser) requests data entry form (GET http://localhost:8080/ ) 
2. Client_service respondes with an HTML form that contains a Javscript function to handle the request to the signature_service.
3. The Javascipt function posts the signature request (POST http://localhost:3495/) 
4. The signature_service responds with the signed data (signature_service.py is a mock-up service with a static result for unit testing)
5. The Javascipt function posts the signed result (or error message) back to the client_service (POST http://localhost:8080/ )
6. Success if the signed data has been received
7. The Javascript function will replace the current page with the response content of the client_service


## Test setup:

1. start client_service.py
2. start signature_service.py
3. Redirect the browser to http://localhost:8080/