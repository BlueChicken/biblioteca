import json
import os
import re
from glob import glob

ID_REGEX = re.compile(r'[A-Z]{3}\d{4}')

PATH = '../*/*.json'

if __name__ == '__main__':
    for path in glob(PATH):
        print(path)

        if os.stat(path).st_size == 0:
            continue

        with open(path) as json_file:
            data = json.load(json_file)

        assert ID_REGEX.match(data['id']) is not None

        assert data['name'] != ''

        for entry in data['entries']:
            assert entry['title'] != ''
            assert entry['link'] != ''