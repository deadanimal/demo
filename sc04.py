import requests
r = requests.post('https://httpbin.org/post', data = {'name':'AA', 'cat': False})
print(r)

body_ = r.content
print(body_)
