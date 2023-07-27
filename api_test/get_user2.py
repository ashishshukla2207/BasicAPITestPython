import requests

p={"page":2} #sending parameter as dictionary
resp=requests.get("https://reqres.in/api/users?", params=p)
print(resp.url)
json_response= resp.json()
print(json_response['total'])
assert json_response['total']== 12, "count doesn't match"


print(json_response["data"][0]["email"])

assert json_response["data"][0]["email"].endswith("reqres.in"), "email format not valid"

print(json_response["data"][2]["last_name"])

assert json_response["data"][2]["last_name"]!=None
