import pickle
import types
import os
from collections import Iterable

this_dir = os.path.dirname(os.path.realpath(__file__))
tagger = pickle.load(open(os.path.join(this_dir, "sl-tagger.pickle"), "rb"))

def tag(sentence):
    """
    Tags a sentence with POS symbols. Expected parameter is either text (which will be tokenized on word an punctuation
    boundaries) or a list of words.

    Returns a list of tuples in form (word, tag)
    """
    if isinstance(sentence, types.StringTypes):
        from nltk.tokenize import WordPunctTokenizer
        return tagger.tag(WordPunctTokenizer().tokenize(sentence))
    elif isinstance(sentence, Iterable):
        return tagger.tag(sentence)
    else:
        raise ArgumentError("Tag parameter MUST be either a string or an iterable collection of words!")



