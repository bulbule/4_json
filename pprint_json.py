import json
import os
import sys


def load_data(filepath):

    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf-8') as data_file:
        return json.loads(data_file.read())


def pretty_print_json(parsed_json):

    print(
        json.dumps(
            parsed_json,
            ensure_ascii=False,
            indent=4,
            sort_keys=True))


if __name__ == '__main__':

    if len(sys.argv) == 1:
        sys.exit('Usage: python pprint_json.py < filepath >')
    else:
        your_json = load_data(sys.argv[1])

    if not your_json:
        sys.exit('Error: the file %s was not found!' % sys.argv[1])
    else:
        pretty_print_json(your_json)
