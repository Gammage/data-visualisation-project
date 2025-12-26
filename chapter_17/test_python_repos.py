##as part of exercise testing python repos 17-3

import pytest
import requests
    
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"accept":"application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)

assert r.status_code == 200
    