import json


def load_data(filepath):
    try:
        with open(filepath, 'r') as file_object:
            parsed_file = json.load(file_object)
            return parsed_file
    
    except (IOError, Exception):
        return None


def print_pretty_json(raw_data):
    pretty_json = json.dumps(
        raw_data,
        indent=4,
        ensure_ascii=False,
        sort_keys=False
    )
    print(pretty_json)


if __name__ == '__main__':
    import os
    import sys

    if len(sys.argv) > 1:
        filepath = sys.argv[1]

        if not os.path.isfile(filepath):
            print('Файл не найден!')
        else:
            raw_data = load_data(filepath)

            if raw_data is None:
                print('Произошла ошибка!')
            else:
                print_pretty_json(raw_data)

    else:
        print('Не задан путь к файлу!')
