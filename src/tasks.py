import json
import csv
import os

from config import huey, EVENTS
from util.github import (
    retrieve_repo_languages, retrieve_repo_readme, clean_readme)


@huey.task()
def collect_data(data_file):
    print('Start processing ' + data_file)

    field_names = [
        'id',
        'event_type',
        'actor_id',
        'actor_login',
        'repo_id',
        'repo_name',
        'created_at',
        'repo_languages',
    ]

    name, ext = os.path.splitext(data_file)

    with open(data_file, 'r') as input_file, \
         open(name + '.csv', 'w') as output_file, \
         open(name + '-readme', 'w') as readme_file:

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
                'event_type': activity_record['type'],
                'actor_id': activity_record['actor']['id'],
                'actor_login': activity_record['actor']['login'],
                'repo_id': activity_record['repo']['id'],
                'repo_name': activity_record['repo']['name'],
                'created_at': activity_record['created_at'],
                'repo_languages': langs,
            }

            writer.writerow(data)
            readme_file.write(readme + '\n\n')
