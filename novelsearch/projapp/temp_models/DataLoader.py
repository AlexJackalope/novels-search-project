import os
import pickle
from . import ItchIoParser


def load_pickled():
    dir_name = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_name, 'SomeGamesInfo.pickle')
    with open(file_path, 'rb') as games:
        loaded = pickle.load(games)
    return loaded


def load_from_itch(pages):
    parser = ItchIoParser.ItchIoParser(pages)
    return parser.get_games()
