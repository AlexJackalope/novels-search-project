from multiprocessing import freeze_support

import pandas as pd
import os
import re
import gensim.corpora as corpora
import gensim
from gensim.utils import simple_preprocess
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from pprint import pprint


class TextClassifier:
    def __init__(self, game_info=None, text_count=1):
        # self.text_count = text_count - вот эта строка зачем? Не используется
        # self.game_info = game_info
        self.stop_words = stopwords.words('russian', 'english')
        # self.stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
        self.stop_words.extend(
            ['the', 'one', 'two', 'of', 'you', 'your', 'in', 'game', 'to',
             'is', 'for', 'on', 'with', 'it', 'this', 'will', 'by', 'that',
             'if', 'be', 'or', 'as', 'an', 'are', 'all', 'but', 'about', 'can',
             'so', 'play', 'story', 'novel', 'from', 'out', 'he', 'she', 'not',
             'they', 'their', 'what', 'up', 'have', 'her', 'more', 'demo',
             'at', 'who', 'fill', 'there', 'was', 'we', 'please', 'new', 'and',
             'features', 'music', 'content', 'version', 'me', 'my', 'like',
             'some', 'how', 'characters', 'his', 'get', 'visual', 'other',
             'also', 'into', 'made', 'us', 'only'])

        # Read from csv
        # self.papers = pd.read_csv('papers.csv')
        # self.papers = self.papers.drop(columns=['id', 'event_type', 'pdf_name'], axis=1).sample(100)

        # Get pd from parameters
        self.papers = game_info

        self.data_cleaning()
        self.data = self.papers.paper_text_processed.values.tolist()

        self.data_words = self.tokenize()
        self.data_words = self.remove_stop_words()

        self.id2word = corpora.Dictionary(self.data_words)
        '''
        создаем словарик для слов, который заюзаем для корпуса
        '''
        texts = self.data_words
        self.corpus = [self.id2word.doc2bow(text) for text in texts]
        '''
        делаем корпус, он дает всем словам теги и возвращает тапл с этими тегами и количеством этих тегов
        '''

    def data_cleaning(self):
        self.papers['paper_text_processed'] = \
            self.papers['paper_text'].map(lambda x: re.sub('[,\.!?\n\t\r]', '', x))

        self.papers['paper_text_processed'] = \
            self.papers['paper_text_processed'].map(lambda x: x.lower())

    def tokenize(self):
        def sent_to_words(sentences):
            for sentence in sentences:
                yield (gensim.utils.simple_preprocess(str(sentence), deacc=True))#deacc уберет пунктуацию

        return list(sent_to_words(self.data))

    def remove_stop_words(self):
        def remove_stopwords(texts):
            return [[word for word in simple_preprocess(str(doc))
                     if word not in self.stop_words] for doc in texts]

        return remove_stopwords(self.data_words)

    def trainLDA(self, num_topics=5):
        lda_model = gensim.models.LdaMulticore(corpus=self.corpus,
                                               id2word=self.id2word,
                                               num_topics=num_topics)

        pprint(lda_model.print_topics())
        # doc_lda = lda_model[self.corpus]
        return lda_model.print_topics()


if __name__ == '__main__':
    freeze_support()
    b = TextClassifier()
    b.trainLDA()
