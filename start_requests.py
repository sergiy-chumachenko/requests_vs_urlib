import requests

test = requests.get("http://www.hipstercode.com")

print(test.__getstate__())