from src.utils.github import collect_repos_description


ARCHIVE_PATTERN = 'dataset/*.json'


if __name__ == '__main__':
    collect_repos_description(ARCHIVE_PATTERN)
