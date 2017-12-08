import json
import re
import requests
import pause

from bs4 import BeautifulSoup
from markdown import markdown
from datetime import datetime

from config import GITHUB_ACCESS_TOKEN


def retrieve_repo_readme(repo):
    url = f"https://raw.githubusercontent.com/{repo['name']}/master/README.md"
    response = requests.get(url)
    return response.text if response.status_code == 200 else ''


def clean_readme(readme):
    html = markdown(readme)
    text = ''.join(BeautifulSoup(html, 'html.parser').findAll(text=True))
    return re.sub('\s+', ' ', text)


def retrieve_repo_languages(repo):
    headers = {'Authorization': 'token ' + GITHUB_ACCESS_TOKEN}
    url = f"{repo['url']}/languages"
    response = requests.get(url, headers=headers)

    # check if we're run out of allowed api requests
    # if yes, wait till the limit reset time and retry
    if int(response.headers['X-RateLimit-Remaining']) == 0:
        limit_reset_time_sec = int(response.headers['X-RateLimit-Reset'])

        print('GitHub API requests limit exceeded - pause till ',
              datetime.fromtimestamp(limit_reset_time_sec).
              strftime('%Y-%m-%d %H:%M:%S'))

        pause.until(limit_reset_time_sec)
        response = requests.get(url, headers=headers)

    langs = (json.loads(response.text)
             if response.status_code == 200
             else {})

    return '/'.join(langs.keys())
