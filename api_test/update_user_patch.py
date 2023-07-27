import requests

payload={
    "name": "morpheus",

}
resp= requests.patch("https://reqres.in/api/users/2", data=payload)
print(resp.json())
print(resp.status_code)
print(resp.json())
print(resp.headers.get("content-type"))
#assert resp.json()["job"]== "QA", "job profile doesn't match"



