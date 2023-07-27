import requests

payload={
    "name" : "Ashish",
    "job" : "Automation"
}
resp=requests.post("https://reqres.in/api/users", data=payload)
print(resp.status_code)
print(resp.json())
assert resp.json()["job"]== "Automation", "job profile doesn't match"

