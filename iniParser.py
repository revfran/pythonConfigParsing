import configparser


def main():
    config = configparser.ConfigParser()

    config.read('config.ini')

    print(f"config: {config.sections()}")

    print(f"config: hello {config['DEFAULTS']['hello']}")

    for section in config.sections():
        for x in config[section]:
            print(f"x: {x}, value: {config[section][x]}")


if __name__ == '__main__':
    main()
