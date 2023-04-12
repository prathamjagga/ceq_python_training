## this file contains the solutions to assignment 8


## (1) What is meant by stateless in REST?
## Ans: Stateless means that each API call is independent of other calls, the data or the result of any call is not stored
## in any fashion whatsoever, that is why we can say that the state of calls is not maintained, hence stateless.


## (2) 403, 503, 301 Status Codes?
## Ans: (i) 403 - It means that the user, no matter authorized or unauthorized don't have access to the resource (Forbidden)
## (ii) 503 - It indicates that there is a performance issue on the server. Most probably due to unhandling of the load (Service Unavailable)
## (iii) 301 - It indicates the requested resource is moved permanently to a new address. (Moved Permanently)


## (3) Making GET, POST, PUT and DELETE Requests using requests module to a public API

import requests

URL = "https://reqres.in/api"  ## PUBLIC API URL

## simple get request
resp = requests.get(URL + "/users/2")  ## Let us get the second user
print("GET OUTPUT -->", resp.json())

## simple post request
resp = requests.post(URL + "/users", data={"hello": "world"})  ## let us add new data
print("POST OUTPUT -->", resp.json())

## simple delete request
resp = requests.delete(
    URL + "/users/2"
)  ## this is a dummy request which takes a user's id as a param and returns 204 deleted
print("DELETE OUTPUT -->", resp.status_code)

## simple put request
resp = requests.get(
    URL + "/users", data={"hello": "there", "id": 715}
)  ## update our object with "hello":"there"
print("PUT OUTPUT -->", resp.status_code)
