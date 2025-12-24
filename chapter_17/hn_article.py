##The Hacker News API##

# https://news.ycombinator.com

#current call returns information about the current top article as of this writing
# https://hacker-news.firebasio.com/v0/item/31353677.json

import requests
import json

#make an api call, and store the response
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"status code: {r.status_code}")

#explore the structure
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)


