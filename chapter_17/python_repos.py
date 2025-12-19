##processing an API Response

#import requests module
import requests

#make an api call and check the response

#assign the url of the api call to the url variable
#main part of url
url = "https://api.github.com/search/repositories"

#the query string. we appended stars:>10_000 (only look for python repos more than 10_000 stars)
url += "?q=language:python+sort:stars+stars:>10000"

#github is on 3rd version of its api, (hence v3)
#we define headers for the api call that ask explicity use this version of the api,
    #then return the results in the JSON format
headers = {"accept":"application/vnd.github.v3+json"}

#we use requests to make the call to the API.
#we call get() and pass it the URL and the header that we defined,
    #and we assign the response object to the variable r
r = requests.get(url, headers=headers)

#response object has an attribute called status code, telling us whether request was successful
print(f"status code: {r.status_code}")

#asked the api to return information in json format, so we use the json() method to convert
#the information to a python dictionary
response_dict = r.json()

#process results
print(response_dict.keys())

#because the status code is 200, we know that the request was successful

##working with the response dictionary##

#we explore the response dictionary by printing the value associated with total count
#total count represents total number of python repositories returned by the api call
print(f"total repositories: {response_dict['total_count']}")

#we use the not statement with incomplete results to get the completed results
print(f"complete results: {not response_dict['incomplete_results']}")

#value from items is a list containing a number of dictionaries
    #each of which contains data about an individual python repo
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

#examine first repository
#looping over that first repo dictionary from the list and call it repo_dict
repo_dict = repo_dicts[0]

print(f"\nKeys: {len(repo_dict)}")

#loop over the keys in that repo dict
for key in sorted(repo_dict.keys()):
    print(key)

##summarising the top repositories
#want to include more then one repository
#a loop to print selected info about each repo the api call returns to inc in visualisation


#intro message
print("\nSelected information about first repository:")

#loop through the dictionaries in repo dicts, inside the loop we print below
for repo_dict in repo_dicts:
    print(f"\nname: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"stars: {repo_dict['stargazers_count']}")
    print(f"repository: {repo_dict['html_url']}")
    # print(f"created: {repo_dict['created_at']}")
    # print(f"updated: {repo_dict['updated_at']}")
    print(f"description: {repo_dict['description']}")
    
#monitoring API rate limits#
#most apis have rate limits, which means theres a limit to how many 
#requests you can make in a certian amount of time. to see if your approaching githubs limits,
#enter https://api.github.com/rate_limit see a response

#many APIs require you to register and obtain an API key or access token to make API calls
#github has no such requirement, but if you obtain an access token, limits go higher

#visualing repositories using plotly

#a visualisation using the data we've gathered to show the relative popularity of
#python projects on github

