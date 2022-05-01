import pickle
import pandas as pd

import ItchIoParser
import TextClassifier
import Classifier


def load_from_itch():
    parser = ItchIoParser.ItchIoParser(20)
    return parser.get_games()


def load_pickled():
    with open('SomeGamesInfo.pickle', 'rb') as games:
        loaded = pickle.load(games)
    return loaded


def main():
    games_info = load_pickled()
    link_to_gi = {gi.link: gi for gi in games_info}
    games_info_df = pd.DataFrame(data={
        'paper_text': [gi.description for gi in games_info],
        'link': [gi.link for gi in games_info]
    })

    # classifier = TextClassifier.TextClassifier(games_info_df)
    # text_topics = classifier.trainLDA(15)

    classifier = Classifier.Classifier(games_info_df)
    pop_tags_to_links = classifier.get_tags()

    # сделать фильтрацию по тегам
    # сделать словарь пользовательских альбомов
    # посчитать какие теги/игры часто используются вместе с данной игрой

    print('this is this, that\'s that')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
