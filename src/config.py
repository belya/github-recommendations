import os

from huey import RedisHuey
from dotenv import load_dotenv

huey = RedisHuey()

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN')

EVENTS = [
    'CommitCommentEvent',
    'CreateEvent',
    'WatchEvent',
    'ForkEvent',
    'IssueEvent',
    'IssueCommentEvent',
    'PullRequestEvent',
    'PushEvent',
    'MemberEvent',
]
