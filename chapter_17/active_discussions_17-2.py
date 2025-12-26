## active discussions ## 
#using data from hn_submissions.py, make bar chart showing the most active discussions
#currently happening on hacker news
    #height of each bar should correspond to the number of comments
    #each submission has. the label for each bar should include the submissions
    #titles and act as a link to the dicussion page for that submission
        #if you get keyerror when creating a chart use a try-except block to skip over
        #promotional costs
        
import plotly.express as px
import json
from pathlib import Path

path = Path("./chapter_17/data/hn_submissions_data.json")
contents = path.read_text(encoding="utf-8")
all_data = json.loads(contents)

topics, comments, links = [],[],[]
for data in all_data:
    
    #name of each bar that acts as link
    topic = data['title']
    link = data['hn_link']
    topic_link = f"<a href='{link}'>{topic}</a>"
    topics.append(topic_link)
    
    comment = data['comments']
    comments.append(comment)

title = "most dicussed topic on hackernews"
labels = {'x':'topic','y':'comments'}
fig = px.bar(x=topics,y=comments,title=title,labels=labels)    
fig.show()   
    


# fig = px.bar()f