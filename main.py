import ItchIoParser
import pickle


def load_from_itch():
    parser = ItchIoParser.ItchIoParser(20)
    return parser.get_games()


def load_pickled():
    with open('SomeGamesInfo.pickle', 'rb') as games:
        loaded = pickle.load(games)
    return loaded


def main():
    games_info = load_pickled()
    print('that\'s it')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
