import json

import os


def main():

    with open('config.json', 'r') as f:
        config = json.load(f)

    print(f"json data: {config}")
    print(config['hey'])

    print(f"config:{(config['hey'])['sample']}")


if __name__ == '__main__':
    main()