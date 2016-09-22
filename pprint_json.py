import json
import pprint


def load_data(filepath):
    with open(filepath, encoding='UTF-8') as file:
        return json.load(file)
    pass


def pretty_print_json(data):
    lst = load_data(data)
    return pprint.pprint(lst)
    pass


if __name__ == '__main__':
    path = 'D:/test/alco.json'
    pretty_print_json(path)
    pass
