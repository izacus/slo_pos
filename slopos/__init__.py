# Part of speech tagger for Sloveninan language
# Copyright (C) 2013 Jernej Virag
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

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



