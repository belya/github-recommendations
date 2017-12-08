import glob

from config import huey
from tasks import collect_data


ARCHIVE_PATTERN = '../dataset/*.json'


if __name__ == '__main__':
    for fname in glob.glob(ARCHIVE_PATTERN):
        collect_data(fname)
