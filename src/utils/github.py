import json
import glob
import os
import requests
from dotenv import load_dotenv, find_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)
GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN')


def retrieve_repo_readme(repo):
    url = f"https://raw.githubusercontent.com/{repo['name']}/master/README.md"
    response = requests.get(url)
    return response.text if response.status_code == 200 else ''


def retrieve_repo_languages(repo):
    headers = {'Authorization': 'token ' + GITHUB_ACCESS_TOKEN}
    url = f"{repo['url']}/languages"
    response = requests.get(url, headers=headers)
    return response.text if response.status_code == 200 else ''


def collect_repos_description(data_files_pattern):
    for fname in glob.glob(data_files_pattern):
        name, ext = os.path.splitext(fname)

        input_file = open(fname, 'r')
        output_file = open(f'{name}-extra{ext}', 'w')

        for line in input_file:
            activity_record = json.loads(line)
            readme = retrieve_repo_readme(activity_record.get('repo'))
            langs = retrieve_repo_languages(activity_record.get('repo'))
            json.dump({
                'id': activity_record['id'],
                'repo': {
                    'id': activity_record['repo']['id'],
                    'readme': readme,
                    'languages': langs}},
                output_file)
            output_file.write('\n')

        input_file.close()
        output_file.close()
