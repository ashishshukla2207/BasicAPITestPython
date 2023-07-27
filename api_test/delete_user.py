import requests

resp=requests.delete("https://reqres.in/api/users/2")
print(resp)

assert resp.status_code==204, "status code incorrect"