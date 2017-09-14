import sys, json

filepath = sys.argv[1]


def load_data(filepath):
    try:
        with open(filepath, 'r') as fp:
            parsed_file = json.load(fp)
            return parsed_file

    except (FileNotFoundError) as err:
        print('Файл не найден!')
    except (IOError, Exception) as err:
        print(err)                


def pretty_print_json(data):
    data = load_data(filepath)
    pretty_json = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=False)
    return pretty_json


if __name__ == '__main__':
    print(pretty_print_json(filepath))
