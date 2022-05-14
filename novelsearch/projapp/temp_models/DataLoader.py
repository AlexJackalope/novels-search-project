import os
import sys
import pickle
from . import GameInfo
from . import ItchIoParser

sys.modules['GameInfo'] = GameInfo


def load_pickled():
    dir_name = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.abspath(os.path.join(dir_name, '..', '..', '..', 'SomeGamesInfo.pickle'))
    print(file_path)
    with open(file_path, 'rb') as games:
        loaded = pickle.load(games)
    return loaded
