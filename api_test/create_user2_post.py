import json

import requests

mydata= open("data.json", "r").read()
resp=requests.post("https://reqres.in/api/users", json.loads(mydata))
print(resp.status_code)
print(resp.json())
print(resp.headers.get("content-type"))
assert resp.json()["job"]== "QA", "job profile doesn't match"

