import csv
import json
import glob
import os
import re
import requests

from bs4 import BeautifulSoup
from markdown import markdown

from config import GITHUB_ACCESS_TOKEN, EVENTS


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
    langs = (json.loads(response.text)
             if response.status_code == 200
             else {})
    return '/'.join(langs.keys())


def collect_event_data(fname):
    field_names = [
        'id',
        'type',
        'actor_id',
        'actor_login',
        'repo_id',
        'repo_name',
        'created_at',
        'repo_languages',
    ]

    name, ext = os.path.splitext(fname)

    input_file = open(fname, 'r')
    output_file = open(name + '.csv', 'w')
    readme_file = open(name + '-readme', 'w')

    writer = csv.DictWriter(output_file, fieldnames=field_names)
    writer.writeheader()

    for line in input_file:
        activity_record = json.loads(line)
        # skip unnecessary event types that are not related to repos
        if activity_record['type'] not in EVENTS:
            continue

        readme = clean_readme(
            retrieve_repo_readme(activity_record['repo']))
        langs = retrieve_repo_languages(activity_record['repo'])
        data = {
            'id': activity_record['id'],
            'type': activity_record['type'],
            'actor_id': activity_record['actor']['id'],
            'actor_login': activity_record['actor']['login'],
            'repo_id': activity_record['repo']['id'],
            'repo_name': activity_record['repo']['name'],
            'created_at': activity_record['created_at'],
            'repo_languages': langs,
        }
        writer.writerow(data)
        readme_file.write(readme + '\n\n')

    input_file.close()
    output_file.close()
    readme_file.close()
