import pickle
import pandas as pd

import ItchIoParser
import TextClassifier


def load_from_itch():
    parser = ItchIoParser.ItchIoParser(20)
    return parser.get_games()


def load_pickled():
    with open('SomeGamesInfo.pickle', 'rb') as games:
        loaded = pickle.load(games)
    return loaded


def main():
    games_info = load_pickled()
    games_info_df = pd.DataFrame(data={
        'paper_text': [gi.description for gi in games_info]
    })
    classifier = TextClassifier.TextClassifier(games_info_df)
    text_topics = classifier.trainLDA(15)
    print('that\'s it')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
