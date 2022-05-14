import pickle
import pandas as pd
import ItchIoParser
import Classifier
import Filtration


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
    classifier = Classifier.Classifier(games_info_df)
    pop_tags_to_links = classifier.get_tags()
    filtration = Filtration.Filtration(pop_tags_to_links)
    print(filtration.find_perfect_match("release", "everyone"))

    ## Classifier:
    ## сделать приведение к начальной форме
    ## попробовать вытащить биграммы как теги
    # сделать фильтрацию по тегам (пользователь указывает один или несколько тегов и получает список игр в порядке убывания приоритета (вдруг подходящих игр не окажется вообще, пустой список будет грустным))
    # сделать словарь пользовательских альбомов
    # посчитать какие теги/игры часто используются вместе с данной игрой

    print('this is this, that\'s that')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
