import requests

response= requests.get("https://reqres.in/api/users?page=2")

#int(response)  #prints status code
print(type(response))
print(dir(response))

#print(response.text)
#print(response.content)
print(response.json())

code = response.status_code
assert code ==200, "code doesn't matches"

print(response.headers)

print(response.cookies)
print(response.encoding)
print(response.url)