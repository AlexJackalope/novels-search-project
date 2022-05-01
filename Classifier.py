import re
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
#import spacy


class Classifier:
    stop_words = stopwords.words('russian', 'english')
    stop_words.extend(
        ['the', 'one', 'two', 'of', 'you', 'your', 'in', 'game', 'to',
         'is', 'for', 'on', 'with', 'it', 'this', 'will', 'by', 'that',
         'if', 'be', 'or', 'as', 'an', 'are', 'all', 'but', 'about', 'can',
         'so', 'play', 'story', 'novel', 'from', 'out', 'he', 'she', 'not',
         'they', 'their', 'what', 'up', 'have', 'her', 'more', 'demo',
         'at', 'who', 'fill', 'there', 'was', 'we', 'please', 'new', 'and',
         'features', 'music', 'content', 'version', 'me', 'my', 'like',
         'some', 'how', 'characters', 'his', 'get', 'visual', 'other', 'll',
         'also', 'into', 'made', 'us', 'only', 'has', 'our', 'time', 'find',
         'life', 'world', 'make', 'just', 'any', 'them', 'when', 'do', 'now',
         'help', 're', 'free', 'endings', 'no', 'first', 'here', 'want',
         'through', 'been', 'available', 'after', 'where', 'full', 'different',
         'follow', 'may', 'credits', 'own', 'll', 'character', 'even', 'him',
         'than', 'way', 'being', 'games', 'each', 'warning', 'over',
         'contains', 'see', 'day', 'words', 'which', 'around', 'something',
         'know', 'would', 'take', 'right', 've', 'well', 'much', 'while',
         'work', 'project', 'three', 'best', 'still', 'don', 'jam', 'end',
         'many', 'enjoy', 'join', 'playing', 'really', 'every', 'little',
         'most', 'things', 'download', 'note', 'come', 'keep', 'very', 'its',
         'feel', 'hope', 'ending', 'main', ])
    #en_nlp = spacy.load("en_core_web_sm")
    #ru_nlp = spacy.load("ru_core_news_sm")
    en_letter = re.compile(r'[a-z]')
    ru_letter = re.compile(r'[а-я]')

    def __init__(self, game_info=None):
        self.pd_texts = game_info
        self.pd_texts['paper_text'] = \
            self.pd_texts['paper_text'].apply(lambda x: self.clean_up_text(x))

    def get_tags(self):
        cv = CountVectorizer()
        vocab = cv.fit(self.pd_texts['paper_text'].values)
        a = pd.DataFrame(data=cv.transform(self.pd_texts['paper_text']).toarray(),
                     columns=vocab.get_feature_names())
        # сделать приведение к начальной форме
        # попробовать вытащить биграммы как теги
        top_tags = a.sum(axis=0).sort_values(ascending=False)[:40].index
        tag_to_texts = dict()
        for tag in top_tags:
            texts = [one['link'] for index, one in self.pd_texts.iterrows()
                     if tag in one['paper_text']]
            tag_to_texts[tag] = texts
        return tag_to_texts

    def clean_up_text(self, text):
        doc = re.sub("[\(\[].*?[\)\]]", "", text)  # Remove the "written by" caption
        doc = doc.replace(u'\n', u'').replace(u'\r', u'')
        doc = re.sub(r'[^\s\w]', '', doc)
        doc = re.sub('\s+', ' ', doc)
        doc = doc.lower().split()
        doc = ' '.join([t for t in doc
               if not t in Classifier.stop_words and len(t) > 1 and not t.isdigit()])
        return doc

    @staticmethod
    def lemmatize(word):
        if Classifier.en_letter.search(word):
            return Classifier.en_nlp(word)
        if Classifier.ru_letter.search(word):
            return Classifier.ru_nlp(word)
        return word
