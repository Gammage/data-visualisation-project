import requests
import plotly.express as px

#make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"accept":"application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

#process overall results
response_dict = r.json()
print(f"complete results: {not response_dict['incomplete_results']}")


repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [],[],[]
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    stars.append(repo_dict['stargazers_count'])

    #adding custom tooltips
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)
    
    # turn repo names into active links
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)


#styling the chart
title = "most-starred python projects on github"
labels = {'x':'Repository', 'y':'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20,)

#trace refers to a collection of data on a chart
fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)


fig.show()



