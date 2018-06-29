import requests



r =requests.get('https://api.github.com/events')
print r.json()
print r.encoding
print r.content