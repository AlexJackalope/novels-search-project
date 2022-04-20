import ItchIoParser


def main():
    parser = ItchIoParser.ItchIoParser(10)
    games_info = parser.get_games()
    print('that\'s it')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
