import requests

r = requests.get('http://www.uaex.edu')

print(r.status_code)

print(r.encoding)

print(r.text)
