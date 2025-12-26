## finding top stories on hacker news##
from operator import itemgetter
from pathlib import Path
import json
import requests

#make an api call and check the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"status code: {r.status_code}")

# process information about each submission

#convert the response object to a python list
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:10]:
    #make a new api call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    #status code for each
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    #build a dictionary for each article
    submission_dict = {
        'title':response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)


for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion Link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

path = Path("./chapter_17/data/hn_submissions_data.json")
data = json.dumps(submission_dicts)
path.write_text(data)
