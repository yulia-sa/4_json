# Prettify JSON

This script pretty-prints the contents of unformatted JSON.

# Quickstart

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>

```

Output example:

```#!bash

{
    "weather": [
        {
            "id": 300,
            "main": "Drizzle",
            "description": "light intensity drizzle",
            "icon": "09d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 280.32,
        "pressure": 1012,
        "humidity": 81,
        "temp_min": 279.15,
        "temp_max": 281.15
    },
    "visibility": 10000,
    "wind": {
        "speed": 4.1,
        "deg": 80
    },
    "clouds": {
        "all": 90
    },
    "id": 2643743,
    "name": "City",
    "cod": 200
}

```




# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
