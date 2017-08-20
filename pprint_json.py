import json


def load_data(filepath):
    with open(filepath, 'r') as fp:
        parsed_file = json.load(fp)
        return parsed_file


def pretty_print_json(data):
    data = load_data(filepath)
    pretty_json = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=False)
    return pretty_json


if __name__ == '__main__':
    filepath = input('Введите путь до файла: ')
    print(pretty_print_json(filepath))

